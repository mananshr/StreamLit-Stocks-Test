import numpy as np
import yfinance as yf
import pandas as pd
import streamlit as st
import math
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

symbol = "AAPL"

symbol = st.selectbox(
    "Select a stock to analyse",
    (
        "AAPL",
        "ACN",
        "ADBE",
        "ADP",
        "AMD",
        "AMZN",
        "AVGO",
        "BABA",
        "BRK-A",
        "CMCSA",
        "CSCO",
        "GILD",
        "GOOG",
        "INTC",
        "JNJ",
        "JPM",
        "KO",
        "MA",
        "MCD",
        "META",
        "MSFT",
        "NFLX",
        "NVDA",
        "ORCL",
        "PG",
        "TSLA",
        "TSM",
        "V",
        "WMT",
        "TM",
    ),
)

ticker_data = yf.Ticker(symbol)

df = ticker_data.history(period="1y")
fig = plt.figure(figsize=(16, 8))
plt.title('historical price past year')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close_Price', fontsize=18)
st.pyplot(fig)

df = ticker_data.history(period="5y")
fig = plt.figure(figsize=(16, 8))
plt.title('historical price past 5 yrs')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close_Price', fontsize=18)
st.pyplot(fig)

df = ticker_data.history(period="max")
fig = plt.figure(figsize=(16, 8))
plt.title('historical price since inception')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close_Price', fontsize=18)
st.pyplot(fig)

data = df.filter(['Close'])
print(data)
temp_array = np.array(data)
print(temp_array)
temp_df = temp_array.reshape(-1, 1)
print(temp_df)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_df = scaler.fit_transform(np.array(temp_df.reshape(-1, 1)))
print("Scaled DF")
print(scaled_df)

training_data_len = math.ceil(len(scaled_df)*0.8)
print("training_data_len ")
print(training_data_len)

training_data = scaled_df[0:training_data_len, :]
x_train = []
y_train = []

for i in range(60, len(training_data)):
    x_train.append(training_data[i-60:i, 0])
    y_train.append(training_data[i, 0])
    if i <= 60:
        print(x_train)
        print(y_train)

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
print(x_train.shape)

# Modeling

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(50))
# model.add(Dense(1))

with st.spinner("Running Predictions....[This may take a long time...]"):
    model.compile(optimizer='adam', loss='mean_squared_error')
    # print(model.summary())
    model.fit(x_train, y_train, batch_size=40, epochs=20)
st.success('Done!')

test_data = scaled_df[training_data_len - 60:, :]
x_test = []

print(type(df))
print("Total length:")
print(len(df.index))
print("training_data_len:")
print(training_data_len)

y_test = scaled_df[training_data_len:, :]

if y_test is None:
    print("y_test is none lol")

try:
    print("y_test")
    print(y_test)
except Exception as exp:
    print(exp)

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(predictions-y_test)**2)
print("rmse")
print(rmse)
print("predictions")
print(predictions.shape)
print(type(predictions))
print(predictions)

train = data[:training_data_len]
val = data[training_data_len:]
val['predictions'] = predictions[:, 0]
fig = plt.figure(figsize=(16, 8))
plt.title('model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close_Price', fontsize=18)
plt.plot(train['Close'])
plt.plot(val[['Close', 'predictions']],)
plt.legend(['train', 'val', 'predictions'], loc='lower right')

st.pyplot(fig)

test = df[training_data_len:]
fig = plt.figure(figsize=(16,8))
plt.title('historical price')
plt.plot(test)
plt.plot(predictions)
plt.xlabel('Days', fontsize=18)
plt.ylabel('Close_Price', fontsize=18)
plt.legend(['test', 'predictions'], loc='lower right')
st.pyplot(fig)
