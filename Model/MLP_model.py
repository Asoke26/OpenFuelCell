import os
import pandas as pd 
import tensorflow as tf
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split

# Input Data
input_file = "/home/ad26/Projects/Fall-19/EECS-245/tensorFlow/data_home/quicktestStack-formatted-output.csv"

# read_input_csv = open(input_file,'r') 
quicktestStack_data = pd.read_csv(input_file,error_bad_lines=False) 

print("columns ",len(quicktestStack_data.columns))

# Creating training and test dataset
input_features = ['Time', 'Tair_min', 'Tair_mean', 'Tair_max', 'Tfuel_min', 'Tfuel_mean',
       'Tfuel_max', 'rhoAir_min', 'rhoAir_mean', 'rhoAir_max', 'rhoFuel_min',
       'rhoFuel_mean', 'rhoFuel_max', 'muAir_min', 'muAir_mean', 'muAir_max',
       'muFuel_min', 'muFuel_mean', 'muFuel_max', 'nuAir_min', 'nuAir_mean',
       'nuAir_max', 'nuFuel_min', 'nuFuel_mean', 'nuFuel_max', 'kAir_min',
       'kAir_mean', 'kAir_max', 'kFuel_min', 'kFuel_mean', 'kFuel_max',
       'sumVolume', 'Nern_min', 'Nern_max', 'ibar0', 'ibar', 
       'min_curr', 'max_curr', 'Energy_Ir', 'Energy_Fr',
       'Energy_t_min', 'Energy_t_mean', 'Energy_t_max']

print("Input input_features :",len(input_features))
predict_features = ['Voltage','mean_curr']

X = quicktestStack_data[input_features]
Y = quicktestStack_data[predict_features]
X_train,X_test,Y_train,Y_test = train_test_split(quicktestStack_data, Y, test_size=0.3)

print(X_train.shape)
print("\n\n")
print(X_test.shape)
print("\n\n")

print(Y_train.shape)
print("\n\n")
print(Y_test.shape)
print("\n\n")

## Defining various initialization parameters for 784-512-256-10 MLP model
num_classes = Y_train.shape[1]
num_features = X_train.shape[1]
num_output = Y_train.shape[1]
num_layers_0 = 512
num_layers_1 = 256
starter_learning_rate = 0.001
regularizer_rate = 0.1





# # Placeholders for the input data
# input_X = f(X_train)
# input_y = f(Y_train)
# ## for dropout layer
# keep_prob = tf.compat.v1.placeholder(tf.float32)


## Weights initialized by random normal function with std_dev = 1/sqrt(number of input features)
# weights_0 = tf.Variable(tf.random_normal([num_features,num_layers_0], stddev=(1/tf.sqrt(float(num_features)))))
# bias_0 = tf.Variable(tf.random_normal([num_layers_0]))
# weights_1 = tf.Variable(tf.random_normal([num_layers_0,num_layers_1], stddev=(1/tf.sqrt(float(num_layers_0)))))
# bias_1 = tf.Variable(tf.random_normal([num_layers_1]))
# weights_2 = tf.Variable(tf.random_normal([num_layers_1,num_output], stddev=(1/tf.sqrt(float(num_layers_1)))))
# bias_2 = tf.Variable(tf.random_normal([num_output]))

# ## Initializing weigths and biases
# hidden_output_0 = tf.nn.relu(tf.matmul(input_X,weights_0)+bias_0)
# hidden_output_0_0 = tf.nn.dropout(hidden_output_0, keep_prob)
# hidden_output_1 = tf.nn.relu(tf.matmul(hidden_output_0_0,weights_1)+bias_1)
# hidden_output_1_1 = tf.nn.dropout(hidden_output_1, keep_prob)
# predicted_y = tf.sigmoid(tf.matmul(hidden_output_1_1,weights_2) + bias_2)

# ## Defining the loss function
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=predicted_y,labels=input_y)) \
#         + regularizer_rate*(tf.reduce_sum(tf.square(bias_0)) + tf.reduce_sum(tf.square(bias_1)))

# ## Variable learning rate
# learning_rate = tf.train.exponential_decay(starter_learning_rate, 0, 5, 0.85, staircase=True)
# ## Adam optimzer for finding the right weight
# optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss,var_list=[weights_0,weights_1,weights_2,bias_0,bias_1,bias_2])

# ## Metrics definition
# correct_prediction = tf.equal(tf.argmax(y_train,1), tf.argmax(predicted_y,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# ## Training parameters
# batch_size = 128
# epochs=14
# dropout_prob = 0.6
# training_accuracy = []
# training_loss = []
# testing_accuracy = []
# s.run(tf.global_variables_initializer())
# for epoch in range(epochs):    
#     arr = np.arange(X_train.shape[0])
#     np.random.shuffle(arr)
#     for index in range(0,X_train.shape[0],batch_size):
#         s.run(optimizer, {input_X: X_train[arr[index:index+batch_size]],
#                           input_y: y_train[arr[index:index+batch_size]],
#                         keep_prob:dropout_prob})
#     training_accuracy.append(s.run(accuracy, feed_dict= {input_X:X_train,input_y: y_train,keep_prob:1}))
#     training_loss.append(s.run(loss, {input_X: X_train,input_y: y_train,keep_prob:1}))
    
#     ## Evaluation of model
#     testing_accuracy.append(accuracy_score(y_test.argmax(1),s.run(predicted_y, {input_X: X_test,keep_prob:1}).argmax(1)))
#     print("Epoch:{0}, Train loss: {1:.2f} Train acc: {2:.3f}, Test acc:{3:.3f}".format(epoch,training_loss[epoch],training_accuracy[epoch],testing_accuracy[epoch]))