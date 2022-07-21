import matplotlib.pyplot as plt
import numpy as np
# Plot
  # Data Points  
def plotdata(x1,y1,x2,y2):
  plt.scatter(x1,y1)
  plt.scatter(x2,y2)
  # Line
def plotline(slope,intercept,start,end):
  x = np.linspace(start,end,100)
  y=slope*x + intercept # ALT w[2]*x2 = w[1]*x1+w[0]
  plt.plot(x, y)
  # Graphics Details  
  font = {'family': 'serif',
          'color':  'darkred',
          'weight': 'normal',
          'size': 16,
          }
  plt.xlabel('X',fontdict=font)
  plt.ylabel('Y',fontdict=font)
  plt.title('--> Dataset2D <--',fontdict=font)


