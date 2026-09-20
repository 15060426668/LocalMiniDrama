/**
 * 自定义分镜提示词解析器
 * 解析用户导入的结构化分镜文本格式
 */

export function parseCustomStoryboards(text, context = {}) {
  if (!text || !text.trim()) {
    throw new Error('导入文本为空')
  }

  const { characterMap = {}, sceneMap = {}, episodeId = null } = context
  const storyboards = []
  let globalShotNumber = 1

  const videoBlocks = splitByVideoNumber(text)

  for (const block of videoBlocks) {
    try {
      const parsed = parseVideoBlock(block, {
        characterMap,
        sceneMap,
        episodeId,
        startShotNumber: globalShotNumber
      })
      storyboards.push(...parsed.storyboards)
      globalShotNumber = parsed.nextShotNumber
    } catch (e) {
      console.warn('解析视频块失败:', e.message, block.slice(0, 100))
    }
  }

  if (storyboards.length === 0) {
    throw new Error('未解析到任何分镜，请检查格式是否正确')
  }

  return storyboards
}

function splitByVideoNumber(text) {
  const regex = /={10,}【视频编号[\d-]+】={10,}/g
  const parts = text.split(regex)
  return parts.filter(p => p.trim()).map(p => p.trim())
}

function parseVideoBlock(block, context) {
  const { characterMap = {}, sceneMap = {}, episodeId, startShotNumber } = context

  const headerMatch = block.match(/总时长：([\d.]+)s\s*｜\s*场景：(.+?)\s*｜\s*人物：(.+?)(?=\n|$)/)
  if (!headerMatch) {
    throw new Error('未找到头部信息（总时长、场景、人物）')
  }

  const totalDuration = parseFloat(headerMatch[1])
  const sceneName = headerMatch[2].trim()
  const characterNames = headerMatch[3].split('、').map(n => n.trim()).filter(Boolean)

  const sceneStateMatch = block.match(/【场景与连续状态】([\s\S]*?)(?=【|$)/)
  const lightingMatch = block.match(/【光线】([\s\S]*?)(?=【|$)/)
  const lightingLockMatch = block.match(/【本编号场景光影锁】([\s\S]*?)(?=【|$)/)
  const charactersMatch = block.match(/【出场人物】([\s\S]*?)(?=【|$)/)

  const sceneState = sceneStateMatch ? sceneStateMatch[1].trim() : ''
  const lighting = lightingMatch ? lightingMatch[1].trim() : ''
  const lightingLock = lightingLockMatch ? lightingLockMatch[1].trim() : ''
  
  // 优先使用【出场人物】区块，否则使用头部的人物信息
  let charactersText = charactersMatch ? charactersMatch[1].trim() : characterNames.join('、')
  
  // 清理角色名：只保留第一行，去除后续的镜头描述
  charactersText = charactersText.split(/\n/)[0].trim()

  const sceneId = matchScene(sceneName, sceneMap)

  const allCharacterNames = charactersText.split(/[、，,]/).map(n => n.trim()).filter(Boolean)
  
  // 去重
  const uniqueCharacterNames = [...new Set(allCharacterNames)]
  
  // Frontend preview: store names only (IDs will be matched on backend)
  const characterList = uniqueCharacterNames.map(name => ({
    id: null,
    name: name
  }))

  const shots = parseShots(block)

  validateDurations(shots, totalDuration)

  // Build universal_segment_text
  const universalSegmentText = buildUniversalSegmentText(shots, totalDuration, sceneName, lighting)

  // Build dialogue from all shots
  const allDialogues = shots
    .map(shot => shot.dialogue)
    .filter(d => d && d.trim())
    .join('\n')

  const storyboard = {
    episode_id: episodeId,
    storyboard_number: startShotNumber,
    title: `视频${headerMatch[0].match(/【视频编号([\d-]+)】/)?.[1] || startShotNumber}`,
    description: sceneState,
    location: sceneName,
    time: '',
    duration: totalDuration,
    action: lightingLock || '',
    dialogue: allDialogues || null,
    narration: '',
    result: '',
    atmosphere: '',
    shot_type: shots[0]?.shotType || '中景',
    angle: shots[0]?.angle || '',
    angle_h: shots[0]?.angleH || '',
    angle_v: shots[0]?.angleV || '',
    angle_s: shots[0]?.angleS || '',
    movement: shots[0]?.movement || '',
    lighting_style: lighting,
    depth_of_field: '',
    universal_segment_text: universalSegmentText,
    video_prompt: '',
    image_prompt: '',
    polished_prompt: '',
    characters: JSON.stringify(characterList),
    scene_id: sceneId,
    creation_mode: 'universal',
    status: 'pending',
    segment_index: 1,
    segment_title: sceneName,
  }

  return {
    storyboards: [storyboard],
    nextShotNumber: startShotNumber + 1
  }
}

function parseShots(block) {
  const shots = []
  
  const shotRegex = /镜头(\d+)（([\d.]+)s）([^\n]+)\n\s*画面描述（大白话）：([\s\S]*?)\n\s*备注：([\s\S]*?)(?=镜头\d+|$)/g
  
  let match
  while ((match = shotRegex.exec(block)) !== null) {
    const number = parseInt(match[1])
    const duration = parseFloat(match[2])
    const shotDesc = match[3].trim()
    const visualDesc = match[4].trim()
    const remark = match[5].trim()

    const { shotType, angle, angleH, angleV, angleS, movement } = parseShotDescription(shotDesc)
    const dialogue = parseDialogue(remark)
    const transition = parseTransition(visualDesc)

    shots.push({
      number,
      duration,
      shotDesc,
      visualDescription: transition ? visualDesc.replace(transition.raw, '').trim() : visualDesc,
      transition,
      dialogue,
      shotType,
      angle,
      angleH,
      angleV,
      angleS,
      movement
    })
  }

  return shots
}

