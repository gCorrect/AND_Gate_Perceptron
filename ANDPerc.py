from code import interact
import pandas as pd
import numpy as np
import csv
import sys
sys.path.append(r'C:\Users\nanas\Desktop\Nikos2\Lessons\Ypol_nohm\Ergasia\Tutorials\python\AND_GATE_Perceptron\libraries')
from functions import *
from loaddata import *
from plot import *
print("-----------------------------------------------------------------------------------")
# Training
# functions
def step_function(x):
    if x<0:
        return 0
    else:
        return 1
# variables
tablename= "lg_and"
df=pd.DataFrame(loaddata(tablename=tablename),columns=['x1', 'x2','EO'])
print("data frame: \n",df)
cols = 2 # columns count
n = 0.5 # learning rate
iterations_count=0 
expected_output = df["EO"] # ALT -> data['output'] 
#   # Weights
weights = weights(cols)
data = np.asarray(df) # asarray df
print("data[row,1:3]---\n",data[:,0:2])
rows = len(data[:,0]) # Data_Rows
# data
# Epochs
epoch=True
correct=False
errors=[None]*rows
b = 0
# while (epoch!=correct):
for epoch in range(0,30):
    for row in range(0, rows):
        net_sum = np.sum(np.multiply(data[row,:1],weights)) #net_sum = Σ(x[i]*w[i]) Bias*w[0] included 
        # Activation Function
        actual_output= step_function(net_sum + b)
        errors[row] = expected_output[row] - actual_output
        iterations_count+=1
        # Change Weights
        for col in range(0, cols):
            weights[col] += n * errors[row] * data[row,col] # If (!error) => DON'T CHANGE, else CHANGE        
            b += n * errors[row] 

print("---------------------------")
print("iterations_count",iterations_count)
print("---------------------------")
print("w_0 = %.3f" %(weights[0]))
print("w_1 = %.3f" %(weights[1])) 
#plot
  #data
x1,y1,x2,y2 = loadPlotdata(tablename=tablename)
plotdata(x1,y1,x2,y2)
  #line
slope = weights[1]/weights[2]
intercept = weights[0]/weights[2]
# plotline(slope=slope,intercept=intercept,start=0,end=1.5)
a = [0,-b/weights[1]]
c = [-b/weights[0],0]
plt.plot(a,c)

plt.show()

print("-----------------------------------------------------------------------------------")

# Next Goals
 # -> Draw line

# Garbage notes
# print("data[:, 0] ",data[:, 0])
# print("---------------------------")
# print("tr_count: ",training_count)
# # data[:, :1]
# training_count1 = len(data[:, :1])
# print("data[:, :1] ",data[:, :1])
# print("---------------------------")
# print("tr_count1: ",training_count1)

# # Drop, output
# df = df.drop(['EO'], axis=1) # Drop output
# print("Output dropped")
# print("---------------------------")
# df[:, 0] 

# for epoch in range(0,5):
#     for datum in range(0, training_count):
#         net_sum = np.sum(np.multiply(data[datum,0:3],weights)) #net_sum = Σ(x[i]*w[i]) Bia*w[0] included 
#         # Activation Function
#         if net_sum < 0: 
#             actual_output = 0
#         else:
#             actual_output = 1
#         error = expected_output[datum] - actual_output
#         iterations_count+=1
#         # Change Weights
#         for n in range(0, input_dim):
#             weights[n] = weights[n] + learning_rate*error*data[datum,n] # If (!error) => DON'T CHANGE, else CHANGE 
# print("---------------------------")
# print("iterations_count",iterations_count)
# print("---------------------------")
# print("w_0 = %.3f" %(weights[0]))
# print("w_1 = %.3f" %(weights[1])) 
# print("w_2 = %.3f" %(weights[2]))    

# for check in error:
#           if check==1:
#             break

# print("expected Output: \n", expected_output)
