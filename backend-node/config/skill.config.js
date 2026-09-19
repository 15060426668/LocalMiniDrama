/**
 * Skill 配置文件
 * 
 * 这里定义：
 * 1. scene_key 到 skill 的映射
 * 2. 每个 skill 的时长策略
 * 3. 分镜时长的默认值
 */

// Scene Key 到 Skill 的映射
const SCENE_TO_SKILL_MAP = {
  // 故事生成
  story_generation: null,
  
  // 角色/道具/场景提取
  role_extraction: 'gpt-image-prompt-field-manual',
  character_extraction: 'gpt-image-prompt-field-manual',
  identity_anchors: 'gpt-image-prompt-field-manual',
  prop_extraction: 'gpt-image-prompt-field-manual',
  scene_extraction: 'gpt-image-prompt-field-manual',
  
  // 分镜生成
  storyboard_extraction: 'director-storyboard-integrated',
  storyboard_system: 'director-storyboard-integrated',
  storyboard_universal: 'director-storyboard-integrated',
  
  // 图像提示词
  first_frame_prompt: 'mj-cinematic-image-prompt',
  key_frame_prompt: 'mj-cinematic-image-prompt',
  last_frame_prompt: 'mj-cinematic-image-prompt',
  panel_prompt: 'mj-cinematic-image-prompt',
  action_prompt: 'mj-cinematic-image-prompt',
  
  // 图像润色
  image_polish: 'qidu-aigc-prompt-atelier',
  role_image_polish: 'qidu-aigc-prompt-atelier',
  prop_image_polish: 'qidu-aigc-prompt-atelier',
  
  // 视频提示词
  video_prompt_generation: 'video-prompt-workbench',
  video_prompt_sd: 'dream-suspense-sd',
  
  // 小说导入
  novel_import: null,
};

// 分镜时长策略配置
const STORYBOARD_DURATION_CONFIG = {
  // 是否允许 AI 自主决定时长（不再使用固定时长覆盖）
  aiDecidedDuration: true,
  
  // 时长范围限制（秒）
  minDuration: 1,
  maxDuration: 120,
  
  // 默认时长（当 AI 未返回时）
  defaultDuration: 5,
  
  // Skill 指导的时长范围（仅供参考，不强制）
  skillGuidance: {
    // 内部动作拍通常为 2-4 秒
    actionBeat: { min: 2, max: 4 },
    // 按动作完成、台词停顿、信息改变、遮挡或镜头落点划分
    description: 'Set duration dynamically based on content: typically 2-4s per action beat, dialogue pause, information change, occlusion, or camera landing point',
  },
};

module.exports = {
  SCENE_TO_SKILL_MAP,
  STORYBOARD_DURATION_CONFIG,
};