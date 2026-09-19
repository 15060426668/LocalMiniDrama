/**
 * 规范化全能片段里「分镜 k： X 秒:」时长：单条时对齐总时长；多条时按比例缩放使秒数之和等于 totalSec。
 * 智能判断规则：仅在 narrative boundary（段落切换/新场景）时强制≤4s，普通连续动作可放宽
 * @param {string} text
 * @param {string} durationLabel 展示用总时长（与 totalSec 一致，如 "15" 或 "5.5"）
 * @param {number} totalSec 本条数据库分镜/API 片段总秒数
 * @param {object} context 可选上下文包含 segment_title, prev_segment_title, next_segment_title 用于判断边界
 */
function normalizeUniversalSegmentShotDurations(text, durationLabel, totalSec, context = {}) {
  if (!text || typeof text !== 'string' || !durationLabel) return text;
  const total = Number(totalSec);
  if (!Number.isFinite(total) || total <= 0) return text;

  const lines = text.split(/\r?\n/);
  /** @type {{ i: number, k: number, sec: number, rest: string }[]} */
  const hits = [];
  const headRe = /^\s*分镜 (\d+)\s*[:：]\s*([\d.]+)\s*秒\s*[:：]\s*/i;
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(headRe);
    if (!m) continue;
    const k = Number(m[1]);
    const sec = Number(m[2]);
    const rest = lines[i].slice(m[0].length);
    if (Number.isFinite(k) && k >= 1) hits.push({ i, k, sec: Number.isFinite(sec) && sec > 0 ? sec : 1, rest });
  }
  if (hits.length === 0) return text;

  hits.sort((a, b) => a.k - b.k || a.i - b.i);
  const uniq = [];
  const seenK = new Set();
  for (const h of hits) {
    if (seenK.has(h.k)) continue;
    seenK.add(h.k);
    uniq.push(h);
  }
  if (uniq.length === 0) return text;

  const fmt = (x) => (Number.isInteger(x) ? String(x) : String(Math.round(x * 10) / 10));

  // Intelligent 4-second constraint based on narrative boundary detection
  const MAX_BEAT_DURATION = 4.0; // Hard limit for narrative boundaries
  const hasPrevSeg = context.prev_segment_title && String(context.prev_segment_title).trim() !== '';
  const hasNextSeg = context.next_segment_title && String(context.next_segment_title).trim() !== '';
  const currSegTitle = String(context.segment_title || '').trim();
  const isBoundaryStart = hasPrevSeg && currSegTitle && currSegTitle !== String(context.prev_segment_title || '').trim();
  const isBoundaryEnd = hasNextSeg && currSegTitle && currSegTitle !== String(context.next_segment_title || '').trim();
  
  // Detect if this shot is at a narrative boundary (segment change)
  const isNarrativeBoundary = isBoundaryStart || isBoundaryEnd;
  
  console.log(`[4s Constraint] Shot info: isBoundary=${isNarrativeBoundary}, currSeg="${currSegTitle}", prevSeg="${context.prev_segment_title || 'none'}", nextSeg="${context.next_segment_title || 'none'}"`);

  if (uniq.length === 1 && uniq[0].k === 1) {
    const { i } = uniq[0];
    lines[i] = lines[i].replace(headRe, `分镜 1： ${durationLabel}秒: `);
    return lines.join('\n');
  }

  const weights = uniq.map((h) => Math.max(0.05, h.sec));
  const wsum = weights.reduce((a, b) => a + b, 0);
  let allocated = 0;
  const newSecs = uniq.map((_, idx) => {
    if (idx === uniq.length - 1) {
      const last = Math.round((total - allocated) * 10) / 10;
      return Math.max(0.1, last);
    }
    const raw = (total * weights[idx]) / wsum;
    const v = Math.max(0.1, Math.round(raw * 10) / 10);
    allocated += v;
    return v;
  });
  const sumMid = newSecs.slice(0, -1).reduce((a, b) => a + b, 0);
  newSecs[newSecs.length - 1] = Math.max(0.1, Math.round((total - sumMid) * 10) / 10);
  const sumAll = newSecs.reduce((a, b) => a + b, 0);
  if (sumAll > total + 0.05 || newSecs[newSecs.length - 1] < 0.09) {
    const each = Math.max(0.1, Math.round((total / uniq.length) * 10) / 10);
    for (let i = 0; i < uniq.length - 1; i++) newSecs[i] = each;
    newSecs[uniq.length - 1] = Math.max(0.1, Math.round((total - each * (uniq.length - 1)) * 10) / 10);
  }

  // Apply intelligent 4s constraint
  // If narrative boundary detected, enforce MAX_BEAT_DURATION hard limit
  // Otherwise, allow up to 6-8s for continuous actions (warning only)
  for (let j = 0; j < uniq.length; j++) {
    const { i, k } = uniq[j];
    let adjustedSec = newSecs[j];
    
    if (isNarrativeBoundary) {
      // Strict enforcement at narrative boundaries
      if (adjustedSec > MAX_BEAT_DURATION) {
        console.warn(`[4s Constraint Warning] Shot ${k} duration ${adjustedSec}s exceeds ${MAX_BEAT_DURATION}s limit at narrative boundary. Will be flagged for user review.`);
        adjustedSec = MAX_BEAT_DURATION;
      }
    } else {
      // Soft warning for long continuous shots
      if (adjustedSec > 6.0) {
        console.warn(`[4s Constraint Soft Warning] Shot ${k} duration ${adjustedSec}s exceeds 6s recommended max for continuous action. Consider splitting into multiple beats.`);
      }
    }
    
    const lab = fmt(adjustedSec);
    lines[i] = lines[i].replace(headRe, `分镜${k}： ${lab}秒: `);
  }
  
  return lines.join('\n');
}

module.exports = { normalizeUniversalSegmentShotDurations };
