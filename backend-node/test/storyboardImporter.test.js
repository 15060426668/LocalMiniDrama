/**
 * 分镜导入功能测试（Node.js 内置 test runner）
 */
const { test } = require('node:test');
const assert = require('node:assert');
const storyboardImporter = require('../src/services/storyboardImporter');

const BLOCK_1 = `====================【视频编号01-01】====================
总时长：13.6s｜场景：SC01中和宫庭院大树下｜人物：林君雪·浅朱庭院宫装、丹珍、巧心、谷雨

【场景与连续状态】白日近黄昏，中和宫庭院大树下已有一个浅坑；林君雪蹲在坑边持小铲，脸上沾土，丹珍、巧心、谷雨围在她身边。
【光线】LG01庭院斜阳：斜阳5200K、强度34%；树荫环境光6200K、强度18%；泥土与酒坛反光3600K、强度14%。
【本编号场景光影锁】先交代浅坑、酒坛和皇后亲自挖土，再以支脸嘟囔表现体力不支；三名宫女始终围在树下。
【出场人物】林君雪·浅朱庭院宫装、丹珍、巧心、谷雨。

镜头01（3.4s）树下四人全景，石径方向高机位轻俯拍，缓慢推近
画面描述（大白话）：←承上，【大树下浅坑只挖开薄薄一层，酒坛等在旁边；林君雪蹲地握着小铲，丹珍、巧心、谷雨围成半圈】。
备注：（无台词）

镜头02（6.4s）林君雪中近景，浅坑侧方平视，静态浅焦
画面描述（大白话）：【林君雪用一只手支着脸，小铲无力垂在另一只手里；她看着迟迟挖不深的坑，带着鼻尖泥点小声嘟囔】。
备注：林君雪（台词01）：太累了。

镜头03（3.8s）丹珍动作近景，林君雪肩后侧拍，缓慢横移
画面描述（大白话）：【丹珍忍笑递出帕子，巧心已经蹲下查看林君雪脸上的土；谷雨扶稳坑边酒坛】。
备注：（无台词）`;

const BLOCK_2 = `====================【视频编号02-02】====================
总时长：13.8s｜场景：SC01中和宫庭院大树下｜人物：丹珍、林君雪·浅朱庭院宫装、巧心、谷雨

【场景与连续状态】丹珍将帕子递到林君雪面前，巧心蹲在她身侧，谷雨扶住酒坛；林君雪仍握着小铲不肯起身。
【光线】锁定LG01庭院斜阳。
【本编号场景光影锁】丹珍笑劝、巧心擦脸并接活、林君雪拒绝三步连续；不让宫女真正拿走小铲。
【出场人物】丹珍、林君雪·浅朱庭院宫装、巧心、谷雨。

镜头01（5.4s）丹珍双人近景，林君雪肩后平视，缓慢推近
画面描述（大白话）：←承上视频编号01，【丹珍把帕子送到林君雪手边，笑着指向她脸上泥点】。
备注：丹珍（台词02）：娘娘，都说了让奴婢们来。

镜头02（2.6s）巧心动作近景，树根侧方低机位，静态浅焦
画面描述（大白话）：【巧心接过帕子替林君雪擦脸，另一只手伸向小铲】。
备注：巧心（台词03）：您歇着，奴婢们挖。

镜头03（5.8s）林君雪四人中景，酒坛方向三分之四侧拍，快速横移
画面描述（大白话）：【林君雪立即摇头，把小铲收回怀中】。
备注：林君雪（台词04）：不行。这是本宫的诚意，必须自己挖。`;

test('解析单个分镜块 - 视频编号/场景/人物', () => {
  const parsed = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  assert.strictEqual(parsed.success, true, '解析应成功');
  assert.strictEqual(parsed.videoId, '01-01', '视频编号应为 01-01');
  assert.strictEqual(parsed.scene, 'SC01中和宫庭院大树下', '场景应正确提取');
  assert.deepStrictEqual(
    parsed.characters,
    ['林君雪·浅朱庭院宫装', '丹珍', '巧心', '谷雨'],
    '人物列表应正确提取'
  );
});

test('解析镜头 - 数量与时长', () => {
  const parsed = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  assert.strictEqual(parsed.shots.length, 3, '应解析出 3 个镜头');
  assert.strictEqual(parsed.shots[0].durationSec, 3.4);
  assert.strictEqual(parsed.shots[1].durationSec, 6.4);
  assert.strictEqual(parsed.shots[2].durationSec, 3.8);
});

test('总时长 = 镜头秒数之和取整 (13.6 -> 14)', () => {
  const parsed = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  const sum = parsed.shots.reduce((a, s) => a + s.durationSec, 0);
  assert.ok(Math.abs(sum - 13.6) < 0.001, `秒数之和应约为 13.6，实际 ${sum}`);
  assert.strictEqual(Math.round(sum), 14, '取整后应为 14');
});

test('运镜信息提取', () => {
  const info = storyboardImporter.extractCameraInfo('树下四人全景，石径方向高机位轻俯拍，缓慢推近');
  assert.strictEqual(info.shotType, '全景');
  assert.strictEqual(info.cameraPos, '高机位');
  assert.strictEqual(info.cameraMove, '缓慢推近');
});

test('画面描述与备注提取', () => {
  const parsed = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  assert.ok(parsed.shots[0].visualDesc.includes('大树下浅坑'), '画面描述应提取正确');
  assert.ok(parsed.shots[1].remarks.includes('台词'), '第 2 镜头备注应含台词');
});

test('镜头提示词构建', () => {
  const parsed = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  const prompt = storyboardImporter.buildShotPrompt(parsed.shots[0]);
  assert.ok(prompt.includes('景别：全景'));
  assert.ok(prompt.includes('画面：'));
});

test('批量解析两个分镜块', () => {
  const p1 = storyboardImporter.parseStoryboardBlock(BLOCK_1);
  const p2 = storyboardImporter.parseStoryboardBlock(BLOCK_2);
  assert.strictEqual(p1.success, true);
  assert.strictEqual(p2.success, true);
  assert.strictEqual(p2.videoId, '02-02');
  const sum2 = p2.shots.reduce((a, s) => a + s.durationSec, 0);
  assert.strictEqual(Math.round(sum2), 14, '第二块 5.4+2.6+5.8=13.8 -> 14');
});
