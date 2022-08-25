from statistics import variance
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from libraries.load import load_feats_values, load3DPlotData 
# 2D------------------------------------------------------------------
# Plot
  # Graphics Details : Define font, x,y axis labels, title etc.   
def graph_details(): 
  font = {'family': 'serif',
          'color':  'darkred',
          'weight': 'normal',
          'size': 16,
          }
  plt.xlabel('X',fontdict=font)
  plt.ylabel('Y',fontdict=font)
  plt.title('--> Dataset2D <--',fontdict=font)
  # Data Points : Plots feature values
def plot_data(x1,y1,x2,y2):
  plt.scatter(x1,y1)
  plt.scatter(x2,y2)
  # Decision Boundary : Plots a line  
def plot_decision_boundary(slope,intercept,start,end):
  # graph_details()
  x = np.linspace(start,end,100)
  y= slope*x + intercept # ALT w[2]*x2 = w[1]*x1+w[0]
  plt.plot(x, y)
  # Trained Data : Plots feature values and decision boundary
def plot_trained_data(tablename, weights, bias):
  # data
  c1_x1, c1_x2, c2_x1, c2_x2 = load_feats_values(tablename=tablename) # -> libraries.load.py
    # Decision boundary
  slope = -weights[0]/weights[1]
  intercept = -bias / weights[1]
  plot_decision_boundary(slope=slope, intercept=intercept,start=0,end=1.5)
  plot_data(c1_x1, c1_x2, c2_x1, c2_x2)
  graph_details()
  plt.show()

# 3D------------------------------------------------------------------
# Plot
  # Data Points  
def plot3DData(x1,y1,z1,x2,y2,z2):
  fig = plt.figure(figsize = (10, 10))
  ax = plt.axes(projection ="3d")

  ax.scatter3D(x1, y1, z1, color = "blue")
  ax.scatter3D(x2, y2, z2, color = "red")

  # Graphics Details  
  font = {'family': 'serif',
          'color':  'darkred',
          'weight': 'normal',
          'size': 16,
          }
  plt.xlabel('X',fontdict=font)
  plt.ylabel('Y',fontdict=font)
  ax.set_zlabel('Z',fontdict=font)
  # plt.zlabel('Z',fontdict=font)
  plt.title('--> Dataset3D <--',fontdict=font)
  plt.show
  # Decision Plane
def plot3DDecisionBoundary(x1, y1, z1,x2, y2, z2,w,d):
  fig = plt.figure(figsize = (10, 10))
  # syntax for 3-D projection
  ax = plt.axes(projection ='3d')
  # variables
  a = w[0]
  b = w[1]
  c = w[2]
  d = d
  # create x,y
  x = np.linspace(min(x1),max(x2),10)
  y = np.linspace(min(y1),max(y2),10)
  xx, yy = np.meshgrid(x, y)
  # calculate corresponding z
  z = ( -a * xx -b * yy - d) / c
  # Plot data + decision plane
  ax.plot_surface(xx, yy, z, alpha=0.9)
  ax.scatter3D(x1, y1, z1, color = "blue")
  ax.scatter3D(x2, y2, z2, color = "red")
  # Graphics Details  
  font = {'family': 'serif',
          'color':  'darkred',
          'weight': 'normal',
          'size': 16,
          }
  plt.xlabel('X',fontdict=font)
  plt.ylabel('Y',fontdict=font)
  ax.set_zlabel('Z',fontdict=font)
  # plt.zlabel('Z',fontdict=font)
  plt.title('--> Dataset3D <--',fontdict=font)
  plt.show()
  def printValues():
    print("xx: \n", xx)
    print("yy: \n", yy)
    print("z: \n", z)

def plotPlane():
  fig = plt.figure(figsize = (10, 10))
  # syntax for 3-D projection
  ax = plt.axes(projection ='3d')
  # variables
  a = 2
  b = 2
  c = 1
  d = 2
  # create x,y
  x = np.linspace(0,1,6)
  y = np.linspace(0,1,6)
  xx, yy = np.meshgrid(x, y)
  # calculate corresponding z
  z = (-a * xx -b * yy - d) / c
  # z = -( a * xx + b * yy + d) / c
  # Plot decision plane
  ax.plot_surface(xx, yy, z, alpha=0.9)
  # Graphics Details  
  font = {'family': 'serif',
          'color':  'darkred',
          'weight': 'normal',
          'size': 16,
          }
  plt.xlabel('X',fontdict=font)
  plt.ylabel('Y',fontdict=font)
  ax.set_zlabel('Z',fontdict=font)
  plt.title('--> 3D Plane <--',fontdict=font)
  plt.show()
    
# ax.plot3D(x, y, z, 'green')
# z = ( -a * x -b * y - d) * 1. /c

#   # Trained Data
# def plot3DTrainedData(tablename, w):
#   # data
#   x1,y1,z1,x2,y2,z2 = load3Dplot_data(tablename=tablename)
#   plot3DData(x1,y1,z1,x2,y2,z2)
#     #line
#   # b = 1
#   # a = [0,-b/w[1]]
#   # c = [-b/w[0],0]
#   # plt.plot(a,c)
#   plt.show()
