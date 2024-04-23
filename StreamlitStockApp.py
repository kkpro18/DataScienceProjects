import yfinance as yf
import streamlit as st

st.write("""# This is my first Streamlit Web App! 
Enter the Stock Symbol you would like to see the data for, 
and the High Value, Close Value and Volume will be displayed in chart form.
It ranges from 2020 to Present. """
)


# tickerSymbol = 'GOOGL'

stock_name = st.text_input('Enter Stock Name')
tickerSymbol = stock_name

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2020-01-01', end='2024-04-23')
# Open High | Low close | Volume | Dividends | Stock Splits

st.write("""High Value""")
st.line_chart(tickerDf.High)
st.write("""Close Value""")
st.line_chart(tickerDf.Close)
st.write("""Volume""")
st.line_chart(tickerDf.Volume)
