#######################################
#       Asoke Datta                   #
#               PhD Student           #
#   University of California, Merced  #
#######################################


# Importing Required Library
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Importing the dataset 
import pandas as pd
dataset = pd.read_csv('C:\\Users\Ashok\Documents\EECS245\OpenFuelCell\Data\quicktestStack-formatted-output.csv')
dataset.drop(0, axis=0, inplace=True)
dataset.drop('Time', axis=1, inplace=True)
X = dataset.iloc[:,0:12].values
Y = dataset.iloc[:,12].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Importing the Keras libraries and packages
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Initialising the ANN
mlp_regrassor = Sequential()

#Add hidden layer
mlp_regrassor.add(Dense(units=36,kernel_initializer='uniform',activation='relu',input_shape=(12,)))
mlp_regrassor.add(Dense(units=24,kernel_initializer='uniform',activation='relu'))
mlp_regrassor.add(Dense(units=12,kernel_initializer='uniform',activation='relu'))

# Add output layer
mlp_regrassor.add(Dense(units=1,kernel_initializer='uniform',activation='linear'))

#Compiling the ANN model
mlp_regrassor.compile(opimizer='adam',loss = 'mean_absolute_error',matrics=['accuracy'])

#Fitting the model in our Training data
mlp_regrassor.fit(X_train,Y_train,batch_size = 10,epochs = 100,verbose = 2)

#Evaluate the model
from sklearn.metrics import r2_score
Y_prediction = mlp_regrassor.predict(X_test)
r2_score(Y_test,Y_prediction)


