param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$Root = Split-Path -Parent $PSScriptRoot
$Validator = Join-Path $PSScriptRoot "validate_storyboard_sd.py"
$Fixtures = Join-Path $PSScriptRoot "fixtures"
$SkillsRoot = Split-Path -Parent $Root
$DreamRoot = Join-Path $SkillsRoot "dream-suspense-sd"
$AnimationRoot = Join-Path $SkillsRoot "animation-suspense-performance"
$AnimationValidator = Join-Path $AnimationRoot "scripts\validate_animation_performance.py"
$AnimationFixtures = Join-Path $AnimationRoot "scripts\fixtures"
$DirectorSkill = Join-Path $Root "SKILL.md"
$DreamSkill = Join-Path $DreamRoot "SKILL.md"
$AnimationSkill = Join-Path $AnimationRoot "SKILL.md"
$RuntimeContract = Join-Path $Root "references\runtime-contract.json"
$PipelineContract = Join-Path $Root "references\animation-production-pipeline.md"
$ModelProfiles = Join-Path $DreamRoot "references\model-output-profiles.json"
$SeedanceValidator = Join-Path $DreamRoot "scripts\validate_seedance_json.py"
$DreamFixtures = Join-Path $DreamRoot "scripts\fixtures"

foreach ($Check in @(
    @{ Path = $DirectorSkill; Terms = @('Runtime contract: `v6.0', "场景可拍闸门", "谁开口就切谁", "用户侧只交付纯文本") },
    @{ Path = $AnimationSkill; Terms = @('Runtime contract: `v6.0', "不改剧情、台词和镜头的戏剧目的", "16-30秒", "用户侧JSON") },
    @{ Path = $DreamSkill; Terms = @('Runtime contract: `v6.0', "唯一用户输出格式", "五字段A拍", "Never deliver user-facing JSON") },
    @{ Path = $PipelineContract; Terms = @("六步主链与所有权", "场景可拍闸门", "纯文本SD承接", "JSON仅可存在于内部配置") },
    @{ Path = $RuntimeContract; Terms = @('"subject_performance_detail_gate"', '"animation_formal_storyboard_fields"') },
    @{ Path = $ModelProfiles; Terms = @('"profiles"', '"default_animation_schema"') }
)) {
    foreach ($Term in $Check.Terms) {
        if (-not (Select-String -LiteralPath $Check.Path -Pattern $Term -SimpleMatch -Quiet)) {
            throw "Phase/segment contract missing: $Term in $($Check.Path)"
        }
    }
}

$RuntimeObject = Get-Content -LiteralPath $RuntimeContract -Raw -Encoding UTF8 | ConvertFrom-Json
if ($RuntimeObject.contract_version -ne "6.0" -or
    $RuntimeObject.sd_output_architecture.user_facing_format -ne "plain_text" -or
    $RuntimeObject.sd_output_architecture.json_usage_scope -ne "internal_validation_only" -or
    -not $RuntimeObject.sd_output_architecture.user_facing_json_forbidden -or
    $RuntimeObject.sd_output_architecture.animation_default_schema -ne "animation_text_v6" -or
    $RuntimeObject.timing.sd_segment_max_seconds -ne 30 -or
    -not $RuntimeObject.pipeline_authority.downstream_may_not_rewrite_upstream -or
    -not $RuntimeObject.dialogue_logic_gate.approved_text_mutation_forbidden) {
    throw "Runtime contract v6 structured values are inconsistent."
}
if ($RuntimeObject.sd_output_modes -contains "seedance_json" -or $null -ne $RuntimeObject.seedance_json_schema) {
    throw "Runtime contract still exposes user-facing Seedance JSON."
}
$ProfileObject = Get-Content -LiteralPath $ModelProfiles -Raw -Encoding UTF8 | ConvertFrom-Json
if ($ProfileObject.profile_version -ne "2.0" -or
    $ProfileObject.default_profile -ne "model_execution" -or
    $ProfileObject.user_facing_format -ne "plain_text" -or
    $ProfileObject.json_usage -ne "internal_validation_only" -or
    -not $ProfileObject.user_facing_json_forbidden -or
    $ProfileObject.default_animation_schema -ne "animation_text_v6") {
    throw "Model output profile v2 structured values are inconsistent."
}
if ($ProfileObject.profiles.PSObject.Properties.Name -contains "seedance_json") {
    throw "Model profiles still expose a Seedance JSON output profile."
}

