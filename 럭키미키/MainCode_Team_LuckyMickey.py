### Team_LuckyMickey MainCode
## Prediction for Yellow Sea Test Set

# model load
from tensorflow.keras.models import load_model

lstm_model = load_model('lstm_model')
rnn_model = load_model('rnn_model')
gru_model = load_model('gru_model')

# module load
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Set random seed
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

# Trainset load
df = pd.read_csv('MachineLearningData.csv')

input_df = df.iloc[:, :27]
target_df = df['temp_0m_tom']

all_input = input_df.values.tolist()
all_target = target_df.values.tolist()
all_target = np.array(all_target)

train_input, val_input, train_target, val_target = train_test_split(all_input, all_target, test_size=0.2, random_state=42)

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
val_scaled = ss.transform(val_input)

# Testset load
df = pd.read_csv('TestsetData.csv')

test_input_df = df.iloc[:, :27]
test_target_df = df['temp_0m_tom']

test_input = test_input_df.values.tolist()
test_target = test_target_df.values.tolist()
test_target = np.array(test_target)
test_scaled = ss.transform(test_input)

yes_sst = df['temp_0m_yes']
yes_sst = yes_sst.tolist()

# RNN model prediction
rnn_test_predictions = rnn_model.predict(test_scaled)

test_mse = mean_squared_error(test_target, rnn_test_predictions)
test_mae = mean_absolute_error(test_target, rnn_test_predictions)

print("RNN Test MSE:", test_mse)
print("RNN Test MAE:", test_mae)

plt.figure(figsize=(10, 5))
plt.plot(test_target, label='Tomorrow Actual SST', color='blue')
plt.plot(rnn_test_predictions, label='Tomorrow Predicted SST', color='orange')
plt.title('RNN Model Predictions vs Actual SST')
plt.xlabel('Sample Index')
plt.ylabel('SST')

plt.ylim(12, 30)
plt.yticks(np.arange(12, 30, 2))

plt.legend(loc='lower left')
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.show()

# GRU model prediction
gru_test_predictions = gru_model.predict(test_scaled)

test_mse = mean_squared_error(test_target, gru_test_predictions)
test_mae = mean_absolute_error(test_target, gru_test_predictions)

print("GRU Test MSE:", test_mse)
print("GRU Test MAE:", test_mae)

plt.figure(figsize=(10, 5))
plt.plot(test_target, label='Tomorrow Actual SST', color='blue')
plt.plot(gru_test_predictions, label='Tomorrow Predicted SST', color='orange')
plt.title('GRU Model Predictions vs Actual SST')
plt.xlabel('Sample Index')
plt.ylabel('SST')

plt.ylim(12, 30)
plt.yticks(np.arange(12, 30, 2))

plt.legend(loc='lower left')
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.show()

# LSTM model prediction
lstm_test_predictions = lstm_model.predict(test_scaled)

test_mse = mean_squared_error(test_target, lstm_test_predictions)
test_mae = mean_absolute_error(test_target, lstm_test_predictions)

print("LSTM Test MSE:", test_mse)
print("LSTM Test MAE:", test_mae)

plt.figure(figsize=(10, 5))
plt.plot(test_target, label='Tomorrow Actual SST', color='blue')
plt.plot(lstm_test_predictions, label='Tomorrow Predicted SST', color='orange')
                
plt.title('LSTM Model Predictions vs Actual SST')
plt.xlabel('Sample Index')
plt.ylabel('SST')

plt.ylim(12, 30)
plt.yticks(np.arange(12, 30, 2))

plt.legend(loc='lower left')
plt.grid(True, axis='y', linestyle='--', linewidth=0.5)
plt.show()