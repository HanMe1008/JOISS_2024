### Make and Save model

# modul load
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, SimpleRNN, GRU, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.initializers import GlorotUniform, Orthogonal, Zeros

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

# LSTM model
lstm_model = Sequential()
lstm_model.add(LSTM(64, activation='tanh', return_sequences=True, input_shape=(27, 1), 
                    kernel_initializer=GlorotUniform(seed=42),   
                    recurrent_initializer=Orthogonal(seed=42),  
                    bias_initializer=Zeros(),                   
                    name='lstm_layer_1'))
lstm_model.add(LSTM(32, activation='tanh',
                    kernel_initializer=GlorotUniform(seed=42),   
                    recurrent_initializer=Orthogonal(seed=42),  
                    bias_initializer=Zeros(),                   
                    name='lstm_layer_2'))
lstm_model.add(Dense(1, activation='linear', name='output'))

lstm_model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001), metrics=['mae'])

# RNN model
rnn_model = Sequential()
rnn_model.add(SimpleRNN(64, activation='tanh', return_sequences=True, input_shape=(27, 1), 
                        kernel_initializer=GlorotUniform(seed=42),   
                        recurrent_initializer=Orthogonal(seed=42),  
                        bias_initializer=Zeros(),                  
                        name='rnn_layer_1'))
rnn_model.add(SimpleRNN(32, activation='tanh', 
                        kernel_initializer=GlorotUniform(seed=42),   
                        recurrent_initializer=Orthogonal(seed=42), 
                        bias_initializer=Zeros(),                   
                        name='rnn_layer_2'))
rnn_model.add(Dense(1, activation='linear', name='output'))

rnn_model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001), metrics=['mae'])

# GRU model
gru_model = Sequential()
gru_model.add(GRU(64, activation='tanh', return_sequences=True, input_shape=(27, 1), 
                  kernel_initializer=GlorotUniform(seed=42),   
                  recurrent_initializer=Orthogonal(seed=42),  
                  bias_initializer=Zeros(),                  
                  name='gru_layer_1'))
gru_model.add(GRU(32, activation='tanh',
                  kernel_initializer=GlorotUniform(seed=42),   
                  recurrent_initializer=Orthogonal(seed=42),  
                  bias_initializer=Zeros(),                   
                  name='GRU_layer_2'))
gru_model.add(Dense(1, activation='linear', name='output'))

gru_model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001), metrics=['mae'])

# Model training
lstm_history = lstm_model.fit(train_scaled, train_target, epochs=50, validation_data=(val_scaled, val_target), verbose=0)
rnn_history = rnn_model.fit(train_scaled, train_target, epochs=50, validation_data=(val_scaled, val_target), verbose=0)
gru_history = gru_model.fit(train_scaled, train_target, epochs=50, validation_data=(val_scaled, val_target), verbose=0)

# Validation predict
lstm_val_predictions = lstm_model.predict(val_scaled)
rnn_val_predictions = rnn_model.predict(val_scaled)
gru_val_predictions = gru_model.predict(val_scaled)

# evaluation
lstm_val_loss = lstm_history.history['val_loss']
rnn_val_loss = rnn_history.history['val_loss']
gru_val_loss = gru_history.history['val_loss']

lstm_val_mae = lstm_history.history['val_mae']
rnn_val_mae = rnn_history.history['val_mae']
gru_val_mae = gru_history.history['val_mae']

# plotting
plt.figure(figsize=(16, 6))

# Loss graph
plt.subplot(1, 2, 1)
plt.plot(lstm_history.history['loss'], label='LSTM Train Loss')
plt.plot(lstm_history.history['val_loss'], label='LSTM Val Loss')
plt.plot(rnn_history.history['loss'], label='RNN Train Loss')
plt.plot(rnn_history.history['val_loss'], label='RNN Val Loss')
plt.plot(gru_history.history['loss'], label='GRU Train Loss')
plt.plot(gru_history.history['val_loss'], label='GRU Val Loss')
plt.title('Loss Comparison')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()

# MAE graph
plt.subplot(1, 2, 2)
plt.plot(lstm_history.history['mae'], label='LSTM Train MAE')
plt.plot(lstm_history.history['val_mae'], label='LSTM Val MAE')
plt.plot(rnn_history.history['mae'], label='RNN Train MAE')
plt.plot(rnn_history.history['val_mae'], label='RNN Val MAE')
plt.plot(gru_history.history['mae'], label='GRU Train MAE')
plt.plot(gru_history.history['val_mae'], label='GRU Val MAE')
plt.title('MAE Comparison')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()

plt.tight_layout()
plt.show()

# model save
lstm_model.save('lstm_model') 
rnn_model.save('rnn_model') 
gru_model.save('gru_model') 