function Invoke-ExpectedPass {
    param([string]$Name, [string]$Mode)
    if ($Mode -eq "sd") {
        & $Python $Validator (Join-Path $Fixtures $Name) --mode $Mode --source-storyboard (Join-Path $Fixtures "pass-storyboard.md") --continuity-manifest (Join-Path $Fixtures "continuity-manifest-pass.json")
    }
    else {
        & $Python $Validator (Join-Path $Fixtures $Name) --mode $Mode
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Expected PASS: $Name"
    }
}

function Invoke-ExpectedFail {
    param([string]$Name, [string]$Mode)
    if ($Mode -eq "sd") {
        & $Python $Validator (Join-Path $Fixtures $Name) --mode $Mode --source-storyboard (Join-Path $Fixtures "pass-storyboard.md")
    }
    else {
        & $Python $Validator (Join-Path $Fixtures $Name) --mode $Mode
    }
    if ($LASTEXITCODE -eq 0) {
        throw "Expected FAIL: $Name"
    }
}

Invoke-ExpectedPass "pass-storyboard.md" "storyboard"
Invoke-ExpectedFail "fail-storyboard.md" "storyboard"
Invoke-ExpectedPass "pass-sd.md" "sd"
Invoke-ExpectedFail "fail-sd.md" "sd"

& $Python $Validator (Join-Path $Fixtures "pass-sd-execution.md") --mode sd
if ($LASTEXITCODE -ne 0) {
    throw "Expected compact BASE+A model execution without E to pass."
}

& $Python (Join-Path $PSScriptRoot "test_validator_contract.py")
if ($LASTEXITCODE -ne 0) {
    throw "Validator contract unit tests failed."
}

foreach ($Case in Get-ChildItem -LiteralPath $AnimationFixtures -Filter "*.md") {
    $ExpectedPass = $Case.Name.StartsWith("pass-")
    $Profile = "standard"
    if ($Case.Name -match "mixed-reality") {
        $Profile = "mixed-reality"
    }
    elseif ($Case.Name -match "scene-") {
        $Profile = "scene"
    }
    elseif ($Case.Name -match "expressive") {
        $Profile = "expressive"
    }
    $AnimationMode = if ($Case.Name -match "handoff") { "handoff" } else { "formal" }
    & $Python $AnimationValidator $Case.FullName --mode $AnimationMode --profile $Profile | Out-Null
    $Passed = $LASTEXITCODE -eq 0
    if ($Passed -ne $ExpectedPass) {
        throw "Animation fixture result changed: $($Case.Name), expected pass=$ExpectedPass, profile=$Profile, mode=$AnimationMode"
    }
}

& $Python $Validator (Join-Path $Fixtures "pass-sd-15s-multibeat.md") --mode sd
if ($LASTEXITCODE -ne 0) {
    throw "Expected one 15-second prompt with multiple internal A beats to pass."
}

& $Python $Validator (Join-Path $Fixtures "pass-sd-30s-multibeat.md") --mode sd
if ($LASTEXITCODE -ne 0) {
    throw "Expected one 30-second prompt with sequential internal A beats to pass."
}

& $Python $Validator (Join-Path $Fixtures "pass-animation-storyboard-30s-sitcom.md") --mode storyboard
if ($LASTEXITCODE -ne 0) {
    throw "Expected the 30-second animation sitcom storyboard to pass."
}

& $Python $Validator (Join-Path $Fixtures "pass-sd-30s-animation-sitcom.md") --mode sd --source-storyboard (Join-Path $Fixtures "pass-animation-storyboard-30s-sitcom.md")
if ($LASTEXITCODE -ne 0) {
    throw "Expected the 30-second animation sitcom SD handoff to pass."
}

