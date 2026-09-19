const express = require('express');
const router = express.Router();
const skillLoader = require('../services/skillLoader');

router.get('/', (req, res) => {
  const skills = skillLoader.listAvailableSkills();
  res.json({ code: 0, data: skills });
});

router.get('/:name', (req, res) => {
  const info = skillLoader.getSkillInfo(req.params.name);
  if (!info) {
    return res.status(404).json({ code: 1, message: 'Skill not found' });
  }
  res.json({ code: 0, data: { name: info.name, frontmatter: info.frontmatter } });
});

router.get('/:name/content', (req, res) => {
  const info = skillLoader.getSkillInfo(req.params.name);
  if (!info) {
    return res.status(404).json({ code: 1, message: 'Skill not found' });
  }
  res.json({ code: 0, data: { name: info.name, content: info.content } });
});

router.get('/test/:sceneKey', (req, res) => {
  const { sceneKey } = req.params;
  const skillName = skillLoader.getSkillForScene(sceneKey);
  const skillInfo = skillName ? skillLoader.getSkillInfo(skillName) : null;
  res.json({
    code: 0,
    data: {
      sceneKey,
      hasSkill: !!skillName,
      skillName,
      skillDescription: skillInfo?.frontmatter?.description || null,
      skillLength: skillInfo?.body?.length || 0,
    },
  });
});

router.get('/mapping', (req, res) => {
  const mapping = {
    story_generation: null,
    role_extraction: 'gpt-image-prompt-field-manual',
    character_extraction: 'gpt-image-prompt-field-manual',
    identity_anchors: 'gpt-image-prompt-field-manual',
    storyboard_extraction: null,
    storyboard_system: null,
    storyboard_universal: null,
    first_frame_prompt: 'mj-cinematic-image-prompt',
    key_frame_prompt: 'mj-cinematic-image-prompt',
    last_frame_prompt: 'mj-cinematic-image-prompt',
    panel_prompt: 'mj-cinematic-image-prompt',
    action_prompt: 'mj-cinematic-image-prompt',
    image_polish: 'qidu-aigc-prompt-atelier',
    role_image_polish: 'qidu-aigc-prompt-atelier',
    video_prompt_generation: 'video-prompt-workbench',
    video_prompt_sd: 'dream-suspense-sd',
    prop_extraction: 'gpt-image-prompt-field-manual',
    prop_image_polish: 'qidu-aigc-prompt-atelier',
    scene_extraction: 'gpt-image-prompt-field-manual',
    novel_import: null,
  };
  res.json({ code: 0, data: mapping });
});

module.exports = router;