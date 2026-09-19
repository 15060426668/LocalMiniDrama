/**
 * 核心技能包注册与服务调用层
 * Loads and invokes skills from 核心技能整合包_精简版_2026-08-28(2)/
 * 
 * 主要功能：
 * 1. 扫描并加载所有 23 个 skill 的定义
 * 2. 提供 skill → prompt template 的映射关系
 * 3. 在 LLM 调用前注入 skill 规则约束
 */

const fs = require('fs');
const path = require('path');

class SkillRegistry {
  constructor() {
    // Skill package fixed path in project root
    this.skillPackagePath = path.join(__dirname, '../../核心技能整合包_精简版_2026-08-28(2)');
    this.skills = new Map();
    this.loaded = false;
    this.promptTemplateMappings = null;
  }

  /**
   * 初始化：扫描并加载所有 skill
   */
  async initialize() {
    if (this.loaded) return true;

    try {
      console.log(`[SkillRegistry] Starting load from ${this.skillPackagePath}`);
      
      const categories = await this._scanCategories();
      console.log(`[SkillRegistry] Found ${categories.length} categories:`, categories);

      for (const cat of categories) {
        const catPath = path.join(this.skillPackagePath, cat);
        const skillsInCategory = await this._scanCategory(catPath, cat);
        
        for (const skill of skillsInCategory) {
          this.skills.set(skill.id, skill);
          console.log(`  ✓ Loaded skill: ${skill.id} (${skill.name})`);
        }
      }

      this._buildPromptTemplateMappings();
      this.loaded = true;
      
      console.log(`[SkillRegistry] Successfully loaded ${this.skills.size} skills`);
      return true;
    } catch (error) {
      console.error('[SkillRegistry] Initialization failed:', error);
      throw error;
    }
  }

  /**
   * 扫描所有分类目录
   */
  async _scanCategories() {
    const dirs = [];
    
    try {
      const entries = await fs.promises.readdir(this.skillPackagePath, { withFileTypes: true });
      for (const entry of entries) {
        if (entry.isDirectory()) {
          // Only include numbered categories like "01-图像生成", "02-视频生成" etc.
          if (/^\d+/.test(entry.name)) {
            dirs.push(entry.name);
          }
        }
      }
    } catch (err) {
      console.warn(`[SkillRegistry] Could not read skill package path: ${err.message}`);
      return [];
    }
    
    return dirs.sort(); // Sort by number order
  }

