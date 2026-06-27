#!/usr/bin/env python3
"""
Sternberg Love Triangle Score Calculator — score_sternberg.py

Computes Intimacy, Passion, and Commitment scores from chat interaction data
based on Sternberg's Triangular Theory of Love (1986).

Each dimension is scored 1-5 across 5 items → total /25 per dimension.

Usage:
    python score_sternberg.py --intimacy 4,3,5,4,3 --passion 5,4,3,4,5 --commitment 2,2,3,3,2

Output:
    Intimacy:  19/25
    Passion:   21/25
    Commitment: 12/25
    Type: Romantic Love (Intimacy + Passion, low Commitment)
"""

import argparse
import sys


def compute_dimension(scores: list[int], name: str) -> tuple[int, str]:
    """Compute score and label for one dimension."""
    total = sum(scores)
    if total >= 18:
        label = "高"
    elif total >= 12:
        label = "中"
    else:
        label = "低"
    return total, label


def classify_type(intimacy: tuple, passion: tuple, commitment: tuple) -> str:
    """
    Classify love type based on Sternberg's 8 types.
    High >= 18, Medium >= 12, Low < 12.
    """
    i_score, i_label = intimacy
    p_score, p_label = passion
    c_score, c_label = commitment

    i_high = i_score >= 18
    p_high = p_score >= 18
    c_high = c_score >= 18

    i_low = i_score < 12
    p_low = p_score < 12
    c_low = c_score < 12

    if i_high and p_high and c_high:
        return "完美之爱 (Consummate Love) — 极其罕见"
    elif i_high and p_high and not c_high:
        return "浪漫之爱 (Romantic Love) — 享受但注意承诺缺失"
    elif i_high and not p_high and c_high:
        return "伴侣之爱 (Companionate Love) — 长期关系的坚实基础"
    elif not i_high and p_high and not c_high:
        return "痴迷 (Infatuation) — 可能是蔡格尼克效应伪装"
    elif not i_high and p_high and c_high:
        return "愚昧之爱 (Fatuous Love) — 闪婚风险极高"
    elif i_high and not p_high and not c_high:
        return "喜欢 (Liking) — 知己/朋友"
    elif not i_high and not p_high and c_high:
        return "空洞之爱 (Empty Love) — 义务而非爱"
    else:
        return "无爱 (Non-love) 或低水平混合"


def main():
    parser = argparse.ArgumentParser(description="Sternberg Love Triangle Calculator")
    parser.add_argument("--intimacy", required=True, help="5 comma-separated scores (1-5) for Intimacy")
    parser.add_argument("--passion", required=True, help="5 comma-separated scores (1-5) for Passion")
    parser.add_argument("--commitment", required=True, help="5 comma-separated scores (1-5) for Commitment")
    args = parser.parse_args()

    try:
        intimacy_scores = [int(x.strip()) for x in args.intimacy.split(",")]
        passion_scores = [int(x.strip()) for x in args.passion.split(",")]
        commitment_scores = [int(x.strip()) for x in args.commitment.split(",")]
    except ValueError:
        print("错误: 所有分数必须是 1-5 的整数")
        sys.exit(1)

    for name, scores in [("亲密", intimacy_scores), ("激情", passion_scores), ("承诺", commitment_scores)]:
        if len(scores) != 5:
            print(f"错误: {name} 需要恰好 5 个分数")
            sys.exit(1)
        if any(s < 1 or s > 5 for s in scores):
            print(f"错误: {name} 所有分数必须在 1-5 之间")
            sys.exit(1)

    i = compute_dimension(intimacy_scores, "亲密")
    p = compute_dimension(passion_scores, "激情")
    c = compute_dimension(commitment_scores, "承诺")
    love_type = classify_type(i, p, c)

    print(f"""
╔══════════════════════════════════════╗
║   斯滕伯格爱情三角评分               ║
╠══════════════════════════════════════╣
║  亲密 (Intimacy):   {i[0]:2d}/25  ({i[1]})      ║
║  激情 (Passion):    {p[0]:2d}/25  ({p[1]})      ║
║  承诺 (Commitment): {c[0]:2d}/25  ({c[1]})      ║
╠══════════════════════════════════════╣
║  类型: {love_type[:35]} ║
╚══════════════════════════════════════╝
""")


if __name__ == "__main__":
    main()
