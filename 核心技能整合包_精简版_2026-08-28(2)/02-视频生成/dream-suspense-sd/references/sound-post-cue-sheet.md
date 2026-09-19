# Sound Post Cue Sheet

用途：把分镜和A区块中的声音设计转成交给拟音、环境声、配音、音乐和混音的执行表。视频提示词保留声画触发，后期表负责真正制作层次。数值口径、七类总线、对数叠加和交付档位以 `../../director-storyboard-integrated/references/sound-mix-metering.md` 为准。

## Cue Fields

```text
时间段：
源镜头号：
声源总线：ENV / BODY / OBJ / VOX / FX / INT / MUS
具体声源：
声源状态：画内 / 画外 / 主观 / 结构性
叙事权限：谁制造 / 谁听见 / 谁忽略 / 谁误判
屏幕方位与距离：
起音方式：硬起 / 渐入 / 预先进入 / 接触触发
包络与节奏：attack / sustain / release
频段重点：
目标电平：RMS dBFS / peak dBFS / 相对主声源dB
环境遮蔽与混响：EQ / RT60 / pre-delay / dry-wet
闪避与掩蔽：谁为谁让位 / dB / 时间
触发的可见反应：
结束方式：切断 / 衰减 / 回声 / 延续到下一镜
下一段继承：
```

## Mix Priority

一个短节拍通常只保留一个主听觉注意力。所有七类总线都要经过审查，但只启用服务当前节拍的2-5类：

```text
主声源
-> BODY/OBJ/VOX关键接触或信息
-> ENV空间底床
-> FX/INT/MUS结构层
```

关键动作发生时，背景声可降低频段或音量，为接触、呼吸、门锁、刹车、物件落地或一句重音让出位置。

## Numeric Mix Summary

每个时间段必须汇总：

```text
主声源ID：
启用总线：
逐轨RMS dBFS / peak dBFS / 相对主声源dB：
估算能量和：10*log10(sum(10^(Li/10)))
最坏同相峰值：20*log10(sum(10^(Pi/20)))
镜头目标LUFS-S：
母版档位LUFS-I / dBTP：
峰值余量与处理备注：
```

估算值只用于层级、余量与风险判断。最终 `LUFS-I` 和 `dBTP` 必须在EQ、动态、声像、混响与限制之后实测。

## Dialogue And Lip Sync

- 台词表记录实际文本、说话者、起止秒、语速档位、重音词和呼吸点。
- 画外台词仍记录声源方向、距离和人物可见反应。
- 争吵允许抢话，但同一画面只保留一个主要可读口型。
- 规则音和系统音保持关键词清楚，环境声在关键词处短暂让位。

## Handoff Format

| 时间 | 镜头 | 主声源 | 启用总线/具体声源 | 方位/距离 | RMS/Peak/相对电平 | 频段/遮挡/混响 | 闪避/掩蔽 | 镜头总线/母版 | 声画触发 | 尾音/声桥 |
|---|---|---|---|---|---|---|---|---|---|---|

结构化交接使用 `../../director-storyboard-integrated/references/sound-mix-manifest.schema.json` 对应字段，并运行：

```powershell
python scripts/calculate_sound_mix.py <sound-mix.json> --strict --format markdown
python scripts/compile_sound_cue_sheet.py <execution.md> --mix-manifest <sound-mix.json> --output <sound-sheet.md>
python scripts/analyze_audio_delivery.py <mix.wav> --dialogue <dialogue-stem.wav> --profile dialogue_led
```
