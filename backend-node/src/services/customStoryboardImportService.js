/**
 * 自定义分镜导入服务
 * 解析并批量导入用户自定义的分镜提示词
 */

/**
 * 批量导入自定义分镜
 * @param {import('better-sqlite3').Database} db
 * @param {object} log
 * @param {object} params
 * @returns {object} { success, count, storyboards }
 */
function importCustomStoryboards(db, log, params) {
  const { episodeId, text, characterMap = {}, sceneMap = {} } = params;

  if (!episodeId) {
    throw new Error('episodeId 必填');
  }

  if (!text || !text.trim()) {
    throw new Error('导入文本不能为空');
  }

  // 验证剧集存在
  const episode = db.prepare(
    'SELECT id, drama_id FROM episodes WHERE id = ? AND deleted_at IS NULL'
  ).get(episodeId);

  if (!episode) {
    throw new Error('剧集不存在');
  }

  // 解析文本
  const storyboards = parseCustomStoryboardText(text, { characterMap, sceneMap, episodeId, db });

  if (storyboards.length === 0) {
    throw new Error('未解析到任何分镜');
  }

  // 获取当前最大分镜编号
  const maxNumRow = db.prepare(
    'SELECT MAX(storyboard_number) as maxNum FROM storyboards WHERE episode_id = ? AND deleted_at IS NULL'
  ).get(episodeId);

  let nextNumber = (maxNumRow?.maxNum || 0) + 1;

  // 批量插入
  const insertStmt = db.prepare(`
    INSERT INTO storyboards (
      episode_id, scene_id, storyboard_number, title, description,
      location, time, duration, dialogue, narration, action, result, atmosphere,
      shot_type, angle, angle_h, angle_v, angle_s, movement, lighting_style, depth_of_field,
      universal_segment_text, video_prompt, image_prompt, polished_prompt,
      characters, creation_mode, status, segment_index, segment_title,
      created_at, updated_at
    ) VALUES (
      ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'universal', 'pending', ?, ?, ?, ?
    )
  `);

  const now = new Date().toISOString();
  const insertedIds = [];

  db.transaction(() => {
    for (const sb of storyboards) {
      const result = insertStmt.run(
        episodeId,
        sb.scene_id || null,
        nextNumber,
        sb.title || null,
        sb.description || null,
        sb.location || null,
        sb.time || null,
        sb.duration || 5,
        sb.dialogue || null,
        sb.narration || null,
        sb.action || null,
        sb.result || null,
        sb.atmosphere || null,
        sb.shot_type || null,
        sb.angle || null,
        sb.angle_h || null,
        sb.angle_v || null,
        sb.angle_s || null,
        sb.movement || null,
        sb.lighting_style || null,
        sb.depth_of_field || null,
        sb.universal_segment_text || null,
        sb.video_prompt || null,
        sb.image_prompt || null,
        sb.polished_prompt || null,
        sb.characters || '[]',
        sb.segment_index || 1,
        sb.segment_title || '',
        now,
        now
      );

      insertedIds.push(result.lastInsertRowid);
      nextNumber++;
    }
  })();

  log.info('Custom storyboards imported', {
    episode_id: episodeId,
    count: storyboards.length,
    ids: insertedIds
  });

  return {
    success: true,
    count: storyboards.length,
    storyboards: storyboards.map((sb, i) => ({ ...sb, id: insertedIds[i] }))
  };
}

/**
 * 解析自定义分镜文本（与前端解析器逻辑一致）
 */
function parseCustomStoryboardText(text, context) {
  const { characterMap = {}, sceneMap = {}, episodeId, db } = context;
  const storyboards = [];
  let globalShotNumber = 1;

  const videoBlocks = splitByVideoNumber(text);

  for (const block of videoBlocks) {
    try {
      const parsed = parseVideoBlock(block, {
        characterMap,
        sceneMap,
        episodeId,
        startShotNumber: globalShotNumber,
        db
      });
      storyboards.push(...parsed.storyboards);
      globalShotNumber = parsed.nextShotNumber;
    } catch (e) {
      console.warn('解析视频块失败:', e.message);
    }
  }

  return storyboards;
}

