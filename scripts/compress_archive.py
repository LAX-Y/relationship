#!/usr/bin/env python3
"""
Chat Archive Compressor — compress_archive.py

Reads her_chat_archive.md and produces a compressed summary in
her_chat_summary.md, preserving key patterns while discarding verbatim
chat content older than the retention threshold.

Usage:
    python compress_archive.py
    python compress_archive.py --archive path/to/archive.md --summary path/to/summary.md --retention 14
"""

import argparse
import re
import os
from datetime import datetime, timedelta

RETENTION_DAYS = 14
SUMMARY_HEADER = """# 聊天压缩摘要 — her_chat_summary

> 🗜️ 自动生成于: {timestamp}
> 📅 保留最近 {days} 天的详细记录，更早的内容已压缩为摘要。

---

## 摘要

"""


def extract_date_from_block(block: str) -> datetime | None:
    """Extract date from a chat block header."""
    match = re.search(r'(\d{4}-\d{2}-\d{2})', block)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            pass
    return None


def summarize_block(block: str) -> str:
    """Generate a brief summary of a chat block."""
    lines = block.strip().split("\n")
    summary_lines = []

    # Extract date
    date_match = re.search(r'(\d{4}-\d{2}-\d{2}.*?)(?:\n|$)', block)
    date_str = date_match.group(1) if date_match else "未知日期"

    # Count interactions
    speaker_a = len(re.findall(r'^(?:A|我|用户)[：:]', block, re.MULTILINE))
    speaker_b = len(re.findall(r'^(?:B|TA|她|他)[：:]', block, re.MULTILINE))
    total = speaker_a + speaker_b

    # Extract key topics (simple keyword-based)
    topics = []
    keywords = {
        "见面": "见面/约会讨论",
        "感情": "感情状态讨论",
        "过去": "过去关系回顾",
        "冷淡": "冷淡/距离信号",
        "晚安": "温馨互动",
        "想": "思念/情感表达",
        "忙": "忙碌/推脱",
        "复合": "复合讨论",
    }
    for kw, desc in keywords.items():
        if kw in block:
            topics.append(desc)

    if total > 0:
        summary_lines.append(f"- **{date_str}** | 共 {total} 条消息 | {', '.join(topics[:3]) if topics else '日常互动'}")
        if speaker_a > 0 and speaker_b > 0:
            ratio = speaker_a / max(speaker_b, 1)
            if ratio > 2:
                summary_lines.append(f"  - ⚠ 你发消息比例过高 ({speaker_a}:{speaker_b})")
            elif ratio < 0.5:
                summary_lines.append(f"  - TA 发消息更多 ({speaker_a}:{speaker_b})")

    return "\n".join(summary_lines)


def main():
    parser = argparse.ArgumentParser(description="Compress chat archive to summary")
    parser.add_argument("--archive", default="memory/her_chat_archive.md", help="Path to archive file")
    parser.add_argument("--summary", default="memory/her_chat_summary.md", help="Path to summary output")
    parser.add_argument("--retention", type=int, default=RETENTION_DAYS, help="Days to retain verbatim")
    args = parser.parse_args()

    if not os.path.exists(args.archive):
        print(f"错误: 找不到 archive 文件: {args.archive}")
        return

    with open(args.archive, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into blocks by date separators
    blocks = re.split(r'\n---\n(?=\d{4}-\d{2}-\d{2})', content)
    cutoff_date = datetime.now() - timedelta(days=args.retention)

    recent_blocks = []
    old_blocks = []
    header = ""

    for i, block in enumerate(blocks):
        if i == 0:
            # First block is the header
            header = block
            continue
        date = extract_date_from_block(block)
        if date and date >= cutoff_date:
            recent_blocks.append(block)
        else:
            old_blocks.append(block)

    # Generate summary from old blocks
    summaries = []
    for block in old_blocks:
        summary = summarize_block(block)
        if summary:
            summaries.append(summary)

    # Load existing summary if any
    existing_summary = ""
    if os.path.exists(args.summary):
        with open(args.summary, "r", encoding="utf-8") as f:
            existing_summary = f.read()

    # Rebuild archive with recent + header
    new_archive = header + "\n---\n" + "\n---\n".join(recent_blocks) if recent_blocks else header
    with open(args.archive, "w", encoding="utf-8") as f:
        f.write(new_archive)

    # Build new summary
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    summary_content = SUMMARY_HEADER.format(timestamp=timestamp, days=args.retention)
    summary_content += "\n".join(summaries) if summaries else "（无更早的记录需要压缩）"
    summary_content += "\n\n---\n\n## 历史摘要\n\n" + existing_summary.split("## 历史摘要")[-1] if "## 历史摘要" in existing_summary else ""

    with open(args.summary, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"✅ 压缩完成:")
    print(f"   保留最近 {args.retention} 天的 {len(recent_blocks)} 个对话块")
    print(f"   压缩了 {len(old_blocks)} 个旧对话块 → {args.summary}")


if __name__ == "__main__":
    main()