function parseShotDescription(desc) {
  const result = {
    shotType: '中景',
    angle: '',
    angleH: '',
    angleV: '',
    angleS: '',
    movement: ''
  }

  const shotTypeMap = {
    '全景': '全景',
    '中景': '中景',
    '近景': '近景',
    '特写': '特写',
    '双人近景': '近景',
    '动作近景': '近景',
    '中近景': '中近景',
    '大远景': '大远景',
    '远景': '远景',
    '中全景': '中全景',
    '大特写': '大特写'
  }

  for (const [keyword, type] of Object.entries(shotTypeMap)) {
    if (desc.includes(keyword)) {
      result.shotType = type
      break
    }
  }

  const angleMap = {
    '高机位': { h: '高', v: '俯', s: '' },
    '低机位': { h: '低', v: '仰', s: '' },
    '平视': { h: '平', v: '平', s: '' },
    '俯拍': { h: '', v: '俯', s: '' },
    '仰拍': { h: '', v: '仰', s: '' },
    '侧拍': { h: '侧', v: '平', s: '' },
    '肩后': { h: '过肩', v: '平', s: '' },
    '三分之四侧': { h: '3/4侧', v: '平', s: '' }
  }

  for (const [keyword, angles] of Object.entries(angleMap)) {
    if (desc.includes(keyword)) {
      result.angle = keyword
      result.angleH = angles.h
      result.angleV = angles.v
      result.angleS = angles.s
      break
    }
  }

  const movementMap = {
    '推近': '推镜头',
    '推镜头': '推镜头',
    '拉远': '拉镜头',
    '拉镜头': '拉镜头',
    '横移': '横移',
    '缓慢横移': '横移',
    '快速横移': '横移',
    '跟拍': '跟镜头',
    '跟镜头': '跟镜头',
    '环绕': '环绕',
    '升降': '升降',
    '静态': '固定镜头',
    '浅焦': '固定镜头',
    '固定': '固定镜头'
  }

  for (const [keyword, movement] of Object.entries(movementMap)) {
    if (desc.includes(keyword)) {
      result.movement = movement
      break
    }
  }

  return result
}

function parseDialogue(remark) {
  if (!remark || remark.includes('无台词')) {
    return ''
  }

  const dialogueRegex = /(.+?)（台词\d+）：[""](.+?)[""]/
  const match = remark.match(dialogueRegex)

  if (match) {
    return `${match[1].trim()}：${match[2].trim()}`
  }

  return remark.trim()
}

function parseTransition(visualDesc) {
  const transitionRegex = /→衔接至视频编号(\d+)：(.+?)(?=；|$)/
  const match = visualDesc.match(transitionRegex)

  if (match) {
    return {
      raw: match[0],
      nextVideoNumber: parseInt(match[1]),
      description: match[2].trim()
    }
  }

  return null
}

function matchCharacter(name, characterMap) {
  if (characterMap[name]) {
    return characterMap[name]
  }

  const baseName = name.split('·')[0].trim()
  if (characterMap[baseName]) {
    return characterMap[baseName]
  }

  const normalizedName = name.replace(/[·\s]/g, '')
  for (const [key, id] of Object.entries(characterMap)) {
    if (key.replace(/[·\s]/g, '') === normalizedName) {
      return id
    }
  }

  console.warn(`未找到角色: ${name}`)
  return null
}

function matchScene(name, sceneMap) {
  if (sceneMap[name]) {
    return sceneMap[name]
  }

  const nameWithoutPrefix = name.replace(/^SC\d+/i, '').trim()
  if (sceneMap[nameWithoutPrefix]) {
    return sceneMap[nameWithoutPrefix]
  }

  for (const [key, id] of Object.entries(sceneMap)) {
    if (key.includes(nameWithoutPrefix) || nameWithoutPrefix.includes(key)) {
      return id
    }
  }

  console.warn(`未找到场景: ${name}`)
  return null
}

function validateDurations(shots, totalDuration) {
  const sum = shots.reduce((acc, shot) => acc + shot.duration, 0)
  const diff = Math.abs(sum - totalDuration)

  if (diff > 0.2) {
    console.warn(`时长不匹配：标注总时长${totalDuration}s，各镜头时长总和${sum.toFixed(1)}s`)
  }

  return shots
}

/**
 * 构建全能片段文本（universal_segment_text）
 */
function buildUniversalSegmentText(shots, totalDuration, sceneName, lighting) {
  const lines = []

  // 第1行：环境描述
  lines.push(`场景：${sceneName}。光线：${lighting || '自然光'}。`)

  // 第2行：子分镜数量声明
  lines.push(`由以下${shots.length}个分镜组成，总时长${totalDuration}秒。`)

  // 第3行：参考图约束
  lines.push('参考图：场景图→角色图顺序。')

  // 第4行起：各子分镜描述
  for (let i = 0; i < shots.length; i++) {
    const shot = shots[i]
    const shotLine = `分镜${i + 1}：${shot.duration}秒: ${shot.visualDescription}`
    lines.push(shotLine)
  }

  return lines.join('\n')
}

export function previewParseResult(text, context = {}) {
  try {
    const storyboards = parseCustomStoryboards(text, context)
    return {
      success: true,
      count: storyboards.length,
      storyboards: storyboards.map(sb => ({
        number: sb.storyboard_number,
        title: sb.title,
        duration: sb.duration,
        characters: JSON.parse(sb.characters).length,
        scene: sb.location,
        shotType: sb.shot_type,
        movement: sb.movement,
      }))
    }
  } catch (e) {
    return {
      success: false,
      error: e.message
    }
  }
}