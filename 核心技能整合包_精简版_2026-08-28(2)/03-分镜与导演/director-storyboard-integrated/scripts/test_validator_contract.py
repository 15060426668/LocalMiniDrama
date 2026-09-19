#!/usr/bin/env python3
"""Focused unit tests for the v6 storyboard/SD pipeline contract."""

from __future__ import annotations

import json
import unittest

from validate_storyboard_sd import (
    DEFAULT_CONTRACT,
    split_a_segments,
    validate_sd,
    validate_source_mapping,
    validate_storyboard,
)


class ValidatorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = json.loads(DEFAULT_CONTRACT.read_text(encoding="utf-8"))

    def test_contract_is_v6_plain_text_only(self) -> None:
        self.assertEqual(self.contract["contract_version"], "6.0")
        output = self.contract["sd_output_architecture"]
        self.assertEqual(output["user_facing_format"], "plain_text")
        self.assertEqual(output["json_usage_scope"], "internal_validation_only")
        self.assertTrue(output["user_facing_json_forbidden"])
        self.assertNotIn("seedance_json", self.contract["sd_output_modes"])
        self.assertNotIn("seedance_json_schema", self.contract)

    def test_pipeline_authority_is_layered(self) -> None:
        authority = self.contract["pipeline_authority"]
        self.assertEqual(
            authority["chain"],
            [
                "story-framework",
                "script-writing",
                "script-roundtable",
                "dialogue-doctor",
                "director-storyboard-integrated",
                "animation-suspense-performance",
                "dream-suspense-sd",
            ],
        )
        self.assertTrue(authority["downstream_may_not_rewrite_upstream"])
        self.assertTrue(authority["approved_storyboard_becomes_sole_sd_source"])
        self.assertTrue(self.contract["story_readiness_gate"]["deletion_must_cause_loss"])
        self.assertTrue(self.contract["dialogue_logic_gate"]["approved_text_mutation_forbidden"])

    def test_a_headers_ignore_inline_time_ranges(self) -> None:
        text = """第0-8秒｜源镜头1
画面内容：0-3秒奔跑，3-5秒减速，5-8秒开门。
第8-15秒｜源镜头2
画面内容：8-12秒进入，12-15秒回望。
"""
        self.assertEqual([item[0] for item in split_a_segments(text)], [(0, 8), (8, 15)])

    def test_multi_reference_storyboard_policy(self) -> None:
        policy = self.contract["counterpart_workflow"]
        self.assertEqual(policy["candidate_count_range"], [0, 6])
        self.assertFalse(policy["candidate_count_is_quota"])
        self.assertTrue(policy["return_only_storyboard_relevant_references"])
        self.assertFalse(policy["counterpart_binding_required"])
        self.assertTrue(policy["multiple_film_references_per_scheme_allowed"])
        self.assertTrue(policy["cross_film_director_synthesis_allowed"])
        self.assertTrue(policy["approved_storyboard_becomes_sole_sd_source"])
        self.assertFalse(policy["film_metadata_retained_in_sd_checksum"])

    def test_phase_and_reference_mechanism_policy(self) -> None:
        phase = self.contract["phase_advancement"]
        self.assertTrue(phase["one_user_visible_phase_per_turn"])
        self.assertTrue(phase["advance_requires_explicit_user_command"])
        self.assertTrue(phase["pipeline_description_is_not_a_request_to_output_all_phases"])
        self.assertIn("story_readiness", self.contract["phase_contract"])
        self.assertIn("animation_performance", self.contract["phase_contract"])
        self.assertIn("approval_lock", self.contract["phase_contract"])

    def test_long_sequence_segmentation_is_adaptive(self) -> None:
        policy = self.contract["counterpart_workflow"]
        self.assertEqual(policy["long_sequence_segment_duration_seconds"], [4, 30])
        timing = self.contract["timing"]
        self.assertEqual(timing["sd_segment_max_seconds"], 30)
        self.assertEqual(timing["animation_internal_beat_duration_seconds"], [2, 4])
        self.assertEqual(timing["animation_midpoint_refresh_window_seconds"], [12, 18])
        self.assertTrue(timing["keep_16_30_animation_in_one_prompt_by_default"])
        self.assertTrue(policy["single_segment_when_requested_total_is_within_limit"])

    def test_total_prompt_duration_30_is_allowed(self) -> None:
        text = """【A区块·模型执行词】
第0-15秒｜源镜头1
第15-30秒｜源镜头2
"""
        findings = validate_sd(text, self.contract)
        self.assertFalse(any("超过30秒上限" in item.message for item in findings))

    def test_total_prompt_duration_over_30_is_rejected(self) -> None:
        text = """【A区块·模型执行词】
第0-15秒｜源镜头1
第15-31秒｜源镜头2
"""
        findings = validate_sd(text, self.contract)
        self.assertTrue(any("A区块总时长为31秒" in item.message for item in findings))

    def test_animation_v6_schema_is_five_fields(self) -> None:
        schema = self.contract["sd_animation_a_fields"]
        self.assertEqual(schema["default_schema"], "animation_text_v6")
        self.assertEqual(
            schema["required"],
            [
                "镜头与构图",
                "主体动作与表演",
                "关系/物件/环境反馈",
                "声光与转场触发",
                "尾帧与连续性",
            ],
        )
        self.assertEqual(self.contract["sd_a_fields"], schema["required"])
        self.assertEqual(
            self.contract["sd_a_field_schemas"]["animation_text_v6"]["status"],
            "active_user_output",
        )
        self.assertEqual(
            self.contract["sd_a_field_schemas"]["execution_expanded"]["status"],
            "compatibility_input_only",
        )
        self.assertEqual(
            self.contract["sd_a_field_schemas"]["legacy"]["status"],
            "compatibility_input_only",
        )

    def test_animation_v6_action_chain_passes(self) -> None:
        text = """【BASE LOCK】
媒介与身份：东方幻想厚涂二维动画，人物身份稳定。
空间与方向：男主从画面左侧冲向右侧，右手持断剑。
【A区块·模型执行词】
第0-3秒｜源镜头A1
镜头与构图：低机位跟拍男主从左向右冲锋，摄影机沿断剑抬升并落到右肩后方。
主体动作与表演：男主先用左脚压住积雪，视线锁定前方长枪，呼吸骤停；重心压低后右肩带动肘腕由下向上发力，断剑沿枪杆加速上挑，在接触峰值撞开枪锋；反作用使右腕下沉、胸口前倾，他借左脚支点继续跨步，右脚越过失衡敌人后落地站稳，视线重新锁回画面右侧。
关系/物件/环境反馈：枪杆受击上弹，敌人上身先后仰、脚底晚一拍滑动，断剑震颤，雪块和衣摆延迟甩向画面左后方。
声光与转场触发：画面右前近距离金属撞击声先响，触发男主压肩与摄影机抬升；接触闪现短促冷白粗笔触，敌人黑衣扫过镜头形成连续遮挡，撞击尾音延续到落雪声。
尾帧与连续性：男主右脚落地、左脚继续支撑，右手断剑下沉后回正，视线朝右；下一拍从再次蹬地开始。
"""
        errors = [item for item in validate_sd(text, self.contract) if item.level == "ERROR"]
        self.assertFalse(errors)

    def test_animation_v6_summary_action_is_rejected(self) -> None:
        text = """【BASE LOCK】
媒介与身份：二维动画。
【A区块·模型执行词】
第0-3秒｜源镜头A1
镜头与构图：低机位跟随男主向右移动。
主体动作与表演：男主冲过去挥剑击倒敌人，然后继续向前跑。
关系/物件/环境反馈：敌人倒地，积雪飞起。
声光与转场触发：画面右前撞击声触发镜头抬升，黑衣遮挡后露出道路。
尾帧与连续性：男主位于画面右侧，右手持断剑，下一拍继续奔跑。
"""
        findings = validate_sd(text, self.contract)
        self.assertTrue(any(item.level == "ERROR" and "主体动作与表演" in item.message for item in findings))

    def test_live_action_five_field_prompt_uses_live_action_detail_gate(self) -> None:
        text = """【BASE LOCK】
媒介与身份：真人数字电影，同一成年女性。
【A区块·模型执行词】
第0-4秒｜源镜头1
镜头与构图：50mm门侧中景，摄影机固定在门框左侧。
主体动作与表演：她抬手靠近门把，听见响声后停住。
关系/物件/环境反馈：钥匙碰门板，衣摆晚半拍落稳。
声光与转场触发：画面右侧近距离锁舌声触发她抬眼，尾音延续到下一拍。
尾帧与连续性：她指尖停在门把前三厘米，视线朝右。
"""
        errors = [item for item in validate_sd(text, self.contract) if item.level == "ERROR"]
        self.assertFalse(errors)

    def test_user_facing_json_is_rejected(self) -> None:
        text = '{"estimated_duration":"30s","performance_timeline":[]}'
        findings = validate_sd(text, self.contract)
        self.assertTrue(any("禁止JSON载荷" in item.message for item in findings))

    def test_positive_language_scan_preserves_approved_dialogue(self) -> None:
        text = """【A区块·模型执行词】
第0-4秒｜源镜头A1
声光与转场触发：角色说：“这锅不能用了。”尾音触发听者抬眼。
"""
        findings = validate_sd(text, self.contract)
        self.assertFalse(any("非正向表达" in item.message for item in findings))

    def test_negative_prompt_instruction_is_rejected(self) -> None:
        text = """【A区块·模型执行词】
第0-4秒｜源镜头A1
镜头与构图：摄影机不切反打，保持双人中景。
"""
        findings = validate_sd(text, self.contract)
        self.assertTrue(any("非正向表达" in item.message for item in findings))

    def test_multiple_base_locks_are_rejected(self) -> None:
        text = """【BASE LOCK】
媒介：动画。
【BASE LOCK】
媒介：动画。
【A区块·模型执行词】
第0-4秒｜源镜头1
"""
        findings = validate_sd(text, self.contract)
        self.assertTrue(any("只能有一个" in item.message for item in findings))

    def test_e_must_be_separated_from_model_payload(self) -> None:
        text = """【BASE LOCK】
媒介：动画。
【A区块·模型执行词】
第0-4秒｜源镜头1
镜头与构图：固定中景。
主体动作与表演：男人先抬眼，再用手掌撑床坐起，落在稳定坐姿。
关系/物件/环境反馈：床垫压低，床单向外展开。
声光与转场触发：右后方近距离呼吸声触发他回头，尾音延续到剪点。
尾帧与连续性：男人保持坐姿并看向右侧。
【E区块·审核索引】
| 时间 |
|---|
| 0-4秒 |
"""
        findings = validate_sd(text, self.contract)
        self.assertTrue(any("制作审核附件" in item.message for item in findings))

    def test_alphanumeric_source_id_and_strict_anchor_coverage(self) -> None:
        source = """| 镜头 | 时长 | 景别/焦段 | 构图画面 | 机位与运镜 | 光影/色彩 | SD承接锚点 |
|---|---|---|---|---|---|---|
| 1A | 4秒 | 中景 | 门在左侧 | 横移 | 冷光 | 门把位置、手部高度 |
"""
        complete = """【A区块·模型执行词】
第0-4秒｜源镜头1A
SD承接锚点：门把位置、手部高度。
"""
        incomplete = """【A区块·模型执行词】
第0-4秒｜源镜头1A
SD承接锚点：门把位置。
"""
        self.assertFalse(validate_source_mapping(source, complete, self.contract, True))
        findings = validate_source_mapping(source, incomplete, self.contract, True)
        self.assertTrue(any(item.level == "ERROR" and "要求至少100%" in item.message for item in findings))

    def test_animation_storyboard_and_source_mapping_pass(self) -> None:
        source = """【动画正式分镜】
| 镜号与整秒时间 | 戏剧变化 | 镜头与构图 | 主体与关系表演 | 物件/环境/NPC | 动画表达 | 声音与台词 | 转场与尾帧 |
|---|---|---|---|---|---|---|---|
| A1｜0-4秒 | 小师妹误解欢迎仪式 | 固定中景后轻推，主体朝右 | 她抬眼并把糖人举高，大师兄迟半拍收账本 | 门帘继续摆，桌边茶杯轻震 | 现实法则，表情保持克制 | 右侧门响触发抬眼，台词后留停顿 | 尾帧她举着糖人，大师兄看向她 |
"""
        storyboard_errors = [
            item for item in validate_storyboard(source, self.contract, False) if item.level == "ERROR"
        ]
        self.assertFalse(storyboard_errors)
        sd = """【BASE LOCK】
媒介：二维动画。
【A区块·模型执行词】
第0-4秒｜源镜头A1
镜头与构图：固定中景后轻推。
主体动作与表演：她先抬眼，再把糖人举高，大师兄迟半拍收起账本。
关系/物件/环境反馈：门帘继续摆，桌边茶杯轻震。
声光与转场触发：右侧门响触发抬眼，台词尾音后保留停顿。
尾帧与连续性：她举着糖人，大师兄看向她。
"""
        self.assertFalse(validate_source_mapping(source, sd, self.contract, True))


if __name__ == "__main__":
    unittest.main()
