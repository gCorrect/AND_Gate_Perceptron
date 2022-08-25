import numpy as np
from libraries.print import *

def weights(dim):
    weights = np.random.rand(dim)
    print_var(weights, "weights (random before training) - bias = 1")
    return weights
def step_function(x):
    if x<0:
        return 0
    else:
        return 1
def update_weights(x,w,n,error,d):
    for index, value in enumerate(x):
        w[index] += n * error * value 
    d += n*error
    # print("-------------------Start Update Weights")
    # print("w \n",w)
    # print("d \n",d)
    # print("-------------------End Update Weights")
   
    return w,d,#wList    
def train(training_set,w):
    print_title("Function: train()") # ->libraries.print.py
    def init_variables():
        n = .2
        epoch = 30
        b = 0
        iterations = 0
        wList = []
        indexWList = -1
        e = 0
        return n, epoch, b, iterations, wList, indexWList, e 
    n, epoch, b, iterations, wList, indexWList, e  = init_variables()
    # Training
    for i in range(epoch):
        iterations=0
        for x, eo in training_set:
            u = sum(x*w) + b
            error = eo[0] - step_function(u) 
            iterations+=1                        
            if (error): 
                w,b = update_weights(x,w,n,error,b)  
                weights = w
                wb = np.append(weights,b) 
                wList.append(wb)
                indexWList+=1
        if (indexWList>1): # Calculate e
            e = wList[indexWList-1] - wList[indexWList-2]
            # print("e: ",e)
            # print ("differnce distance",e[0]**2 + e[1]**2 + e[2]**2)
    # print("InexWList: ", indexWList)
    # for wd in wList:
        # print("wd: ", wd )
    def print_train_values():
        print_array(training_set,"training_set")
        print_var(iterations,"iterations: " )
        print_var(w,"weigths (after training)")
        print_var(b,"bias (after training)")
    print_train_values() 
    return w,b        
# 3D---------------------------------------------------------------------------------
def train_3d(training_set,w):
    print_title("Function: train_3d()") # ->libraries.print.py
    def init_variables():
        n = .1
        epoch = 1015
        d = 0
        iterations = 0
        return  n, epoch, d, iterations
    n, epoch, d, iterations = init_variables()
    # Training
    for i in range(epoch):
        for x, eo in training_set:
            u = sum(x*w) + d
            error = eo[0] - step_function(u) 
            iterations+=1                        
            if (error): 
                w,d=    update_weights(x,w,n,error,d)
    def print3DTrainValues():
        print("---------------------------") 
        print(" Training Function values: \n")
        print("training_set: \n",training_set)
        print("iterations: ", iterations)
        print("u :", u)
        print("step_function :", step_function(u))
        print("eo[0] :", eo)
        print("error :", error)
        print("w \n",w)
        print("d \n",d)
        print("---------------------------")
    print3DTrainValues() 
    return w,d        


# def initTrainingVariables(training_set):
#     x1 = [training_set[i][0][0] for i in range(len(training_set))]
#     x2 = [training_set[i][0][1] for i in range(len(training_set))]
#     y = [training_set[i][1] for i in range(len(training_set))]
#     print("x1 \n" , x1)
#     print("x2 \n" , x2)
#     print("y \n" , y)
#     return x1,x2,y
