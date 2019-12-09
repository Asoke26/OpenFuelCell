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
dataset = pd.read_csv('C:\\Users\Ashok\Documents\EECS245\OpenFuelCell\Data\sofc-output.csv')
X = dataset.iloc[:,0:9].values
Y = dataset.iloc[:,9].values


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
from tensorflow.keras import layers

# Initialising the ANN
mlp_regrassor = Sequential()



#Add hidden layer
mlp_regrassor.add(Dense(units=5,kernel_initializer='uniform',activation='relu',input_shape=(9,)))
mlp_regrassor.add(Dense(units=5,kernel_initializer='uniform',activation='relu'))
# Add a LSTM layer with 24 internal units.
# mlp_regrassor.add(layers.LSTM((24)))
mlp_regrassor.add(Dense(units=5,kernel_initializer='uniform',activation='relu'))

# Add output layer
mlp_regrassor.add(Dense(units=1,kernel_initializer='normal',activation='linear'))

#Compiling the ANN model
mlp_regrassor.compile(optimizer='adam',loss = 'mean_squared_error',metrics=['accuracy'])

#Fitting the model in our Training data
mlp_regrassor.fit(X_train,Y_train,batch_size = 100,epochs = 10,verbose = 2)

#Evaluate the model
from sklearn.metrics import r2_score
Y_prediction = mlp_regrassor.predict(X_test)
r2_score(Y_test,Y_prediction)


