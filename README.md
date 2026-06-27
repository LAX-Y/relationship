# Relationship Coach — 用科学理论指导你的亲密关系

**一个基于 26 个实证心理学理论的 OpenClaw 聊天分析 skill。**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-%3E%3D2026.3.22-green)](https://openclaw.ai)

---

## 这个 skill 能做什么

把你的聊天记录发给它，它用 **26 个经过实证检验的心理学理论** 来分析，告诉你：

- 你和 TA 的互动质量健康吗？（戈特曼 5:1 正负比 + 四骑士检测）
- 你们是不是陷入了焦虑-回避陷阱？（依恋理论）
- 谁在这段关系中更有权力？（最少兴趣原则）
- 你的大脑是不是在骗你？（认知失调、曝光效应、蔡格尼克效应）
- 这到底算不算爱？（斯滕伯格爱情三角诊断）
- 值不值得继续？（Rusbult 投入模型）
- 下一次该怎么互动？（峰终定律 + 强化理论 + 社会渗透）

**不是通用的"好好沟通"——每条建议都有科学依据和置信度标注。**

---

## 26 个理论基础

| 时期 | 理论 | 来源 |
|------|------|------|
| 经典 | 蔡格尼克效应、曝光效应、互惠喜欢、最少兴趣原则、心理抗拒 | 1927-1968 |
| 基础 | 依恋理论、非暴力沟通、社会渗透、认知失调、情绪 ABC（REBT） | 1950s-1990s |
| 实验 | 戈特曼四骑士+5:1、斯滕伯格三角、Rusbult 投入模型、峰终定律、损失厌恶 | 1979-2015 |
| 最新 | 成长vs命运心态、关系动荡理论、感知伴侣回应性、感恩绑定理论、积极建设性回应、智慧推理 | 2004-2017 |

**全部理论均标注原始实证来源（期刊、年份、作者）。**

---

## 适用人群

5 种场景，分别引导不同阅读路径：

| 场景 | 描述 |
|------|------|
| A | 初次心动——从未开始，不知怎么推进 |
| B | 暧昧/早期约会——关系定义模糊 |
| C | 分手后放不下——过去仍然影响你 |
| D | 关系中遇到问题——需要修复 |
| E | 稳定关系——想维护和深化 |

---

## 安装

**OpenClaw:**
```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/LAX-Y/relationship.git relationship-coach-oss
openclaw gateway restart
```

**Claude Code:** 克隆后在对话中说"帮我分析感情"，`CLAUDE.md` 自动加载。

**Cursor / 通用 Agent:** `AGENTS.md` 会被自动识别。也可将 `CLAUDE.md` 内容粘贴到自定义指令。

**ChatGPT / 任何 LLM:** 粘贴 `CLAUDE.md` 到自定义指令，`references/theory_reference.md` 上传到 Knowledge。

---

## 首次使用

在对话中说"感情咨询"或"帮我分析聊天记录"。首次使用时会自动引导你填写 6 模块画像问卷（你是谁 → TA 的画像 → 你们的故事 → 依恋自测 → 行为观察 → 你的目标）。

---

## 核心特性

- **画像自动纠正：** 自述可能有偏差——skill 会根据实际聊天数据自动检测并纠正
- **反确认偏差：** 在推荐"继续"之前，强制检查"我是不是因为用户想听才这么说？"
- **双场景输出：** 每个重大决策都同时输出"继续的路径"和"退出的路径"
- **置信度标注：** 每条建议标注高/中/低置信度
- **数据全本地：** 所有聊天记录和分析存储在本地

---

## 科学诚信

- 所有 26 个理论均引用同行评审的原始文献
- MBTI 等工具仅作启发式描述，手册中明确标注其学术局限性
- 不讨好用户——证据指向退出时，直接建议退出
- 不确定时，标注不确定

---

## 隐私

所有数据存储在你本地的 `memory/` 目录中。不上传、不收集、不分享。

---

## 执照

MIT

---

> ⚠️ 本 skill 提供基于科学理论的心理分析，但不能替代专业心理咨询。如果你正经历严重的情绪困扰或关系暴力，请寻求专业帮助。

---

## Relationship Coach — Science-Backed Relationship Analysis for OpenClaw

An OpenClaw skill that analyzes your chat records using **26 empirically validated psychological theories**. Not generic advice — evidence-backed analysis with specific, actionable recommendations.

### What It Does

Paste your chat records. The skill analyzes them across 6 dimensions:

- **Interaction Quality** — Gottman's 5:1 ratio + Four Horsemen detection
- **Attachment Dynamics** — Bowlby & Bartholomew attachment patterns
- **Power Balance** — Waller's Least Interest + Brehm's Reactance
- **Communication** — NVC + Social Penetration + PPR + ACR
- **Cognitive Traps** — Dissonance, ABC model, Zeigarnik, Growth/Destiny beliefs
- **Love Diagnosis** — Sternberg's Triangle + Rusbult's Investment Model

### Theories (26 total)

Early (1927-1968): Zeigarnik Effect, Mere Exposure, Reciprocity of Liking, Least Interest, Reactance

Foundational (1950s-1990s): Attachment Theory, NVC, Social Penetration, Cognitive Dissonance, ABC/REBT

Experimental (1979-2015): Gottman's Four Horsemen & 5:1 Ratio, Sternberg's Triangle, Rusbult's Investment Model, Peak-End Rule, Loss Aversion, Self-Determination Theory, Self-Expansion & Michelangelo Phenomenon

Recent (2004-2017): Growth vs Destiny Beliefs (Howe & Dweck, 2016), Relational Turbulence Theory (Solomon et al., 2016), Perceived Partner Responsiveness (Reis et al., 2017), Find-Remind-Bind Gratitude (Algoe, 2016), Active Constructive Responding (Gable, 2004), Wise Reasoning (Grossmann, 2017)

### Key Features

- Auto-correcting relationship profiles
- Anti-confirmation bias checks
- Dual-scenario decision support (continue AND exit paths)
- Confidence annotations on all recommendations
- Fully local data storage

### Install

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/LAX-Y/relationship.git relationship-coach-oss
openclaw gateway restart
```

Trigger with "感情咨询" or "analyze my chat" in a conversation.

### License

MIT