  /**
   * 扫描单个分类下的所有 skill
   */
  async _scanCategory(categoryPath, categoryName) {
    const skills = [];
    
    try {
      const entries = await fs.promises.readdir(categoryPath, { withFileTypes: true });
      
      for (const entry of entries) {
        if (entry.isDirectory()) {
          const skillId = entry.name;
          
          // Skip non-SKILL.md directories
          const skillMdPath = path.join(categoryPath, skillId, 'SKILL.md');
          if (!fs.existsSync(skillMdPath)) continue;
          
          // Read SKILL.md for metadata extraction
          let skillName = skillId;
          let rules = '';
          let examples = '';
          
          try {
            const content = await fs.promises.readFile(skillMdPath, 'utf-8');
            
            // Extract name from first heading or beginning
            const headingMatch = content.match(/^#\s+(.+)$/m);
            if (headingMatch) {
              skillName = headingMatch[1].trim();
            }
            
            // Extract rules section if exists
            const rulesMatch = content.match(/##\s*规则\s*\n([\s\S]*?)(?:##|\Z)/i);
            if (rulesMatch) {
              rules = rulesMatch[1].trim();
            }
            
            // Extract examples if exists
            const examplesMatch = content.match(/##\s*示例\s*\n([\s\S]*?)(?:##|\Z)/i);
            if (examplesMatch) {
              examples = examplesMatch[1].trim();
            }
          } catch (readErr) {
            console.warn(`[SkillRegistry] Failed to read SKILL.md for ${skillId}:`, readErr.message);
          }
          
          skills.push({
            id: skillId,
            name: skillName,
            category: categoryName,
            path: path.join(categoryPath, skillId),
            rules,
            examples,
            version: '1.0', // Can be extracted from SKILL.md header if needed
            execute: this._createExecutor(skillId, categoryPath)
          });
        }
      }
    } catch (err) {
      console.warn(`[SkillRegistry] Could not scan category ${categoryName}:`, err.message);
    }
    
    return skills;
  }

  /**
   * 为 skill 创建执行器（placeholder - will be implemented based on skill type）
   */
  _createExecutor(skillId, categoryPath) {
    return async (context) => {
      // Default executor returns rule-based enhancement
      const skill = this.skills.get(skillId);
      if (!skill) {
        throw new Error(`Skill ${skillId} not found`);
      }
      
      // Return enhanced rules + examples
      return {
        skillId,
        rules: skill.rules || '',
        examples: skill.examples || '',
        context,
        // Additional logic can be added per skill type later
      };
    };
  }

  /**
   * 构建 prompt template → skill 映射
   */
  _buildPromptTemplateMappings() {
    // Mapping table: prompt template function name → relevant skill IDs
    this.promptTemplateMappings = {
      // Storyboard generation & polishing
      'getStoryboardSystemPrompt': ['director-storyboard-integrated'],
      'getUniversalOmniSegmentPrompt': ['dream-suspense-sd'],
      'getUniversalOmniPolishPrompt': ['dream-suspense-sd', 'director-storyboard-integrated'],
      
      // Image prompts
      'getImagePolishPrompt': ['mj-cinematic-image-prompt', 'psychological-anime-imagegen', 'qidu-aigc-prompt-atelier'],
      'getFirstFramePrompt': ['live-action-spatial-previs'],
      'getLastFramePrompt': ['live-action-spatial-previs'],
      'getKeyFramePrompt': ['animation-suspense-performance'],
      
      // Scene prompts
      'getScenePolishPromptSingle': ['scene-asset-decomposition'],
      'getScenePolishPrompt': ['scene-asset-decomposition'],
      'getSceneGenerateImagePrompt': ['scene-asset-decomposition'],
      'getSceneGenerateSingleImagePrompt': ['scene-asset-decomposition'],
      
      // Character prompts
      'getRolePolishPrompt': ['mj-takopi-2d-house-style'],
      'getRoleGenerateImagePrompt': ['mj-takopi-2d-house-style'],
      
      // Prop prompts
      'getPropPolishPrompt': ['scene-asset-decomposition'],
      
      // Continuity tracking
      'getContinuitySnapshotPrompt': ['director-storyboard-training-maintainer'],
      'getRegenerateLayoutDescriptionPrompt': ['live-action-spatial-previs'],
    };
    
    console.log('[SkillRegistry] Built prompt template mappings:', Object.keys(this.promptTemplateMappings).length, 'templates');
  }

  /**
   * 获取指定 prompt template 对应的 skill IDs
   */
  getMappingForPromptTemplate(templateName) {
    if (!this.loaded) {
      throw new Error('SkillRegistry not initialized. Call initialize() first.');
    }
    
    return this.promptTemplateMappings[templateName] || [];
  }

  /**
   * 获取所有已加载的 skill
   */
  getAllSkills() {
    return Array.from(this.skills.values());
  }

  /**
   * 根据类型筛选 skills
   */
  getSkillsByType(type) {
    // type: 'image' | 'video' | 'storyboard' | 'script' | 'analysis'
    const typeMap = {
      'image': ['01-图像生成'],
      'video': ['02-视频生成'],
      'storyboard': ['03-分镜与导演'],
      'script': ['04-剧本与对白'],
      'analysis': ['05-分析、训练与资产'],
    };
    
    const targetCategories = typeMap[type] || [];
    return this.getAllSkills().filter(s => targetCategories.includes(s.category));
  }

  /**
   * 检查 skill 是否已加载
   */
  isLoaded() {
    return this.loaded;
  }

  /**
   * 获取 skill count
   */
  getSkillCount() {
    return this.skills.size;
  }
}

// Singleton instance
const skillRegistry = new SkillRegistry();

// Auto-initialize on import (but can be deferred if needed)
let _initPromise = null;
skillRegistry.ensureInitialized = async () => {
  if (!skillRegistry.loaded) {
    if (!_initPromise) {
      _initPromise = skillRegistry.initialize();
    }
    await _initPromise;
  }
  return skillRegistry;
};

module.exports = skillRegistry;
