#!/usr/bin/env python3
"""
Relationship Profile Initializer — init_profile.py

Interactive command-line tool that walks the user through the 6-module
questionnaire and generates memory/relationship_profile_oss.md.

Usage:
    python init_profile.py
    python init_profile.py --output memory/relationship_profile_oss.md
"""

import os
import sys
from datetime import datetime


def ask(question: str, options: list[str] | None = None, default: str = "") -> str:
    """Ask a question, optionally with numbered options."""
    print(f"\n{'=' * 60}")
    print(f"  {question}")
    if options:
        for i, opt in enumerate(options, 1):
            print(f"    [{i}] {opt}")
    if default:
        prompt = f"  > (默认: {default}): "
    else:
        prompt = "  > "
    answer = input(prompt).strip()
    if not answer and default:
        answer = default
    if options and answer.isdigit():
        idx = int(answer) - 1
        if 0 <= idx < len(options):
            answer = options[idx]
    return answer


def ask_scale(question: str) -> int:
    """Ask a 1-5 scale question."""
    while True:
        try:
            val = int(input(f"  {question} [1-5]: ").strip())
            if 1 <= val <= 5:
                return val
            print("  ⚠ 请输入 1-5 之间的数字")
        except ValueError:
            print("  ⚠ 请输入数字")


def main():
    print("\n" + "=" * 60)
    print("  💕 关系画像问卷 — Relationship Profile Builder")
    print("=" * 60)
    print("  本问卷有 5 个模块，约 20 题，预计 10 分钟完成。")
    print("  你的回答将用于 AI 在分析聊天记录时提供个性化建议。")
    print("  所有数据仅存储在你的本地 workspace。\n")

    profile = {"created_at": datetime.now().strftime("%Y-%m-%d %H:%M")}
    scores = {}

    # ── Module 1: Who You Are ──
    print("\n" + "━" * 40)
    print("  模块一：你是谁")
    print("━" * 40)

    profile["mbti"] = ask("你的 MBTI / 性格类型？", default="未测试")
    profile["gender"] = ask("你的性别？", ["男", "女", "非二元"], default="男")
    age_opts = ["18岁以下", "18-22（大学生）", "23-30（初入职场）", "30岁以上"]
    profile["age_group"] = ask("你的年龄段？", age_opts, default="18-22（大学生）")

    # ── Module 2: Your Story ──
    print("\n" + "━" * 40)
    print("  模块二：你和 TA 的故事")
    print("━" * 40)

    time_opts = ["不到3个月", "3-12个月", "1-3年", "3年以上"]
    profile["known_duration"] = ask("你们认识多久了？", time_opts)
    profile["cycle_count"] = ask("经历了多少次断联→复联的循环？", default="0")
    status_opts = ["暧昧不清", "刚重新联系上", "正在发展中", "冷战/断联中", "已分手但想复合", "稳定交往中"]
    profile["current_status"] = ask("目前的关系状态？", status_opts)
    who_opts = ["我主动", "TA主动", "自然而然的"]
    profile["last_contact_initiator"] = ask("最近一次联系谁发起的？", who_opts)
    profile["core_issue"] = ask("最困扰你的问题（一句话）：", default="不确定对方的真实想法")

    # ── Module 3: TA Profile ──
    print("\n" + "━" * 40)
    print("  模块三：TA 的画像")
    print("  （你对 TA 的感知可能有偏差，后续会自动纠正）")
    print("━" * 40)

    ta_personality_opts = ["外向开朗，社交能量高", "内向安静，社交能量低", "理性冷静，情绪不外露",
                           "感性敏感，情绪表达丰富", "忽冷忽热，难以捉摸"]
    profile["ta_personality"] = ask("TA给你的人格印象？", ta_personality_opts)
    ta_conflict_opts = ["主动沟通，想解决问题", "沉默回避，不想谈", "情绪爆发，事后后悔",
                        "假装没事，但行为上疏远", "不确定/没见过"]
    profile["ta_conflict_style"] = ask("TA面对冲突时怎么反应？", ta_conflict_opts, default="不确定/没见过")
    ta_openness_opts = ["很开放——愿意分享感受和脆弱", "选择性开放——特定话题才深入",
                        "比较封闭——很少主动表达内心", "完全封闭——从不袒露真实感受"]
    profile["ta_openness"] = ask("TA对情感表达的开放程度？", ta_openness_opts)
    ta_attach_opts = ["安全型——情绪稳定", "焦虑型——需要大量确认", "回避型——亲密后需要距离",
                      "恐惧型——想要亲密又怕受伤", "不确定"]
    profile["ta_inferred_attachment"] = ask("你推测TA的依恋风格？", ta_attach_opts, default="不确定")
    ta_comm_opts = ["直接坦率——有什么说什么", "委婉含蓄——拐弯抹角", "幽默打岔——用玩笑回避",
                    "理性分析——用逻辑讨论情感", "沉默寡言——不太主动表达"]
    profile["ta_communication"] = ask("TA的沟通风格？", ta_comm_opts)
    ta_social_opts = ["中心人物——活跃，朋友多", "观察者——话少但参与", "独行侠——社交圈很小", "不太清楚"]
    profile["ta_social_role"] = ask("TA在社交中是什么角色？", ta_social_opts, default="不太清楚")
    profile["ta_overall_impression"] = ask("用一段话描述对TA的总体印象：", default="不确定")

    # ── Module 3: Attachment Self-Test ──
    print("\n" + "━" * 40)
    print("  模块三：依恋风格自测")
    print("  （1=完全不符合, 5=完全符合）")
    print("━" * 40)

    anxiety_items = [
        "TA不回消息时我会反复看手机，焦虑上升",
        "我需要频繁确认TA对我的感觉没变",
        "我担心TA会突然离开我",
    ]
    avoidance_items = [
        "当TA太靠近时我会不自在，想拉开距离",
        "我不习惯对TA完全敞开心扉",
        "在亲密关系中我需要很多个人空间",
    ]

    anxiety_score = sum(ask_scale(q) for q in anxiety_items) / 3.0
    avoidance_score = sum(ask_scale(q) for q in avoidance_items) / 3.0

    scores["anxiety"] = round(anxiety_score, 1)
    scores["avoidance"] = round(avoidance_score, 1)

    if anxiety_score >= 3.5 and avoidance_score < 3.5:
        attachment = "焦虑型 (Preoccupied)"
    elif anxiety_score >= 3.5 and avoidance_score >= 3.5:
        attachment = "恐惧型 (Fearful)"
    elif anxiety_score < 3.5 and avoidance_score >= 3.5:
        attachment = "回避-轻视型 (Dismissive)"
    else:
        attachment = "安全型 (Secure)"

    profile["attachment_style"] = attachment
    profile["anxiety_score"] = scores["anxiety"]
    profile["avoidance_score"] = scores["avoidance"]

    # ── Module 4: Observed Partner Behaviors ──
    print("\n" + "━" * 40)
    print("  模块四：你观察到的 TA 行为")
    print("━" * 40)

    profile["partner_ambiguous_behavior"] = ask(
        "TA是否说过善意的谎言或含糊其辞的话？", default="不确定"
    )
    partner_distance_opts = ["保持亲密/更近", "突然冷淡/拉开距离", "保持不变", "不确定/没到那步"]
    profile["partner_post_closeness"] = ask(
        "最亲密阶段之后TA通常怎么做？", partner_distance_opts, default="不确定/没到那步"
    )
    hc_items = [
        "忽冷忽热，回复速度波动大",
        "不愿讨论关系定义",
        "你表达需求时TA回避或转移话题",
        "TA经常主动联系但拒绝深入",
        "以上都没有",
    ]
    print("  观察到TA的哪些行为？（用逗号分隔序号，如: 1,3）")
    for i, item in enumerate(hc_items, 1):
        print(f"    [{i}] {item}")
    hc_answer = input("  > ").strip()
    profile["partner_hot_cold_behaviors"] = hc_answer if hc_answer else "5"
    other_opts = ["从未提过", "偶尔自然提到", "频繁提及,不舒服", "刻意提及,似有暗示"]
    profile["partner_mentions_others"] = ask(
        "TA是否提及其他异性？", other_opts, default="偶尔自然提到"
    )

    # ── Module 5: Your Goals ──
    print("\n" + "━" * 40)
    print("  模块五：你的目标")
    print("━" * 40)

    goal_opts = [
        "复合/重新在一起",
        "搞清楚TA的真实想法",
        "学习如何更好地沟通",
        "判断这段关系是否值得继续",
        "彻底放下/释怀",
    ]
    profile["primary_goal"] = ask("现阶段最核心的目标？", goal_opts, default="搞清楚TA的真实想法")
    accept_opts = [
        "可以接受——我需要真相不是安慰",
        "勉强接受——但会很难过",
        "不太能接受——希望结论是'可以继续'",
        "完全不能接受——我就是想继续",
    ]
    profile["accepts_exit_conclusion"] = ask(
        "能否接受'这段关系可能不值得继续'的结论？", accept_opts,
        default="可以接受——我需要真相不是安慰"
    )

    # ── Generate Profile ──
    output_path = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--output" else "memory/relationship_profile_oss.md"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    profile_md = f"""# 关系画像 — Relationship Profile

