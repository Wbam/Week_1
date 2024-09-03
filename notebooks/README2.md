# Stock Sentiment Analysis and Correlation Project

This project aims to analyze the sentiment of financial news headlines and correlate the sentiment with the daily returns of selected stocks. The goal is to determine whether there is a statistically significant relationship between news sentiment and stock movements.

## Project Overview

The project includes the following main steps:

1. **Data Collection**: Merging historical stock price data with news headlines data.
2. **Sentiment Analysis**: Performing sentiment analysis on news headlines using the VADER sentiment analysis tool.
3. **Daily Returns Calculation**: Computing daily percentage changes in stock closing prices to represent stock movements.
4. **Correlation Analysis**: Determining the correlation between daily sentiment scores and daily stock returns.

## Data Sources

- **Financial News Headlines**: A CSV file containing news headlines, publication dates, and stock ticker symbols.
- **Stock Price Data**: CSV files containing daily historical stock data (e.g., `AAPL`, `AMZN`, `GOOG`, `META`, `MSFT`, `NVDA`, `TSLA`).

## Tools and Libraries

- Python 3.x
- Pandas
- NLTK (Natural Language Toolkit)
- TextBlob
- Matplotlib (for plotting)
- Scipy (for statistical analysis)

## Installation

To run this project, ensure you have Python 3.x installed, and then install the required libraries:

```bash
pip install pandas nltk textblob matplotlib scipy
```
