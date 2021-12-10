## Matplotlib

# Import
import matplotlib.pyplot as plt
import numpy as np

# Sine
x = np.arange(0,4*np.pi,0.1)   
y = np.sin(x)
plt.plot(x,y)
plt.show()
plt.savefig('foo.png')

# Sine and cosine
z = np.cos(x)
plt.plot(x,y,x,z)

# Sine and cosine
z = np.cos(x)
plt.plot(x,y,x,z)
plt.plot(x,y,'b*',x,z,'k--')

# color coding
plt.plot(x,z,color=np.array([204, 99, 18])/255) # RGB
plt.plot(x,y,color='#5b0de0')                   # HEX


# Description components
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi', fontsize=20,fontweight="bold")
plt.legend(['sin(x)', 'cos(x)'])      
plt.grid(True)
# plt.show()

# + plt.text
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.text(1, 0.5, r'$x=1,y=0.5\ \beta $')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.grid(True)
# plt.show()

# 2 different ways of plotting in Matplotlib
# object way
fig = plt.figure()
ax = fig.add_subplot(111) # ax, axes
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0, 4.5)
plt.show()

# matlab way
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0, 4.5)
plt.show()


# Subplots
# Initialize the plot
fig = plt.figure()
fig.suptitle("Super title")
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax2.fill()
ax1.axvline(0.65)
ax3.scatter(x,y)
ax3.set_title('Ax3 title')


# concise way
figure, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
figure.suptitle("Super title")
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax2.fill()
ax1.axvline(0.65)
ax3.scatter(x,y)


# Web rendering, see plotly
import matplotlib
matplotlib.use('WebAgg')
plt.show()