# Audio Delivery QA

用途：对真实导出的PCM WAV进行成品测量，补足 `calculate_sound_mix.py` 只能分析计划声轨、不能证明最终混音的缺口。

## Division Of Responsibility

```text
calculate_sound_mix.py = 分镜/混音计划值、声层叠加估算、峰值压力测试
analyze_audio_delivery.py = 实际WAV的响度、峰值、动态、底噪、声道与对白余量
```

计划值与实测值必须同时保存。计划声轨通过，不代表最终音频已经达到目标。

## Usage

```powershell
python scripts/analyze_audio_delivery.py <mix.wav> --profile social_balanced --output <audio-report.json>
python scripts/analyze_audio_delivery.py <mix.wav> --dialogue <dialogue-stem.wav> --profile dialogue_led --format markdown
python scripts/analyze_audio_delivery.py --self-test --strict
```

输入限制：

- PCM WAV。
- 1或2声道。
- 推荐48kHz。
- 对白stem必须与mix采样率、声道数、起点和长度对齐。

## Measured Fields

- `integrated_lufs`: 按BS.1770/R128思路进行K-weighting和门限整合的节目响度估算。
- `short_term_lufs`: 3秒窗口的短时响度范围与时间线。
- `sample_peak_dbfs`: 实际采样峰值。
- `oversampled_peak_estimate_dbfs`: 4倍FFT过采样峰值估算；用于风险检查，不能冒充认证dBTP仪表。
- `rms_dbfs` / `crest_factor_db`: 总体能量和瞬态余量。
- `noise_floor_proxy_dbfs`: 100ms窗口能量的低分位代理。
- `silence_ratio`: 低于指定门限的时间比例。
- `clipped_sample_count`: 接近数字满幅的样本数。
- `dc_offset`: 声道直流偏移。
- `stereo_correlation`: 左右声道相关性，检查反相与过宽风险。
- `stereo_balance_db`: 左右声道RMS差值，检查重心偏移。
- `dialogue_to_background_db`: 提供对齐对白stem时，估算对白相对剩余混音的能量余量。

## Acceptance Logic

- 最终响度围绕所选delivery profile判断，默认容差 `±1.5 LU`。
- 过采样峰值高于profile上限时进入限制器/峰值复查。
- clipping、明显DC偏移、极低立体声相关、对白低于背景均产生警告。
- 真实交付仍应使用专业响度表进行最终确认；本工具用于自动回归和早期发现问题。

## Sound-Picture Sync Manual Gate

音频数值通过后仍检查：

```text
接触帧 = 拟音瞬态起点
口型重音 = 台词重音
声源方位 = 画面空间与人物朝向
遮挡开合 = 高频与直达声变化
VFX移动边界 = 设计音发展边界
尾音结束 = 剪点或下一镜继承
人物可见反应 = 角色实际接收到声音之后
```

自动响度报告不能判断声音是否在正确的画面帧发生；声画同步仍需要时间码或成片人工审查。