> 生成时间: {profile['created_at']}
> 依恋类型: {profile['attachment_style']}

## 基本信息
- **性格类型:** {profile['mbti']}
- **性别:** {profile['gender']}
- **年龄段:** {profile['age_group']}

## 关系历史
- **认识时长:** {profile['known_duration']}
- **断联复联循环次数:** {profile['cycle_count']}
- **当前状态:** {profile['current_status']}
- **最近联系发起方:** {profile['last_contact_initiator']}
- **核心困扰:** {profile['core_issue']}

## TA 的画像（自述，可能被自动纠正）
- **人格印象:** {profile['ta_personality']}
- **冲突反应:** {profile['ta_conflict_style']}
- **情感开放性:** {profile['ta_openness']}
- **推测依恋风格:** {profile['ta_inferred_attachment']}
- **沟通风格:** {profile['ta_communication']}
- **社交角色:** {profile['ta_social_role']}
- **总体印象:** {profile['ta_overall_impression']}

## 依恋风格
- **自测类型:** {profile['attachment_style']}
- **焦虑分:** {profile['anxiety_score']} / 5
- **回避分:** {profile['avoidance_score']} / 5

## TA 行为观察
- **含糊/欺骗行为:** {profile['partner_ambiguous_behavior']}
- **亲密后反应:** {profile['partner_post_closeness']}
- **忽冷忽热模式:** {profile['partner_hot_cold_behaviors']}
- **提及其他异性:** {profile['partner_mentions_others']}

## 目标与态度
- **核心目标:** {profile['primary_goal']}
- **对'退出'结论的接受度:** {profile['accepts_exit_conclusion']}
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(profile_md)

    print(f"\n{'=' * 60}")
    print(f"  ✅ 画像已保存到: {output_path}")
    print(f"  📊 依恋类型: {profile['attachment_style']}")
    print(f"  🎯 核心目标: {profile['primary_goal']}")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
