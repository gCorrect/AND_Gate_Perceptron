import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from libraries.train import weights, train3D
from libraries.loaddata import load3DPlotData, load3DTupleData
from libraries.plot import *
# variables
w = weights(3)
tablename= "dataset3d"
# Plot
  # data
x1,y1,z1,x2,y2,z2 = load3DPlotData(tablename=tablename)  
# plot3DData(x1,y1,z1,x2,y2,z2)
plt.show()
# Training
w, d = train3D(load3DTupleData(tablename=tablename), w=w)
print("w",w)
print("d",d)
# Plot
  # Decision boundary
plot3DDecisionBoundary(x1,y1,z1,x2,y2,z2, w, d = d)
# plotPlane()
print("-----------------------------------------------------------------------------------")
