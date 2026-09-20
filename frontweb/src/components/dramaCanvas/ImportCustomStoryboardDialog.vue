<template>
  <el-dialog
    v-model="visible"
    title="导入自定义分镜"
    width="800px"
    :before-close="handleClose"
  >
    <div class="import-custom-storyboard">
      <el-alert
        title="导入说明"
        type="info"
        :closable="false"
        show-icon
        class="mb-3"
      >
        <template #default>
          <p>请粘贴您的自定义分镜提示词文本，系统将自动解析并导入到当前剧集。</p>
          <p class="mt-2">格式要求：</p>
          <ul>
            <li>每个视频块以 <code>==========【视频编号X】==========</code> 开头</li>
            <li>包含总时长、场景、人物信息</li>
            <li>包含场景与连续状态、光线等描述</li>
            <li>包含多个镜头的详细描述</li>
          </ul>
        </template>
      </el-alert>

      <el-form label-position="top">
        <el-form-item label="自定义分镜文本">
          <el-input
            v-model="importText"
            type="textarea"
            :rows="12"
            placeholder="请在此粘贴您的自定义分镜提示词..."
            @input="handleTextInput"
          />
        </el-form-item>

        <el-form-item v-if="previewResult" label="解析预览">
          <div class="preview-container">
            <el-alert
              v-if="previewResult.success"
              type="success"
              :closable="false"
              show-icon
            >
              <template #title>
                成功解析到 {{ previewResult.count }} 条分镜
              </template>
            </el-alert>
            <el-alert
              v-else
              type="error"
              :closable="false"
              show-icon
            >
              <template #title>
                解析失败：{{ previewResult.error }}
              </template>
            </el-alert>

            <div v-if="previewResult.success && previewResult.storyboards" class="preview-list">
              <el-table :data="previewResult.storyboards" border size="small" max-height="300">
                <el-table-column prop="number" label="编号" width="60" />
                <el-table-column prop="title" label="标题" width="100" />
                <el-table-column prop="duration" label="时长(s)" width="80" />
                <el-table-column prop="characters" label="角色数" width="80" />
                <el-table-column prop="scene" label="场景" />
                <el-table-column prop="shotType" label="景别" width="80" />
                <el-table-column prop="movement" label="运镜" width="100" />
              </el-table>
            </div>
          </div>
        </el-form-item>
      </el-form>
    </div>

    <template #footer>
      <el-button @click="handleClose">取消</el-button>
      <el-button
        type="primary"
        :loading="importing"
        :disabled="!canImport"
        @click="handleImport"
      >
        确认导入
      </el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { ElMessage } from 'element-plus'
import { previewParseResult } from '@/utils/customStoryboardParser'
import { storyboardsAPI } from '@/api/storyboards'

const props = defineProps({
  episodeId: {
    type: Number,
    required: true
  }
})

const emit = defineEmits(['imported', 'close'])

const visible = ref(false)
const importText = ref('')
const previewResult = ref(null)
const importing = ref(false)

const canImport = computed(() => {
  return importText.value.trim() && 
         previewResult.value?.success && 
         previewResult.value.count > 0
})

let previewTimer = null

function handleTextInput() {
  if (previewTimer) {
    clearTimeout(previewTimer)
  }
  
  previewTimer = setTimeout(() => {
    if (importText.value.trim()) {
      try {
        previewResult.value = previewParseResult(importText.value, {
          episodeId: props.episodeId
        })
      } catch (e) {
        previewResult.value = {
          success: false,
          error: e.message
        }
      }
    } else {
      previewResult.value = null
    }
  }, 500)
}

async function handleImport() {
  if (!canImport.value) {
    ElMessage.warning('请先输入有效的分镜文本')
    return
  }

  importing.value = true
  
  try {
    const response = await storyboardsAPI.importCustomStoryboards(
      props.episodeId,
      importText.value
    )
    
    ElMessage.success(response.message || `成功导入 ${response.count} 条分镜`)
    emit('imported', response)
    handleClose()
  } catch (error) {
    ElMessage.error(error.message || '导入失败')
  } finally {
    importing.value = false
  }
}

function handleClose() {
  visible.value = false
  importText.value = ''
  previewResult.value = null
  emit('close')
}

function open() {
  visible.value = true
}

defineExpose({
  open
})
</script>

<style scoped>
.import-custom-storyboard {
  padding: 0;
}

.mb-3 {
  margin-bottom: 1rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.preview-container {
  margin-top: 1rem;
}

.preview-list {
  margin-top: 1rem;
}

ul {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

li {
  margin: 0.25rem 0;
}

code {
  background: #f5f5f5;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
}
</style>