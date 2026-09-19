# Local Routing Addendum

把本技能加入现有本地调用索引时，保持一条短入口即可：

```text
2D国风PV：2d-guofeng-pv-workflow
-> video-story-analysis（已有成片/参考视频）或 scene-asset-decomposition（场景图/资产板）
-> director-storyboard-integrated
-> animation-suspense-performance
-> dream-suspense-sd
```

`video-shotcraft` 位于外部参考层：读取其 `references/shots/`、`sequences/`、`aesthetic-rules.md` 和 `sound-design.md`，只迁移运动机制、帧预算、声音因果和 QA 规则。不要让它成为默认入口，也不要把它的产品模板当成江湖美术方向。

如果旧索引暂时无法编辑，当前技能的 `SKILL.md` 和本页仍是完整路由事实；在下次能正常写入索引时只需补上上面两行，不需要重新整理技能正文。
