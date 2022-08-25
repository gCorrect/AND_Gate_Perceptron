from libraries.train import weights, train_3d
from libraries.load import load3DPlotData, load3DTupleData
from libraries.plot import *
# variables
w = weights(3) # ->libraries.train.py
tablename= "dataset3d"
# Plot
  # data
x1,y1,z1,x2,y2,z2 = load3DPlotData(tablename=tablename)  
plot3DData(x1,y1,z1,x2,y2,z2)
plt.show()

plot3DDecisionBoundary(x1,y1,z1,x2,y2,z2, w, d = 1)

# Training
w, d = train_3d(load3DTupleData(tablename=tablename), w=w)
print("w",w)
print("d",d)
# Plot
  # Decision boundary
plot3DDecisionBoundary(x1,y1,z1,x2,y2,z2, w, d = d)
# plotPlane()
print("-----------------------------------------------------------------------------------")