function splitByVideoNumber(text) {
  const regex = /={10,}【视频编号[\d-]+】={10,}/g;
  const parts = text.split(regex);
  return parts.filter(p => p.trim()).map(p => p.trim());
}

function parseVideoBlock(block, context) {
  const { characterMap, sceneMap, episodeId, startShotNumber, db } = context;

  const headerMatch = block.match(/总时长：([\d.]+)s\s*｜\s*场景：(.+?)\s*｜\s*人物：(.+?)(?=\n|$)/);
  if (!headerMatch) {
    throw new Error('未找到头部信息');
  }

  const totalDuration = parseFloat(headerMatch[1]);
  const sceneName = headerMatch[2].trim();
  const characterNames = headerMatch[3].split('、').map(n => n.trim()).filter(Boolean);

  const sceneStateMatch = block.match(/【场景与连续状态】([\s\S]*?)(?=【|$)/);
  const lightingMatch = block.match(/【光线】([\s\S]*?)(?=【|$)/);
  const lightingLockMatch = block.match(/【本编号场景光影锁】([\s\S]*?)(?=【|$)/);
  const charactersMatch = block.match(/【出场人物】([\s\S]*?)(?=【|$)/);

  const sceneState = sceneStateMatch ? sceneStateMatch[1].trim() : '';
  const lighting = lightingMatch ? lightingMatch[1].trim() : '';
  const lightingLock = lightingLockMatch ? lightingLockMatch[1].trim() : '';
  
  // 优先使用【出场人物】区块，否则使用头部的人物信息
  let charactersText = charactersMatch ? charactersMatch[1].trim() : characterNames.join('、');
  
  // 清理角色名：只保留第一行，去除后续的镜头描述
  // 例如："丹珍、林君雪\n\n镜头01..." -> "丹珍、林君雪"
  charactersText = charactersText.split(/\n/)[0].trim();

  const sceneId = matchScene(sceneName, sceneMap, db, episodeId);

  // Auto-match characters from database by name
  const allCharacterNames = charactersText.split(/[、，,]/).map(n => n.trim()).filter(Boolean);
  
  // 去重：避免同一个视频块内重复匹配相同角色
  const uniqueCharacterNames = [...new Set(allCharacterNames)];
  const characterList = matchCharactersFromDatabase(context.db, episodeId, uniqueCharacterNames);

  const shots = parseShots(block);

  // Merge all shots into universal_segment_text format with @图片N references
  const universalSegmentText = buildUniversalSegmentText(shots, totalDuration, sceneName, lighting, sceneId, characterList);

  // Build dialogue from all shots
  const allDialogues = shots
    .map(shot => shot.dialogue)
    .filter(d => d && d.trim())
    .join('\n');

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
  };

  console.log('[导入分镜] 保存的分镜数据:', {
    title: storyboard.title,
    scene_id: sceneId,
    sceneName: sceneName,
    characters: storyboard.characters,
    characterList: characterList,
    hasSceneMatch: sceneId !== null,
    characterCount: characterList.length
  });

  return {
    storyboards: [storyboard],
    nextShotNumber: startShotNumber + 1
  };
}

function parseShots(block) {
  const shots = [];
  
  const shotRegex = /镜头(\d+)（([\d.]+)s）([^\n]+)\n\s*画面描述（大白话）：([\s\S]*?)\n\s*备注：([\s\S]*?)(?=镜头\d+|$)/g;
  
  let match;
  while ((match = shotRegex.exec(block)) !== null) {
    const number = parseInt(match[1]);
    const duration = parseFloat(match[2]);
    const shotDesc = match[3].trim();
    const visualDesc = match[4].trim();
    const remark = match[5].trim();

    const { shotType, angle, angleH, angleV, angleS, movement } = parseShotDescription(shotDesc);
    const dialogue = parseDialogue(remark);
    const transition = parseTransition(visualDesc);

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
    });
  }

  return shots;
}

