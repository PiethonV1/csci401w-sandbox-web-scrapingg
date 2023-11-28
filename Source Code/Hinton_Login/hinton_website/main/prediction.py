
# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

import requests
from bs4 import BeautifulSoup

START = "2013-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

# This renders the stock news as a sidebar
col2 = st.sidebar

# Update the symbols to stock name
stock_name = selected_stock

if selected_stock == 'GOOG':
    stock_name = 'Google'
elif selected_stock == 'AAPL':
    stock_name = 'Apple'
elif selected_stock == 'MSFT':
    stock_name = 'Microsoft'
else:
    stock_name = 'GameStop'

# Dynamically update the title to selected stock
st.title(f'{stock_name} Stock Predictions')

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

@st.cache_data
@st.experimental_memo
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    # Updated the bar color 
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open", line=dict(color='black')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close", line=dict(color='green')))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())

st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
fig1.update_traces(line=dict(color='green'))
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
fig1.update_traces(line=dict(color='green'))
st.write(fig2)

# This is the sidebar to scrape news for selected symbol
with col2:
    def get_stock_news(symbol, num_articles=5):
        # Get stock data using yfinance
        stock = yf.Ticker(symbol)

        st.title(f'{stock_name}\'s Latest Headlines')
        
        # Get the stock's summary page URL
        stock_url = f'https://finance.yahoo.com/quote/{symbol}'
        
        # Fetch the HTML content of the summary page
        response = requests.get(stock_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract news headlines from the Yahoo Finance page
            headlines = soup.find_all('h3', class_='Mb(5px)')

            # Display the latest headlines using st.write
            for i, headline in enumerate(headlines[:num_articles]):
                st.write(f"{i + 1}. {headline.text}")

        else:
            st.write(f"Failed to fetch data for {symbol}")
            
    # Update the stock news dynamically
    stock_symbol = 'selected_stock'
    get_stock_news(selected_stock)