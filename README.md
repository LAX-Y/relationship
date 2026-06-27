# Relationship Coach — OpenClaw Skill

**An OpenClaw skill for relationship chat analysis using 15 empirically validated psychological theories.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-%3E%3D2026.3.22-green)](https://openclaw.ai)

---

## What It Does

This skill transforms OpenClaw into a relationship coach that analyzes your chat records with a romantic interest. It applies **15 scientifically validated psychological theories** to deliver structured, actionable coaching — not generic "communication tips", but evidence-backed analysis with specific behavioral recommendations.

### Analysis Dimensions

| Dimension | Theory Used | What It Tells You |
|-----------|------------|-------------------|
| **Interaction Quality** | Gottman's 5:1 Ratio + Four Horsemen | Is your communication healthy or toxic? |
| **Attachment Dynamics** | Bowlby & Bartholomew Attachment Theory | Are you in an anxious-avoidant trap? |
| **Power Balance** | Waller's Least Interest + Brehm's Reactance | Who holds the power in this dynamic? |
| **Communication Quality** | Rosenberg's NVC + Altman's Social Penetration | Are you connecting or pushing away? |
| **Cognitive Traps** | Festinger's Dissonance + Ellis's ABC | Is your brain lying to you about this? |
| **Love Type Diagnosis** | Sternberg's Triangular Theory | Is this love, infatuation, or nostalgia? |

---

## Theories & Scientific Sources

| # | Theory | Source |
|---|--------|--------|
| 1 | Zeigarnik Effect | Zeigarnik (1927) |
| 2 | Attachment Theory | Bowlby (1969); Bartholomew (1991) |
| 3 | Nonviolent Communication | Rosenberg (1972) |
| 4 | Social Exchange Theory | Thibaut & Kelley (1959) |
| 5 | Peak-End Rule | Kahneman (1999) |
| 6 | Loss Aversion | Kahneman & Tversky (1979) |
| 7 | Reinforcement Theory | Skinner (1953) |
| 8 | Sternberg's Triangular Theory of Love | Sternberg (1986), *Psychological Review* |
| 9 | Gottman's Four Horsemen + 5:1 Ratio | Gottman (1994, 1999, 2015) |
| 10 | Rusbult's Investment Model | Rusbult (1980, 1983), *JPSP* |
| 11 | Self-Expansion Theory + Michelangelo Phenomenon | Aron & Aron (1986); Drigotas et al. (1999) |
| 12 | Mere Exposure Effect | Zajonc (1968) |
| 13 | Social Penetration Theory | Altman & Taylor (1973) |
| 14 | Cognitive Dissonance + ABC Model (REBT) | Festinger (1957); Ellis (1955) |
| 15 | Self-Determination Theory | Deci & Ryan (2000) |

**Full theory reference:** See `references/theory_reference.md` (~25 pages with experimental citations, mechanisms, and practical applications).

---

## Installation

### Prerequisites

- OpenClaw >= 2026.3.22
- Node.js >= 22

### Quick Install

```bash
# Install the skill into your workspace
cd ~/.openclaw/workspace/skills
git clone https://github.com/YOUR_USERNAME/openclaw-relationship-coach.git relationship-coach-oss
```

Then restart the OpenClaw gateway:

```bash
openclaw gateway restart
```

The skill will appear in your enabled skills list as `relationship-coach-oss`.

---

## First Use

Start a new conversation with OpenClaw and say any of the following:

- "感情咨询"
- "帮我分析一段聊天记录"
- "这段对话什么意思"
- "我该怎么回她"
- "她是不是喜欢我"

On first use, the skill detects you have no profile yet and guides you through a **6-module interactive questionnaire** covering:

1. **Who You Are** (15%) — personality type, gender, age
2. **Partner Profile** (35%) — their personality, conflict style, emotional openness, inferred attachment
3. **Your Story** (20%) — relationship history, break-reconnect cycles, current status
4. **Attachment Self-Test** (15%) — ECR-based anxiety/avoidance scoring
5. **Partner Behavior Observations** (10%) — specific patterns you've noticed
6. **Your Goals** (5%) — what you actually want and whether you can accept "exit" as an outcome

Or run the questionnaire from the command line:

```bash
python scripts/init_profile.py
```

---

## How It Works

```
You paste chat records
        ↓
Skill appends to archive
        ↓
Loads your relationship profile
        ↓
Analyzes across 6 psychological dimensions
        ↓
Outputs structured report:
  • Key metrics (5:1 ratio, Sternberg scores, cold-shoulder counter)
  • Pattern discoveries
  • Warning signals (if any)
  • Actionable recommendations
  • Suggested replies (NVC format, 2-3 tone options)
  • Theory references with confidence levels
        ↓
Auto-corrects profile if behavior contradicts self-report
        ↓
Compresses old records into summary when archive grows
```

### Key Features

- **Profile Auto-Correction:** Self-report is biased. The skill compares your stated profile against actual chat behavior and corrects discrepancies — with evidence and confidence levels.
- **Anti-Confirmation Bias:** Before recommending "continue", the skill asks: *"Am I leaning this way because evidence supports it, or because the user wants to hear it?"*
- **Dual-Scenario Output:** Every decision recommendation outputs both "what happens if you continue" AND "what happens if you exit" — with equal rigor.
- **Confidence Annotation:** Every recommendation states its evidence basis and confidence level (高/中/低).
- **Memory Persistence:** Chat records, analyses, and compressed summaries persist across sessions.

---

## File Structure

```
relationship-coach-oss/
├── SKILL.md                         # Skill trigger + 7-step workflow
├── README.md                        # This file
├── references/
│   ├── theory_reference.md          # 25-page theory manual
│   └── questionnaire.md            # 6-module interactive questionnaire
├── scripts/
│   ├── init_profile.py              # Interactive profile builder
│   ├── score_sternberg.py           # Sternberg love triangle calculator
│   └── compress_archive.py          # Chat archive compressor
└── assets/
    └── report_template.md           # Standardized analysis report template
```

---

## Scientific Integrity

- All 15 theories cite original peer-reviewed sources with journal names and years.
- MBTI and other personality type tools are used only as **heuristic descriptors**, not clinical diagnostics. The manual explicitly states their limitations (Pittenger, 1993; Grant, 2013).
- Recommendations are explicitly anti-sugar-coating: the skill will recommend exit when evidence supports it, regardless of user preference.
- Uncertainty is acknowledged: every output includes confidence levels and notes when more data is needed.

---

## Privacy

- **All data stays local.** Chat records are stored only in your workspace's `memory/` directory.
- **No data collection.** This skill does not send any data anywhere.
- **You control everything.** Profile, archives, and analyses are plain Markdown files you can review, edit, or delete at any time.

---

## Contributing

Contributions are welcome. Key areas:

- Additional psychological theories backed by empirical research
- Improved scoring algorithms in `scripts/`
- Multi-language support
- Integration with other chat platforms

Please ensure all theory additions include peer-reviewed citations.

---

## License

MIT — see [LICENSE](LICENSE)

---

> ⚠️ **Disclaimer:** This skill provides psychological analysis based on established scientific theories, but it is not a substitute for professional therapy or counseling. If you're experiencing severe emotional distress or relationship abuse, please seek qualified professional help.
