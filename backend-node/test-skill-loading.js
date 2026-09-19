/**
 * 测试 Skill 加载
 * 运行: node test-skill-loading.js
 */

const skillLoader = require('./src/services/skillLoader');
const { SCENE_TO_SKILL_MAP, STORYBOARD_DURATION_CONFIG } = require('./config/skill.config');

console.log('=== Skill 映射配置 ===');
console.log(JSON.stringify(SCENE_TO_SKILL_MAP, null, 2));

console.log('\n=== 分镜时长策略 ===');
console.log(JSON.stringify(STORYBOARD_DURATION_CONFIG, null, 2));

console.log('\n=== 测试 Skill 加载 ===');

const testScenes = [
  'storyboard_extraction',
  'role_extraction',
  'first_frame_prompt',
  'video_prompt_sd',
];

for (const scene of testScenes) {
  const skillName = skillLoader.getSkillForScene(scene);
  console.log(`\nScene: ${scene}`);
  console.log(`  Skill: ${skillName || '(none)'}`);
  
  if (skillName) {
    const info = skillLoader.getSkillInfo(skillName);
    if (info) {
      console.log(`  Description: ${info.frontmatter?.description || '(none)'}`);
      console.log(`  Body length: ${info.body?.length || 0} chars`);
      console.log(`  Has duration guidance: ${info.body?.includes('2-4秒') || info.body?.includes('2-4s') ? 'YES ✓' : 'NO ✗'}`);
    } else {
      console.log(`  ERROR: Failed to load skill info`);
    }
  }
}

console.log('\n=== 测试 buildSkillSystemPrompt ===');
const skillPrompt = skillLoader.buildSkillSystemPrompt('director-storyboard-integrated');
if (skillPrompt) {
  console.log(`Skill prompt length: ${skillPrompt.length} chars`);
  console.log(`Contains duration guidance: ${skillPrompt.includes('2-4秒') || skillPrompt.includes('2-4s') ? 'YES ✓' : 'NO ✗'}`);
  console.log('\nFirst 500 chars:');
  console.log(skillPrompt.slice(0, 500));
} else {
  console.log('ERROR: Failed to build skill system prompt');
}