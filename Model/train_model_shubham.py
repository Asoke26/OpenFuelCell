import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv("keras_output.csv")

#print(data)

# Tair_min,Tair_mean,Tair_max,Tfuel_min,Tfuel_mean,Tfuel_max,rhoAir_min,rhoAir_mean,rhoAir_max,rhoFuel_min,
# rhoFuel_mean,rhoFuel_max,muAir_min,muAir_mean,muAir_max,muFuel_min,muFuel_mean,muFuel_max,nuAir_min,nuAir_mean,nuAir_max,nuFuel_min,nuFuel_mean,nuFuel_max,
# kAir_min,kAir_mean,kAir_max,kFuel_min,kFuel_mean,kFuel_max,sumVolume,Nern_min,Nern_max,ibar0,ibar
# ,V,stack_Voltage,min_curr,mean_curr,max_curr,Energy_Ir,Energy_Fr,Energy_t_min,Energy_t_mean,Energy_t_max

input=['Tair_min','Tair_mean','Tair_max','Tfuel_min','Tfuel_mean','Tfuel_max','rhoAir_min','rhoAir_mean','rhoAir_max','rhoFuel_min','rhoFuel_mean',
 'rhoFuel_max','muAir_min','muAir_mean','muAir_max','muFuel_min','muFuel_mean','muFuel_max','nuAir_min','nuAir_mean','nuAir_max','nuFuel_min','nuFuel_mean','nuFuel_max',
   'kAir_min', 'kAir_mean', 'kAir_max', 'kFuel_min', 'kFuel_mean', 'kFuel_max', 'sumVolume', 'Nern_min', 'Nern_max', 'ibar0', 'ibar'
    , 'stack_Voltage', 'min_curr','mean_curr','max_curr', 'Energy_Ir', 'Energy_Fr', 'Energy_t_min',  'Energy_t_max']

output=['V','Energy_t_mean']

X=data[input]
Y=data[output]

train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.3,random_state=1)

model=tf.keras.Sequential([tf.keras.layers.Dense(43,input_shape=(43,),activation='relu'),
                           tf.keras.layers.Dense(256, input_shape=(43,), activation='sigmoid'),
                           tf.keras.layers.Dense(256, input_shape=(43,), activation='sigmoid'),
                           tf.keras.layers.Dense(2,activation='softmax')])

model.compile(optimizer='sgd',
              loss=tf.keras.losses.mse,
              metrics=['accuracy'])

model.fit(train_x,train_y,epochs=10)







