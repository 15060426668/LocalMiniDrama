/**
 * 分镜 Excel 导入服务
 * 支持从结构化分镜文本导入分镜数据
 */

/**
 * 解析单个分镜块的文本内容
 * @param {string} blockText - 单个视频编号块的内容
 * @returns {object}
 */
function parseStoryboardBlock(blockText) {
  const result = { success: false };

  try {
    // 提取视频编号 (如"01-01")
    const videoIdMatch = blockText.match(/视频编号\s*([\d\-]+)/);
    if (!videoIdMatch) {
      return result;
    }
    result.videoId = videoIdMatch[1];

    // 提取总时长 (如"13.6s")
    const totalDurationMatch = blockText.match(/总时长[：:]\s*([\d.]+)s/);
    result.totalDuration = totalDurationMatch ? parseFloat(totalDurationMatch[1]) : null;

    // 提取场景（到第一个竖线或换行为止，兼容全/半角竖线）
    const sceneMatch = blockText.match(/场景[：:]\s*([^｜|\n]+)/);
    result.scene = sceneMatch ? sceneMatch[1].trim() : null;

    // 提取出场人物（"人物："优先，否则用"出场人物"）
    const charsMatch = blockText.match(/人物[：:]\s*([^\n]+)/);
    result.characters = charsMatch ? extractCharacters(charsMatch[1]) : [];

    // 提取场景与连续状态
    const scenarioMatch = blockText.match(/【场景与连续状态】\s*([^\n]+)/);
    result.scenarioDesc = scenarioMatch ? scenarioMatch[1].trim() : '';

    // 提取光线
    const lightingMatch = blockText.match(/【光线】\s*([^\n]+)/);
    result.lighting = lightingMatch ? lightingMatch[1].trim() : '';

    // 提取光影锁
    const logicLockMatch = blockText.match(/【本编号场景光影锁】\s*([^\n]+)/);
    result.logicLock = logicLockMatch ? logicLockMatch[1].trim() : '';

    // 解析所有镜头
    const shots = parseShotsFromBlock(blockText);
    result.shots = shots.length > 0 ? shots : null;

    if (result.shots && result.shots.length > 0) {
      result.success = true;
    }
  } catch (err) {
    console.error('parseStoryboardBlock error:', err);
  }

  return result;
}

/**
 * 提取人物列表（按顿号、逗号、分号分割）
 */
function extractCharacters(text) {
  if (!text || !text.trim()) return [];
  // 去掉句末的句号
  const cleaned = text.replace(/[。.]\s*$/, '');
  const parts = cleaned
    .split(/[、,，;；]/)
    .map((s) => s.trim())
    .filter((s) => s && s.length > 0);
  return parts;
}

/**
 * 解析单个分镜块中的所有镜头
 * 镜头行格式：镜头 01（3.4s）xxx描述（兼容全角/半角括号）
 */
