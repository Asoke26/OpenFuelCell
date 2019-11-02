import os
import pandas as pd 
import tensorflow as tf


input_file = "/home/ad26/Projects/Fall-19/EECS-245/OpenFuelCell/Data/parsed-output-quicktestStack.csv"

# read_input_csv = open(input_file,'r') 
read_input_csv = pd.read_csv(input_file) 

# for line in read_input_csv:
# 	print(line)