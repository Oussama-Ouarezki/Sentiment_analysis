# Algeria-Telecom-Sentiment-Analysis

This project provides a comprehensive data visualization and sentiment analysis solution for the three major Algerian mobile operators: **Ooredoo, Djezzy, and Mobilis**. 

The goal is to evaluate customer perception and brand image through Facebook interactions using NLP (Natural Language Processing) and Power BI.

## Project Overview
* **Data Source:** Facebook Posts and Comments datasets.
* **Sentiment Analysis:** Automated classification using a fine-tuned **BERT** model via the **Hugging Face** ecosystem.
* **Visualization:** Interactive Power BI dashboard focusing on competitive benchmarking and sentiment trends.

## Repository Structure
* `data/`: Contains the datasets used for the analysis (Excel/CSV).
* `scripts/`: Python script for AI-powered sentiment labeling.
* `report/`: Detailed PDF documentation of the methodology and results.
* `Project_Data_Vis.pbix`: The full Power BI project file.

## Sentiment Analysis (AI & NLP)
The core of the analysis uses a Transformer-based architecture to process complex dialectal text.

### The Model: CAMeLBERT
I utilized the **CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment** model. 
* **BERT Architecture:** It uses a Bidirectional Encoder Representations from Transformers (BERT) base.
* **Hugging Face Integration:** The script implements the Hugging Face `transformers` library to manage the model pipeline and tokenization.
* **Dialectal Support:** Unlike standard Arabic models, this is specifically fine-tuned for **Dialectal Arabic (DA)**, making it highly effective for **Algerian Darija** and social media comments.

### AI Processing Logic:
1. **Tokenization:** Text is cleaned and truncated to a maximum of 512 tokens.
2. **Inference:** The BERT model analyzes the context of the comment.
3. **Classification:** The model outputs a probability score for three labels: `positive`, `negative`, and `neutral`.

## Power BI Dashboard Features
The dashboard consists of five interconnected pages with dynamic filtering (Date/Operator) and intuitive navigation.

### 1. Main KPI Overview
Displays high-level metrics including total comments and reactions per operator, alongside the **Total vs. Average Post Scores** to identify which brand has the most impactful presence.

### 2. Post Analytics & Scoring
Detailed tracking of engagement through a custom **Post Sentiment Formula**:
$$PostScore = (2 \times Love) + (1.7 \times Wow) + (1.5 \times Care) + (1.2 \times Like) - (0.5 \times Sad) - (0.8 \times Angry)$$
* **Temporal Trends:** Line charts showing the evolution of scores by month/year.
* **Detailed Grain:** Tables breaking down every reaction type per individual post.

### 3. Comment & Sentiment Analysis
Analysis of user feedback using a weighted **Comment Score**:
$$CommentScore = (1.2 \times Positive) + (0.3 \times Neutral) - (1 \times Negative)$$
* **Sentiment Distribution:** 100% stacked bar charts showing the ratio of Positif/Neutre/Négatif per operator.
* **Word Clouds:** Identification of recurring keywords in customer feedback.


## Installation & Usage

### 1. Sentiment Analysis
To run the sentiment analysis script locally:
```bash
pip install -r requirements.txt
python scripts/analyse-sentiment.py
```

### 2. Dashboard
Open the `Project_Data_Vis.pbix` file using Power BI Desktop. Ensure the data source paths are updated to point to the files in the `data/` folder.