function parseShotsFromBlock(blockText) {
  const shots = [];

  // 关键：镜头号 + 括号内秒数 + 括号后同行描述 + 后续多行内容，直到下一个"镜头"或结尾
  const shotPattern = /镜头\s*(\d+)\s*[（(]\s*([\d.]+)\s*s\s*[）)]([^\n]*)([\s\S]*?)(?=镜头\s*\d+\s*[（(]|$)/g;

  let match;
  while ((match = shotPattern.exec(blockText)) !== null) {
    const shotNo = parseInt(match[1], 10);
    const durationSec = parseFloat(match[2]);
    const headline = (match[3] || '').trim();
    const body = (match[4] || '').trim();

    const visualDesc = extractVisualDescription(body);
    const remarks = extractRemarks(body);
    const cameraInfo = extractCameraInfo(headline);

    shots.push({
      shotNo,
      durationSec,
      shotType: cameraInfo.shotType,
      cameraPos: cameraInfo.cameraPos,
      cameraMove: cameraInfo.cameraMove,
      headline,
      visualDesc,
      remarks,
    });
  }

  return shots;
}

/**
 * 从画面描述行提取纯文本内容（兼容全/半角括号与冒号）
 */
function extractVisualDescription(content) {
  const match = content.match(/画面描述[（(]?大白话[）)]?[：:]\s*(.+)/);
  return match ? match[1].trim() : '';
}

/**
 * 从备注行提取内容
 */
function extractRemarks(content) {
  const match = content.match(/备注[：:]\s*(.+)/);
  return match ? match[1].trim() : '';
}

/**
 * 从镜头描述中提取运镜信息
 */
function extractCameraInfo(description) {
  const result = { shotType: '', cameraPos: '', cameraMove: '' };

  const shotTypes = ['大特写', '特写', '全景', '中近景', '中景', '近景', '远景'];
  for (const shotType of shotTypes) {
    if (description.includes(shotType)) {
      result.shotType = shotType;
      break;
    }
  }

  const cameraPositions = ['高机位', '低机位', '平视', '侧拍', '肩后', '俯视', '仰拍'];
  for (const pos of cameraPositions) {
    if (description.includes(pos)) {
      result.cameraPos = pos;
      break;
    }
  }

  const cameraMoves = ['缓慢推近', '快速横移', '静态浅焦', '横移跟拍', '轻俯拍', '缓慢横移', '推近', '横移'];
  for (const move of cameraMoves) {
    if (description.includes(move)) {
      result.cameraMove = move;
      break;
    }
  }

  return result;
}

/**
 * 导入分镜到数据库
 * @param {import('better-sqlite3').Database} db
 * @param {object} log
 * @param {number} episodeId
 * @param {Array<{content:string}>} storyboardBlocks
 * @param {object} assetMapping - { scenes: {name:id}, characters: {name:id} }
 * @returns {{ success:boolean, imported:number, failed:number, errors:string[] }}
 */
function importStoryboardsFromExcel(db, log, episodeId, storyboardBlocks, assetMapping = {}) {
  const result = { success: false, imported: 0, failed: 0, errors: [] };

  const tx = db.transaction((blocks) => {
    let imported = 0;
    let failed = 0;

    blocks.forEach((block, idx) => {
      try {
        const parsed = parseStoryboardBlock(block.content);

        if (!parsed.success) {
          log.warn(`Failed to parse block ${idx + 1}`, { preview: (block.content || '').substring(0, 80) });
          failed++;
          result.errors.push(`第 ${idx + 1} 个分镜解析失败（无法识别镜头）`);
          return;
        }

        // 计算总时长：所有镜头秒数之和取整
        const durationSum = parsed.shots.reduce((sum, shot) => sum + shot.durationSec, 0);
        const finalDuration = Math.round(durationSum);

        const now = new Date().toISOString();
        const storyboardNumber = idx + 1;
        const mainShotDesc = (parsed.shots[0] && parsed.shots[0].visualDesc || '').substring(0, 30);
        const title = `${parsed.videoId}: ${mainShotDesc}`;

        // 组合台词（备注中含"台词"的行）
        const dialogue = parsed.shots
          .filter((s) => s.remarks && s.remarks.includes('台词'))
          .map((s) => s.remarks)
          .join('\n');

        const sbInsert = db.prepare(`
          INSERT INTO storyboards (
            episode_id, storyboard_number, title, location, duration,
            description, action, dialogue, atmosphere,
            shot_type, angle, movement, status, created_at, updated_at
          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', ?, ?)
        `);

        const info = sbInsert.run(
          episodeId,
          storyboardNumber,
          title,
          parsed.scene || '',
          finalDuration,
          parsed.scenarioDesc || '',
          parsed.shots.map((s) => s.visualDesc).filter(Boolean).join(' '),
          dialogue,
          parsed.lighting || '',
          parsed.shots[0] ? parsed.shots[0].shotType : '',
          parsed.shots[0] ? parsed.shots[0].cameraPos : '',
          parsed.shots[0] ? parsed.shots[0].cameraMove : '',
          now,
          now
        );

        const storyboardId = info.lastInsertRowid;

        // 关联场景
        if (parsed.scene && assetMapping.scenes && assetMapping.scenes[parsed.scene]) {
          db.prepare('UPDATE storyboards SET scene_id = ? WHERE id = ?').run(assetMapping.scenes[parsed.scene], storyboardId);
        }

        // 关联角色（写入 episode_characters）
        if (parsed.characters && parsed.characters.length > 0 && assetMapping.characters) {
          parsed.characters.forEach((charName) => {
            const characterId = assetMapping.characters[charName];
            if (characterId) {
              db.prepare('INSERT OR IGNORE INTO episode_characters (episode_id, character_id) VALUES (?, ?)').run(episodeId, characterId);
            }
          });
        }

        // 存储镜头详情到 frame_prompts
        const insertFramePrompt = db.prepare(`
          INSERT INTO frame_prompts (storyboard_id, frame_type, prompt, description, layout, created_at, updated_at)
          VALUES (?, ?, ?, ?, ?, ?, ?)
        `);
        parsed.shots.forEach((shot) => {
          insertFramePrompt.run(storyboardId, 'shot', buildShotPrompt(shot), shot.visualDesc, `镜头${shot.shotNo}`, now, now);
        });

        log.info('Imported storyboard', {
          videoId: parsed.videoId,
          duration: finalDuration,
          shots: parsed.shots.length,
        });

        imported++;
      } catch (err) {
        log.error(`Error importing block ${idx + 1}`, { error: err.message });
        failed++;
        result.errors.push(`第 ${idx + 1} 个分镜导入失败：${err.message}`);
      }
    });

    result.imported = imported;
    result.failed = failed;
    result.success = imported > 0;
  });

  try {
    tx(storyboardBlocks);
  } catch (err) {
    log.error('Import storyboards transaction failed', { error: err.message });
    result.errors.push(`导入过程错误：${err.message}`);
  }

  return result;
}

/**
 * 构建镜头提示词
 */
function buildShotPrompt(shot) {
  const parts = [];
  if (shot.shotType) parts.push(`景别：${shot.shotType}`);
  if (shot.cameraPos) parts.push(`机位：${shot.cameraPos}`);
  if (shot.cameraMove) parts.push(`运镜：${shot.cameraMove}`);
  if (shot.visualDesc) parts.push(`画面：${shot.visualDesc}`);
  if (shot.remarks) parts.push(`备注：${shot.remarks}`);
  return parts.join('\n');
}

module.exports = {
  parseStoryboardBlock,
  parseShotsFromBlock,
  extractCharacters,
  extractCameraInfo,
  extractVisualDescription,
  extractRemarks,
  importStoryboardsFromExcel,
  buildShotPrompt,
};
