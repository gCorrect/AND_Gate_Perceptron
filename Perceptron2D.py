from libraries.loaddata import loadTupleData, loadPlotData 
from libraries.train import weights,train
from libraries.plot import plotTrainedData, plotdata,plotDecisionBoundary,plt
print("-----------------------------------------------------------------------------------")
# variables
w = weights(2)
tablename= "dataset2d"
#Plot (before training)
plotTrainedData(tablename, w=w)
# Training
w, b = train(loadTupleData(tablename=tablename), w=w)
print("-----------------------------------------------------------------------------------")
#Plot
  # Decision boundary
slope = -w[0]/w[1]
intercept = -b / w[1]
plotDecisionBoundary(slope=slope, intercept=intercept,start=0,end=1.5)
  # data
x1,y1,x2,y2 = loadPlotData(tablename=tablename)
plotdata(x1,y1,x2,y2)
plt.show()
   
