const fs = require('fs');
const path = require('path');
const { SCENE_TO_SKILL_MAP } = require('../../config/skill.config');

const SKILLS_DIR = path.join(__dirname, '..', '..', 'skills');

const _skillCache = {};
const _skillPathCache = {}; // 缓存 skillName 到完整路径的映射

// 构建 skill 路径缓存
function buildSkillPathCache() {
  if (Object.keys(_skillPathCache).length > 0) return; // 已构建
  
  if (!fs.existsSync(SKILLS_DIR)) return;
  
  const items = fs.readdirSync(SKILLS_DIR, { withFileTypes: true });
  for (const group of items) {
    if (!group.isDirectory()) continue;
    const groupPath = path.join(SKILLS_DIR, group.name);
    const subItems = fs.readdirSync(groupPath, { withFileTypes: true });
    for (const sub of subItems) {
      if (!sub.isDirectory()) continue;
      const skillPath = path.join(groupPath, sub.name, 'SKILL.md');
      if (fs.existsSync(skillPath)) {
        _skillPathCache[sub.name] = skillPath;
      }
    }
  }
}

function readSkillMarkdown(skillName) {
  if (_skillCache[skillName]) return _skillCache[skillName];
  
  buildSkillPathCache();
  
  const skillPath = _skillPathCache[skillName];
  if (!skillPath || !fs.existsSync(skillPath)) return null;
  
  const content = fs.readFileSync(skillPath, 'utf-8');
  _skillCache[skillName] = content;
  return content;
}

function extractSkillFrontmatter(content) {
  if (!content) return null;
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  const meta = {};
  match[1].split('\n').forEach(line => {
    const idx = line.indexOf(':');
    if (idx > 0) {
      const key = line.slice(0, idx).trim();
      let val = line.slice(idx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      meta[key] = val;
    }
  });
  return meta;
}

function getSkillInfo(skillName) {
  const content = readSkillMarkdown(skillName);
  if (!content) return null;
  const frontmatter = extractSkillFrontmatter(content);
  const body = content.replace(/^---[\s\S]*?---\n?/, '').trim();
  return { name: skillName, frontmatter, body, content };
}

function buildSkillSystemPrompt(skillName, extraContext) {
  const info = getSkillInfo(skillName);
  if (!info) return null;
  const desc = info.frontmatter?.description || '';
  const parts = [
    `You are now operating under the "${skillName}" skill.`,
    desc ? `Skill description: ${desc}` : '',
    '',
    '=== SKILL INSTRUCTIONS (MUST FOLLOW) ===',
    info.body,
    '=== END SKILL INSTRUCTIONS ===',
    extraContext ? `\nAdditional context:\n${extraContext}` : '',
  ].filter(Boolean);
  return parts.join('\n');
}

function listAvailableSkills() {
  if (!fs.existsSync(SKILLS_DIR)) return [];
  const items = fs.readdirSync(SKILLS_DIR, { withFileTypes: true });
  const skills = [];
  for (const group of items) {
    if (!group.isDirectory()) continue;
    const groupPath = path.join(SKILLS_DIR, group.name);
    const subItems = fs.readdirSync(groupPath, { withFileTypes: true });
    for (const sub of subItems) {
      if (!sub.isDirectory()) continue;
      const skillPath = path.join(groupPath, sub.name, 'SKILL.md');
      if (fs.existsSync(skillPath)) {
        const info = getSkillInfo(sub.name);
        skills.push({
          group: group.name,
          name: sub.name,
          description: info?.frontmatter?.description || '',
        });
      }
    }
  }
  return skills;
}

function getSkillForScene(sceneKey) {
  // 使用配置文件中的映射
  return SCENE_TO_SKILL_MAP[sceneKey] || null;
}

module.exports = {
  readSkillMarkdown,
  getSkillInfo,
  buildSkillSystemPrompt,
  listAvailableSkills,
  getSkillForScene,
  SKILLS_DIR,
};