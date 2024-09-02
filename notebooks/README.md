# Financial News and Stock Price Integration Dataset (FNSPID) Analysis

## Overview

This project explores the **Financial News and Stock Price Integration Dataset (FNSPID)**, containing headlines, publication details, and stock ticker symbols from financial news articles. The goal is to derive insights into publication trends, sentiment, and publisher activity within the financial news domain.

## Data Structure

The dataset includes the following columns:

- **headline**: Title of the news article, reflecting key financial actions.
- **url**: Direct link to the full news article.
- **publisher**: Author or creator of the article.
- **date**: Publication date and time (UTC-4 timezone).
- **stock**: Stock ticker symbol representing the company covered in the news.

## Exploratory Data Analysis (EDA)

### Descriptive Statistics
- **Headline Length**: Analyzed lengths of headlines to understand typical title lengths.
- **Publisher Activity**: Counted the number of articles per publisher to identify the most active contributors.
- **Publication Trends**: Examined publication dates to detect patterns and trends in news frequency.

### Text Analysis
- **Sentiment Analysis**: Classified the sentiment of headlines as positive, negative, or neutral.
- **Topic Modeling**: Identified common keywords and topics to highlight significant events or themes.

### Time Series Analysis
- **Publication Frequency**: Analyzed publication frequency over time and identified spikes related to market events.
- **Publishing Times**: Investigated timing of news releases to determine peak publishing times.

### Publisher Analysis
- **Top Publishers**: Identified the most frequent publishers.
- **Domain Analysis**: Analyzed publisher email domains to determine if specific organizations are more active.

## Installation

To run the analysis, clone the repository and install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn nltk
