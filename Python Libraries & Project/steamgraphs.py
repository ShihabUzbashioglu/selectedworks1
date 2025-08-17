import matplotlib.pyplot as plt
import numpy as np

x= np.linespace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.stackplot(x,y1,y2,baseline='wiggle')
plt.title('streamgraphs')
plt.show()