& $Python $Validator (Join-Path $Fixtures "fail-user-facing-json.md") --mode sd | Out-Null
if ($LASTEXITCODE -eq 0) {
    throw "Expected user-facing JSON SD output to fail."
}

& $Python $Validator (Join-Path $Fixtures "fail-sd-total-over-30.md") --mode sd | Out-Null
if ($LASTEXITCODE -eq 0) {
    throw "Expected cumulative A duration over 30 seconds to fail."
}

& $Python $SeedanceValidator (Join-Path $DreamFixtures "seedance-30s-pass.json") | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Expected 30-second Seedance JSON to pass."
}

& $Python $SeedanceValidator (Join-Path $DreamFixtures "seedance-31s-fail.json") | Out-Null
if ($LASTEXITCODE -eq 0) {
    throw "Expected 31-second Seedance JSON to fail."
}

& $Python $Validator (Join-Path $Fixtures "fail-dense-sd.md") --mode sd --strict-complexity
if ($LASTEXITCODE -eq 0) {
    throw "Expected complexity overload rejection."
}

& $Python (Join-Path $PSScriptRoot "estimate_dialogue_timing.py") --file (Join-Path $Fixtures "dialogue-sample.txt") --mode heated --available-seconds 3 --json | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Dialogue timing estimator failed."
}

$Compiled = Join-Path $env:TEMP "dream-sd-model-profile-test.txt"
& $Python (Join-Path $DreamRoot "scripts\compile_model_profile.py") (Join-Path $Fixtures "pass-sd-30s-animation-sitcom.md") --profile seedance_execution --output $Compiled
if ($LASTEXITCODE -ne 0) {
    throw "Model profile compiler failed."
}
$RequiredCompiled = @("BASE LOCK", "A区块·模型执行词", "0-4", "12-16", "27-30", "镜头与构图", "主体动作与表演", "关系/物件/环境反馈", "声光与转场触发", "尾帧与连续性")
foreach ($Term in $RequiredCompiled) {
    if (-not (Select-String -LiteralPath $Compiled -Pattern $Term -SimpleMatch -Quiet)) {
        throw "Model profile compiler lost content: $Term"
    }
}
if (Select-String -LiteralPath $Compiled -Pattern "E区块|声音后期表|自审报告|^\s*\{" -Quiet) {
    throw "Model profile compiler emitted non-model attachments or JSON."
}
& $Python $Validator $Compiled --mode sd --source-storyboard (Join-Path $Fixtures "pass-animation-storyboard-30s-sitcom.md")
if ($LASTEXITCODE -ne 0) {
    throw "Compiled 30-second animation model payload failed SD validation."
}
Remove-Item -LiteralPath $Compiled -Force

$ExecutionCompiled = Join-Path $env:TEMP "dream-sd-model-execution-test.txt"
& $Python (Join-Path $DreamRoot "scripts\compile_model_profile.py") (Join-Path $Fixtures "pass-sd-execution.md") --profile model_execution --output $ExecutionCompiled
if ($LASTEXITCODE -ne 0) {
    throw "Model-execution profile compiler failed."
}
$RequiredExecution = @("BASE LOCK", "A区块·模型执行词", "0-3", "35mm", "50mm")
foreach ($Term in $RequiredExecution) {
    if (-not (Select-String -LiteralPath $ExecutionCompiled -Pattern $Term -SimpleMatch -Quiet)) {
        throw "Model profile lost content: $Term"
    }
}
if (Select-String -LiteralPath $ExecutionCompiled -Pattern "E区块" -SimpleMatch -Quiet) {
    throw "Model execution unexpectedly contains E attachment."
}
& $Python $Validator $ExecutionCompiled --mode sd
if ($LASTEXITCODE -ne 0) {
    throw "Compiled live-action five-field model payload failed SD validation."
}
Remove-Item -LiteralPath $ExecutionCompiled -Force