function parseShotDescription(desc) {
  const result = {
    shotType: '中景',
    angle: '',
    angleH: '',
    angleV: '',
    angleS: '',
    movement: ''
  };

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
  };

  for (const [keyword, type] of Object.entries(shotTypeMap)) {
    if (desc.includes(keyword)) {
      result.shotType = type;
      break;
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
  };

  for (const [keyword, angles] of Object.entries(angleMap)) {
    if (desc.includes(keyword)) {
      result.angle = keyword;
      result.angleH = angles.h;
      result.angleV = angles.v;
      result.angleS = angles.s;
      break;
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
  };

  for (const [keyword, movement] of Object.entries(movementMap)) {
    if (desc.includes(keyword)) {
      result.movement = movement;
      break;
    }
  }

  return result;
}

function parseDialogue(remark) {
  if (!remark || remark.includes('无台词')) {
    return '';
  }

  const dialogueRegex = /(.+?)（台词\d+）：[""](.+?)[""]/;
  const match = remark.match(dialogueRegex);

  if (match) {
    return `${match[1].trim()}：${match[2].trim()}`;
  }

  return remark.trim();
}

function parseTransition(visualDesc) {
  const transitionRegex = /→衔接至视频编号(\d+)：(.+?)(?=；|$)/;
  const match = visualDesc.match(transitionRegex);

  if (match) {
    return {
      raw: match[0],
      nextVideoNumber: parseInt(match[1]),
      description: match[2].trim()
    };
  }

  return null;
}

function matchCharacter(name, characterMap) {
  if (characterMap[name]) {
    return characterMap[name];
  }

  const baseName = name.split('·')[0].trim();
  if (characterMap[baseName]) {
    return characterMap[baseName];
  }

  const normalizedName = name.replace(/[·\s]/g, '');
  for (const [key, id] of Object.entries(characterMap)) {
    if (key.replace(/[·\s]/g, '') === normalizedName) {
      return id;
    }
  }

  return null;
}

function matchScene(name, sceneMap, db, episodeId) {
  if (sceneMap[name]) {
    return sceneMap[name];
  }

  const nameWithoutPrefix = name.replace(/^SC\d+/i, '').trim();
  if (sceneMap[nameWithoutPrefix]) {
    return sceneMap[nameWithoutPrefix];
  }

  for (const [key, id] of Object.entries(sceneMap)) {
    if (key.includes(nameWithoutPrefix) || nameWithoutPrefix.includes(key)) {
      return id;
    }
  }

  // Try to auto-match from database
  if (db && episodeId) {
    const episode = db.prepare(
      'SELECT drama_id FROM episodes WHERE id = ? AND deleted_at IS NULL'
    ).get(episodeId);

    if (episode) {
      console.log('[场景匹配] 开始匹配场景:', name, 'drama_id:', episode.drama_id);
      
      // Get all scenes for this drama
      const allScenes = db.prepare(
        'SELECT id, location FROM scenes WHERE drama_id = ? AND deleted_at IS NULL ORDER BY location ASC'
      ).all(episode.drama_id);

      console.log('[场景匹配] 数据库中的场景列表:', allScenes.map(s => s.location));

      // Exact match
      let matched = allScenes.find(s => s.location === name);
      if (matched) {
        console.log('[场景匹配] 精确匹配成功:', name, '-> id:', matched.id);
        return matched.id;
      }

      // Fuzzy match: remove special characters
      const normalizedName = name.replace(/[·\s\-_]/g, '');
      matched = allScenes.find(s => s.location.replace(/[·\s\-_]/g, '') === normalizedName);
      if (matched) {
        console.log('[场景匹配] 模糊匹配成功:', name, '->', matched.location, 'id:', matched.id);
        return matched.id;
      }

      // Contains match
      matched = allScenes.find(s => s.location.includes(name) || name.includes(s.location));
      if (matched) {
        console.log('[场景匹配] 包含匹配成功:', name, '->', matched.location, 'id:', matched.id);
        return matched.id;
      }

      console.warn('[场景匹配] 未找到匹配的场景:', name);
    }
  }

  return null;
}

/**
 * 从数据库自动匹配角色
 * @param {import('better-sqlite3').Database} db
 * @param {number} episodeId
 * @param {string[]} names
 * @returns {Array<{id: number, name: string}>}
 */
function matchCharactersFromDatabase(db, episodeId, names) {
  // 获取该集所属的 drama_id
  const episode = db.prepare(
    'SELECT drama_id FROM episodes WHERE id = ? AND deleted_at IS NULL'
  ).get(episodeId);

  if (!episode) {
    console.warn('[角色匹配] 剧集不存在，无法匹配角色, episodeId:', episodeId);
    return [];
  }

  console.log('[角色匹配] 开始匹配, drama_id:', episode.drama_id, '角色名:', names);

  // 获取该 drama 下所有角色
  const allCharacters = db.prepare(
    'SELECT id, name FROM characters WHERE drama_id = ? AND deleted_at IS NULL ORDER BY name ASC'
  ).all(episode.drama_id);

  console.log('[角色匹配] 数据库中的角色列表:', allCharacters.map(c => c.name));

  const matchedCharacters = [];

  for (const name of names) {
    console.log('[角色匹配] 尝试匹配角色:', name);
    
    // 精确匹配
    let matched = allCharacters.find(c => c.name === name);
    if (matched) {
      console.log('[角色匹配] 精确匹配成功:', name, '-> id:', matched.id);
      matchedCharacters.push({
        id: matched.id,
        name: matched.name
      });
      continue;
    }

    // 模糊匹配：去掉特殊字符后比较
    const normalizedName = name.replace(/[·\s\-_]/g, '');
    matched = allCharacters.find(c => c.name.replace(/[·\s\-_]/g, '') === normalizedName);
    if (matched) {
      console.log('[角色匹配] 模糊匹配成功:', name, '->', matched.name, 'id:', matched.id);
      matchedCharacters.push({
        id: matched.id,
        name: matched.name
      });
      continue;
    }

    // 包含匹配
    matched = allCharacters.find(c => c.name.includes(name) || name.includes(c.name));
    if (matched) {
      console.log('[角色匹配] 包含匹配成功:', name, '->', matched.name, 'id:', matched.id);
      matchedCharacters.push({
        id: matched.id,
        name: matched.name
      });
      continue;
    }

    console.warn('[角色匹配] 未找到匹配的角色:', name);
  }

  console.log('[角色匹配] 匹配结果:', matchedCharacters.length, '个角色');
  return matchedCharacters;
}

/**
 * 构建全能片段文本（universal_segment_text）
 * 将所有镜头合并成系统标准格式，并自动添加 @图片N 引用
 * @param {Array} shots 镜头数组
 * @param {number} totalDuration 总时长
 * @param {string} sceneName 场景名称
 * @param {string} lighting 光线信息
 * @param {number|null} sceneId 场景ID（用于判断是否有场景参考图）
 * @param {Array<{id: number, name: string}>} characterList 角色列表
 * @returns {string} 全能片段文本
 */
function buildUniversalSegmentText(shots, totalDuration, sceneName, lighting, sceneId, characterList) {
  const lines = [];

  const hasScene = sceneId !== null;
  const hasCharacters = characterList && characterList.length > 0;
  
  // 第1行：环境描述（有图片引用时简化文案）
  if (hasScene) {
    lines.push(`@图片1 ${sceneName}。光线：${lighting || '自然光'}。`);
  } else {
    lines.push(`场景：${sceneName}。光线：${lighting || '自然光'}。`);
  }

  // 添加角色引用（有图片引用时只显示 @图片N + 角色名）
  if (hasCharacters) {
    const startIndex = hasScene ? 2 : 1;
    const charRefs = characterList.map((char, i) => {
      return `@图片${startIndex + i} ${char.name}`;
    }).join('、');
    lines.push(charRefs + '。');
  }

  // 子分镜数量声明
  lines.push(`由以下${shots.length}个分镜组成，总时长${totalDuration}秒。`);

  // 参考图约束
  lines.push('参考图：场景图→角色图顺序。');

  // 各子分镜描述
  for (let i = 0; i < shots.length; i++) {
    const shot = shots[i];
    const shotLine = `分镜${i + 1}：${shot.duration}秒: ${shot.visualDescription}`;
    lines.push(shotLine);
  }

  console.log('[buildUniversalSegmentText] 生成的全能提示词:', {
    hasScene,
    hasCharacters,
    characterCount: characterList?.length || 0,
    firstLine: lines[0],
    secondLine: lines[1]
  });

  return lines.join('\n');
}

module.exports = {
  importCustomStoryboards
};