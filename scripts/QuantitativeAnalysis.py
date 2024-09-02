
import pandas as pd
import talib
import matplotlib.pyplot as plt
import seaborn as sns
import pynance as pn
import numpy as np

def load_and_prepare_data(file_paths):
    data_frames = [pd.read_csv(file) for file in file_paths]
    
    for df in data_frames:
        df.rename(columns={
            'open_price': 'Open', 
            'high_price': 'High',
            'low_price': 'Low',
            'closing_price': 'Close',
            'trade_volume': 'Volume'
        }, inplace=True)
        
        df.fillna(method='ffill', inplace=True)
    
    return data_frames

#Technical Analysis Indicators

def compute_technical_indicators(data_frames):
    indicators = []
    for i, df in enumerate(data_frames):
        if not all(col in df.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume']):
            print(f"DataFrame {i+1} is missing one or more required columns. Skipping...")
            continue

        df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
        df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
        df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(
            df['Close'], 
            fastperiod=12, 
            slowperiod=26, 
            signalperiod=9
        )

        indicators.append(df[['Date', 'Close', 'SMA_50', 'RSI_14', 'MACD', 'MACD_Signal', 'MACD_Hist']].head())
        print(f"DataFrame {i+1} with Indicators:")
        print(df[['Date', 'Close', 'SMA_50', 'RSI_14', 'MACD', 'MACD_Signal', 'MACD_Hist']].head(), "\n")
    
    return indicators

  #PyNance for Financial Metrics

def compute_financial_metrics(data_frames):
    for i, df in enumerate(data_frames):
        if 'Close' not in df.columns:
            print(f"DataFrame {i+1} is missing 'Close' column. Skipping...")
            continue

        df['Daily_Return'] = df['Close'].pct_change()

        annualized_return = np.prod(1 + df['Daily_Return'].dropna()) ** (252/len(df)) - 1
        print(f"DataFrame {i+1} Annualized Return: {annualized_return:.2%}")

        volatility = df['Daily_Return'].std() * np.sqrt(252)
        print(f"DataFrame {i+1} Volatility: {volatility:.2%}")

        risk_free_rate = 0.01  
        sharpe_ratio = (annualized_return - risk_free_rate) / volatility
        print(f"DataFrame {i+1} Sharpe Ratio: {sharpe_ratio:.2f}\n")

        # Visualizing the data
        
def compute_and_plot_technical_indicators(data_frames, stock_tickers):
    for i, df in enumerate(data_frames):
        if 'Close' not in df.columns:
            print(f"DataFrame {i+1} is missing 'Close' column. Skipping...")
            continue

        df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
        df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
        df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(
            df['Close'], 
            fastperiod=12, 
            slowperiod=26, 
            signalperiod=9
        )

        # Plotting Closing Prices with Moving Averages
        plt.figure(figsize=(14, 7))
        plt.plot(df['Close'], label='Close Price')
        plt.plot(df['SMA_20'], label='20-Day SMA', linestyle='--')
        plt.plot(df['SMA_50'], label='50-Day SMA', linestyle='--')
        plt.title(f'{stock_tickers[i]} Stock Close Price with Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        # Plotting RSI
        plt.figure(figsize=(14, 5))
        plt.plot(df['RSI'], label='RSI', color='orange')
        plt.axhline(70, color='red', linestyle='--')
        plt.axhline(30, color='green', linestyle='--')
        plt.title(f'{stock_tickers[i]} Relative Strength Index (RSI)')
        plt.xlabel('Date')
        plt.ylabel('RSI')
        plt.legend()
        plt.show()

        # Plotting MACD
        plt.figure(figsize=(14, 5))
        plt.plot(df['MACD'], label='MACD', color='blue')
        plt.plot(df['MACD_Signal'], label='MACD Signal', color='red')
        plt.bar(df.index, df['MACD_Hist'], label='MACD Histogram', color='gray')
        plt.title(f'{stock_tickers[i]} MACD (Moving Average Convergence Divergence)')
        plt.xlabel('Date')
        plt.ylabel('MACD')
        plt.legend()
        plt.show()
