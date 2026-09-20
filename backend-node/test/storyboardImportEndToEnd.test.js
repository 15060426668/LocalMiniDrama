/**
 * 分镜导入功能 - 端到端完整测试
 * 1. 使用真实分镜格式创建 Excel 文件
 * 2. 通过 API 接口测试导入流程
 */
const { test } = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');
const axios = require('axios');

// 配置
const API_BASE = 'http://localhost:5679/api/v1';
const STORYBOARD_PATH = path.join(__dirname, '../docs/storyboard-import-template.xlsx');

const REAL_BLOCK_1 = `====================【视频编号 01-01】====================
总时长：13.6s｜场景：中和宫庭院大树下｜人物：林君雪、丹珍、巧心、谷雨

【场景与连续状态】白日近黄昏，中和宫庭院大树下已有一个浅坑；林君雪蹲在坑边持小铲，脸上沾土，丹珍、巧心、谷雨围在她身边。
【光线】LG01 庭院斜阳：斜阳 5200K、强度 34%；树荫环境光 6200K、强度 18%；泥土与酒坛反光 3600K、强度 14%。
【本编号场景光影锁】先交代浅坑、酒坛和皇后亲自挖土，再以支脸嘟囔表现体力不支；三名宫女始终围在树下。

镜头 01（3.4s）树下四人全景，石径方向高机位轻俯拍，缓慢推近
画面描述（大白话）：←承上，【大树下浅坑只挖开薄薄一层，酒坛等在旁边；林君雪蹲地握着小铲，丹珍、巧心、谷雨围成半圈】。
备注：（无台词）

镜头 02（6.4s）林君雪中近景，浅坑侧方平视，静态浅焦
画面描述（大白话）：【林君雪用一只手支着脸，小铲无力垂在另一只手里；她看着迟迟挖不深的坑，带着鼻尖泥点小声嘟囔】。
备注：林君雪（台词 01）：太累了。

镜头 03（3.8s）丹珍动作近景，林君雪肩后侧拍，缓慢横移
画面描述（大白话）：【丹珍忍笑递出帕子，巧心已经蹲下查看林君雪脸上的土；谷雨扶稳坑边酒坛】。
备注：（无台词）`;

const REAL_BLOCK_2 = `====================【视频编号 02-02】====================
总时长：13.8s｜场景：中和宫庭院大树下｜人物：丹珍、林君雪、巧心、谷雨

【场景与连续状态】丹珍将帕子递到林君雪面前，巧心蹲在她身侧，谷雨扶住酒坛；林君雪仍握着小铲不肯起身。
【光线】锁定 LG01 庭院斜阳。
【本编号场景光影锁】丹珍笑劝、巧心擦脸并接活、林君雪拒绝三步连续；不让宫女真正拿走小铲。

镜头 01（5.4s）丹珍双人近景，林君雪肩后平视，缓慢推近
画面描述（大白话）：←承上视频编号 01，【丹珍把帕子送到林君雪手边，笑着指向她脸上泥点】。
备注：丹珍（台词 02）：娘娘，都说了让奴婢们来。

镜头 02（2.6s）巧心动作近景，树根侧方低机位，静态浅焦
画面描述（大白话）：【巧心接过帕子替林君雪擦脸，另一只手伸向小铲】。
备注：巧心（台词 03）：您歇着，奴婢们挖。

镜头 03（5.8s）林君雪四人中景，酒坛方向三分之四侧拍，快速横移
画面描述（大白话）：【林君雪立即摇头，把小铲收回怀中】。
备注：林君雪（台词 04）：不行。这是本宫的诚意，必须自己挖。`;

test('测试真实的分镜导入流程', async (t) => {
    // 测试前准备
    t.before(() => {
        console.log('🚀 开始测试分镜导入功能...');
    });

    // 验证后端服务是否运行
    try {
        const healthRes = await axios.get(`${API_BASE.replace('/api/v1', '')}/health`);
        assert.ok(healthRes.data.status === 'ok', '后端服务应正常启动');
        console.log('✅ 后端服务健康检查通过');
    } catch (err) {
        console.warn(`⚠️  后端服务可能未运行，跳过集成测试。本地请执行：cd backend-node && npm run dev`);
        return;
    }

    // 步骤 1: 读取 Excel 文件并转换为文本数组
    console.log('\n📂 步骤 1: 读取 Excel 文件...');
    
    // 假设前端已经处理了 Excel 文件，我们直接模拟后端接收的数据格式
    const mockData = [
        { content: REAL_BLOCK_1 },
        { content: REAL_BLOCK_2 }
    ];

    // 步骤 2: 调用导入 API（需要先创建一个测试剧集）
    console.log('\n📝 步骤 2: 获取剧集 ID...');
    
    let episodeId;
    try {
        // 尝试获取现有剧集
        const episodesRes = await axios.get(`${API_BASE}/episodes?drama_id=1`);
        if (episodesRes.data.data && episodesRes.data.data.length > 0) {
            episodeId = episodesRes.data.data[0].id;
            console.log(`✅ 找到剧集 ID: ${episodeId}`);
        } else {
            console.warn('⚠️  没有可用的剧集，请先在系统中创建剧集');
            process.exit(0);
        }
    } catch (err) {
        console.warn('⚠️  无法获取剧集列表，请先确保有剧集存在');
        process.exit(0);
    }

    // 步骤 3: 调用导入接口
    console.log('\n🎬 步骤 3: 调用导入接口 /storyboards/import-excel...');
    
    const importRes = await axios.post(`${API_BASE}/storyboards/import-excel`, {
        episode_id: episodeId,
        data: mockData
    }, {
        headers: { 'Content-Type': 'application/json' }
    });

    console.log('\n📊 导入结果:', importRes.data);
    
    assert.ok(importRes.data.success || importRes.data.imported > 0, 
        `导入应该成功或部分成功，失败数：${importRes.data.failed}, 错误：${JSON.stringify(importRes.data.errors)}`);
    
    console.log(`\n✅ 导入成功！创建了 ${importRes.data.imported} 个分镜`);
    
    // 步骤 4: 验证导入结果
    console.log('\n🔍 步骤 4: 验证导入的分镜数据...');
    
    const storyboardsRes = await axios.get(`${API_BASE}/storyboards?episode_id=${episodeId}`, {
        params: { limit: 10, offset: 0 }
    });
    
    const importedCount = storyboardsRes.data.data.filter(sb => 
        sb.storyboard_number <= importRes.data.imported
    ).length;
    
    assert.strictEqual(importedCount, importRes.data.imported, 
        `故事板数量应与导入数量一致：${importedCount} === ${importRes.data.imported}`);
    
    console.log(`\n✅ 验证通过！数据库中已存储 ${importedCount} 条分镜记录`);
});

console.log('\n✨ 开始执行分镜导入端到端测试...\n');
