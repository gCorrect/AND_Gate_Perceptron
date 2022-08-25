from libraries.load import load_tuple_data 
from libraries.train import weights,train
from libraries.plot import plot_trained_data, plot_data,plot_decision_boundary
print("-----------------------------------------------------------------------------------")
# variables
w = weights(2) # -> libraries.train.py
bias = 1
tablename = "dataset2d"
#Plot (before training ** weights are random, bias = 1)
plot_trained_data(tablename = tablename, weights = w, bias = bias) # ->libraries.plot.py
# Training
w, b = train(load_tuple_data(tablename = tablename), w = w) # -> libraries.train.py 
print("-----------------------------------------------------------------------------------")
#Plot (after training)
plot_trained_data(tablename = tablename, weights = w, bias = b) # ->libraries.plot.py
