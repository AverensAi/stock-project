import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Apple Stock Price Data

This is a simple project, showing volumes and dividends of the Apple company

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'AAPL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2010-5-31', end='2023-08-21')
# Open	High   Low	 Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Dividends)

# to run the program type in the Terminal "streamlit run ..." with the name of the file. 
# Do not forget to enter the right directory