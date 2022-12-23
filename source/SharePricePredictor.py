import streamlit as st
import datetime as date

import yfinance as yf
from fbprophet import Prophet

from fbprophet.plot import pyfinancelot_plotly
from plotly import graph_objs as go

START = "2010-01-01"
TODAY = date.date.today().strftime("%Y-%m-%d")


st.title("Future Stock Price Prediction Web")


stocks = ("AAPL", "GOOG", "MSFT", "GME", "TSLA")
selected_stock = st.selectbox("Select data set for prediction from the drop down box", stocks)


n_years = st.slider("Years of prediction", 1, 4)
period = n_years * 365


@st.cache

def load_data(ticker):

	data = yf.download(ticker, START, TODAY)
	data.reset_index(inplace=True)
	return data


data_load_state = st.text("Load Data....")
data = load_data(selected_stock)
print(type(data))
data_load_state.text("Loading Data...Done")


st.subheader('Raw Data')
st.write(data.tail())


def plot_raw_data():

	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
	fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)    #for zooming, better viewing of carts
	st.plotly_chart(fig)


plot_raw_data()


#Forecasting The Big Trade
df_train = data[['Date', 'Close']]                                     #syntax for 'data' to read the comand
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})       #just to agree with the syntax  of fbprophet's syntax



m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period) #from line 21
forecast = m.predict(future)  #df_eval


st.subheader('Forecasted Data')
st.write(forecast.tail())


st.write('Forecasted data')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)


st.write('Forecasted Components')
fig2 = m.plot_components(forecast)
st.write(fig2)

