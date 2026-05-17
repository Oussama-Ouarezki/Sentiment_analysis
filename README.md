# 📡 Sentiment Analysis & Competitive Benchmarking of Algerian Telecom Operators

> Turning Facebook comments into strategic insights for **Ooredoo**, **Djezzy**, and **Mobilis**

---

## 🧭 What Is This Project About?

Every day, thousands of Algerians comment on the Facebook pages of the country's three major mobile operators. These comments carry valuable opinions — complaints about network quality, praise for offers, frustration with customer service.

This project **automatically collects, analyzes, and visualizes** all of that public data to answer one key question:

> **What do Algerians actually think about their telecom operator — and how does that compare to the competition?**

The result is an interactive **Power BI dashboard** that any manager or decision-maker can use to track public sentiment over time and benchmark operators side by side.

---

## 🗺️ How It Works — Step by Step

```
Facebook Pages  →  Data Collection  →  Cleaning  →  AI Sentiment Analysis  →  Power BI Dashboard
```

### 1. 📥 Data Collection
Posts and comments were gathered from the official Facebook pages of **Ooredoo Algérie**, **Djezzy**, and **Mobilis**. Two datasets were produced:
- **Posts.csv** — every post published by each operator (with reaction counts: likes, loves, angrys, etc.)
- **Comments.csv** — every user comment left on those posts

### 2. 🧹 Data Cleaning
The raw data was standardized: duplicates removed, dates unified, reaction counts verified, and blank comments filtered out — leaving clean, analysis-ready tables.

### 3. 🤖 AI-Powered Sentiment Analysis
Each comment was automatically classified as **Positive**, **Neutral**, or **Negative** using a specialized Arabic-language AI model ([CAMeL-BERT](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment)) from HuggingFace — designed specifically for Algerian/Arabic dialectal text.

### 4. 📊 Interactive Dashboard
All results feed into a **5-page Power BI dashboard** with filters by operator and date, enabling live competitive comparison.

---

## 📊 Dashboard Pages

### 🏠 Main Page — High-Level Overview
Key metrics at a glance: total reactions, total comments, and scores per operator.

![Main Dashboard](https://github.com/user-attachments/assets/de98bb69-57ee-48d4-bd1d-4cbabf1ffb15)

---

### 📈 Publication Summary — Post Performance Over Time
Tracks how each operator's posts performed month by month, using a weighted score that rewards positive reactions (Love, Wow, Care) and penalizes negative ones (Angry, Sad).

![Publication Summary](https://github.com/user-attachments/assets/d17e720a-c93c-4ef2-93dd-05dcc6c86f02)

---

### 📋 Publication Table — Detailed Post Data
A searchable, filterable table of every post with its full reaction breakdown and calculated score.

![Publication Table](https://github.com/user-attachments/assets/55d79485-bd5b-44a0-9c17-8f2492cbe8b1)

---

### 💬 Comment Summary — Public Sentiment Analysis
Shows the sentiment distribution per operator (positive / neutral / negative) and how it evolves over time.

![Comment Summary](https://github.com/user-attachments/assets/07f1a3b8-b8a5-4bc5-9cce-a118be498a60)

---

### 🗂️ Comment Table — Individual Comment Details
Every comment with its operator, date, text, and AI-assigned sentiment label.

![Comment Table](https://github.com/user-attachments/assets/bd43fc14-dd72-4a12-9a23-8a468d3961c7)

---

## 🏆 Key Findings

| Metric | 🥇 1st | 🥈 2nd | 🥉 3rd |
|---|---|---|---|
| **Avg. Post Score** | Mobilis | Ooredoo | Djezzy |
| **Avg. Comment Sentiment** | Ooredoo | Mobilis | Djezzy |
| **Most Positive Comments** | Ooredoo (~58%) | Mobilis (~42%) | Djezzy |
| **Most Negative Comments** | Djezzy (~44%) | — | — |

### Notable observations:
- 📌 **Mobilis** posts fewer things, but each post generates stronger positive reactions — quality over quantity.
- 📉 **Ooredoo** and **Djezzy** both show a downward trend in post scores over time; Mobilis shows a decline followed by a **recovery**.
- ⚠️ **Djezzy** has the weakest public sentiment overall, with the highest share of negative comments.

---

## 🛠️ Tools & Technologies

| Layer | Tool |
|---|---|
| Data Collection | Python (web scraping) |
| Data Cleaning | Power Query (in Power BI) |
| Sentiment Analysis | HuggingFace — `CAMeL-BERT` Arabic model |
| Visualization | Microsoft Power BI |

---

## 📄 Full Documentation

For a complete technical report including methodology, data model, and scoring formulas:

👉 **[Click here for the full project report (PDF)](https://github.com/Oussama-Ouarezki/Sentiment_analysis/blob/main/report/report.pdf)**

---

## 👥 Who Is This For?

This dashboard is designed for:
- **Marketing teams** tracking brand perception vs. competitors
- **Communication managers** identifying the best and worst-received content
- **Business analysts** benchmarking operator performance using public data

No technical background needed to use the dashboard — just open, filter, and explore.