$SoundSheet = Join-Path $env:TEMP "dream-sd-sound-sheet-test.md"
& $Python (Join-Path $DreamRoot "scripts\compile_sound_cue_sheet.py") (Join-Path $Fixtures "pass-sd.md") --mix-manifest (Join-Path $Fixtures "sound-mix-pass.json") --output $SoundSheet
if ($LASTEXITCODE -ne 0 -or -not (Select-String -LiteralPath $SoundSheet -Pattern "Estimated RMS dBFS" -SimpleMatch -Quiet)) {
    throw "Sound cue-sheet compiler failed."
}
Remove-Item -LiteralPath $SoundSheet -Force

$V6SoundSheet = Join-Path $env:TEMP "dream-sd-v6-sound-sheet-test.md"
& $Python (Join-Path $DreamRoot "scripts\compile_sound_cue_sheet.py") (Join-Path $Fixtures "pass-sd-30s-animation-sitcom.md") --output $V6SoundSheet
if ($LASTEXITCODE -ne 0) {
    throw "V6 five-field sound cue-sheet compiler failed."
}
foreach ($Term in @("0-4秒", "27-30秒", "切菜声", "锅记得", "秦艽")) {
    if (-not (Select-String -LiteralPath $V6SoundSheet -Pattern $Term -SimpleMatch -Quiet)) {
        throw "V6 sound cue-sheet lost content: $Term"
    }
}
Remove-Item -LiteralPath $V6SoundSheet -Force

$SoundReport = Join-Path $env:TEMP "dream-sd-sound-mix-test.json"
& $Python (Join-Path $DreamRoot "scripts\calculate_sound_mix.py") (Join-Path $Fixtures "sound-mix-pass.json") --strict --output $SoundReport
if ($LASTEXITCODE -ne 0 -or -not (Select-String -LiteralPath $SoundReport -Pattern '"status": "pass"' -Quiet)) {
    throw "Sound mix calculator rejected the valid fixture."
}
Remove-Item -LiteralPath $SoundReport -Force

& $Python (Join-Path $DreamRoot "scripts\calculate_sound_mix.py") (Join-Path $Fixtures "sound-mix-fail.json") --strict | Out-Null
if ($LASTEXITCODE -eq 0) {
    throw "Sound mix calculator accepted the invalid fixture."
}

$FrameReport = Join-Path $env:TEMP "dream-sd-frame-qa-test.json"
& $Python (Join-Path $DreamRoot "scripts\analyze_frame_sequence.py") (Join-Path $DreamRoot "scripts\fixtures\frame-sequence") --output $FrameReport
if ($LASTEXITCODE -ne 0 -or -not (Select-String -LiteralPath $FrameReport -Pattern '"frame_count": 2' -Quiet)) {
    throw "Frame sequence QA failed."
}
Remove-Item -LiteralPath $FrameReport -Force

$AudioReport = Join-Path $env:TEMP "dream-sd-audio-delivery-test.json"
& $Python (Join-Path $DreamRoot "scripts\analyze_audio_delivery.py") --self-test --strict --output $AudioReport
if ($LASTEXITCODE -ne 0 -or -not (Select-String -LiteralPath $AudioReport -Pattern '"integrated_lufs"' -Quiet)) {
    throw "Audio delivery QA self-test failed."
}
Remove-Item -LiteralPath $AudioReport -Force

$BehavioralDirectory = Join-Path $Fixtures "behavioral"
& $Python (Join-Path $PSScriptRoot "render_behavioral_fixtures.py") --output $BehavioralDirectory | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Behavioral fixture renderer failed."
}
$BehavioralPayload = & $Python (Join-Path $PSScriptRoot "run_behavioral_regression.py") $BehavioralDirectory --json
if ($LASTEXITCODE -ne 0) {
    throw "Behavioral regression runner failed."
}
$BehavioralText = $BehavioralPayload -join "`n"
if ($BehavioralText -notmatch '"pass"\s*:\s*34' -or $BehavioralText -notmatch '"fail"\s*:\s*0' -or $BehavioralText -notmatch '"pending"\s*:\s*0') {
    throw "Behavioral regression summary changed unexpectedly."
}

Write-Host "Static storyboard/SD regression passed."
