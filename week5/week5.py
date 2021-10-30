# 5w

# Matplotlib, plotly, seaborn, dash (Web?)


# # Matplotlib

# # Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Web rendering, see plotly
# import matplotlib
# matplotlib.use('WebAgg')

# Sine
x = np.arange(0,4*np.pi,0.1)   
y = np.sin(x)

plt.plot(x,y)
plt.show()

# Sine and cosine
z = np.cos(x)
plt.plot(x,y,x,z)

# Sine and cosine
z = np.cos(x)
plt.plot(x,y,'b*',x,z,'k--')

# Description components
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])      
plt.grid(True)
# plt.show()

# + plt.text
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.text(1, 0.5, r'x=1,y=0.5')
plt.legend(['sin(x)', 'cos(x)'])      # legend entries as seperate strings in a list
plt.grid(True)
# plt.show()


# object
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0, 4.5)
plt.show()

# matlab way
fig = plt.figure()
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0, 4.5)
plt.show()


# Subplots
# Initialize the plot
fig = plt.figure()
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

# concise way
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax2.fill()
ax1.axvline(0.65)
ax3.scatter(x,y)



# Example charts from "Python Data Science Handbook" by Jake VanderPlas
# https://jakevdp.github.io/PythonDataScienceHandbook/

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


from sklearn.datasets import make_blobs
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu');



from sklearn.datasets import make_blobs
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)

fig, ax = plt.subplots()

ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
ax.set_title('Naive Bayes Model', size=14)

xlim = (-8, 8)
ylim = (-15, 5)

xg = np.linspace(xlim[0], xlim[1], 60)
yg = np.linspace(ylim[0], ylim[1], 40)
xx, yy = np.meshgrid(xg, yg)
Xgrid = np.vstack([xx.ravel(), yy.ravel()]).T

for label, color in enumerate(['red', 'blue']):
    mask = (y == label)
    mu, std = X[mask].mean(0), X[mask].std(0)
    P = np.exp(-0.5 * (Xgrid - mu) ** 2 / std ** 2).prod(1)
    Pm = np.ma.masked_array(P, P < 0.03)
    ax.pcolorfast(xg, yg, Pm.reshape(xx.shape), alpha=0.5,
                  cmap=color.title() + 's')
    ax.contour(xx, yy, P.reshape(xx.shape),
                levels=[0.01, 0.1, 0.5, 0.9],
                colors=color, alpha=0.2)
    
ax.set(xlim=xlim, ylim=ylim)

fig.savefig('figures/05.05-gaussian-NB.png')




from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
data.target_names

categories = ['talk.religion.misc', 'soc.religion.christian',
              'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)
labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');




# bar chart and pandas
import pandas as pd


colors = ["#006D2C", "#31A354","#74C476"]
data = [[2000, 2000, 2000, 2001, 2001, 2001, 2002, 2002, 2002],
        ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]]

rows = zip(data[0], data[1], data[2])
headers = ['Year', 'Month', 'Value']
df = pd.DataFrame(rows, columns=headers)

pivot_df = df.pivot(index='Year', columns='Month', values='Value')
pivot_df.loc[:,['Jan','Feb', 'Mar']].plot.bar(stacked=True, color=colors, figsize=(10,7))


# just dataframe
data = [[15, 10], [30, 15], [40, 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
df.plot.bar(stacked=True, color=colors, figsize=(10,7))





import plotly.express as px
fig = px.histogram(views, x="views")
fig.show()




# plotly 
import plotly.io as pio
pio.renderers.default='browser'

import plotly.express as px
 
# Data to be plotted
df = px.data.iris()
 
# Plotting the figure
fig = px.scatter_3d(df, x = 'sepal_width',
                    y = 'sepal_length',
                    z = 'petal_width',
                    color = 'species')
 
fig.show()


import plotly.graph_objects as px
import numpy as np
 
 
# creating random data through randomint
# function of numpy.random
np.random.seed(42)
 
# Data to be Plotted
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)
 
plot = px.Figure(data=[px.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',)
])
 
# Add dropdown
plot.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]
)
 
plot.show()



import plotly.graph_objects as px
import plotly.express as go
import numpy as np
 
df = go.data.tips()
 
x = df['total_bill']
y = df['day']
 
plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='lines',)
])
 
plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
 
plot.show()



# Seaborn 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")


sns.regplot(x="total_bill", y="tip", data=tips);
plt.show()


# 3D plot


import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()



# bokeh
# dash

https://github.com/bokeh/bokeh/tree/branch-3.0/examples/app

# dashboard example
https://github.com/bokeh/bokeh/tree/branch-3.0/examples/app/dash







# https://www.machinelearningplus.com/plots/matplotlib-tutorial-complete-guide-python-plot-examples/
# https://www.w3schools.com/python/matplotlib_intro.asp
# https://matplotlib.org/stable/tutorials/index.html

# https://www.activestate.com/blog/plotting-data-in-python-matplotlib-vs-plotly/
# https://towardsdatascience.com/matplotlib-vs-plotly-express-which-one-is-the-best-library-for-data-visualization-7a96dbe3ff09
# https://towardsdatascience.com/matplotlib-vs-seaborn-vs-plotly-f2b79f5bddb



# # Plotly tutorial
# https://plotly.com/python/
# https://www.kaggle.com/kanncaa1/plotly-tutorial-for-beginners
# https://www.geeksforgeeks.org/python-plotly-tutorial/
# https://neptune.ai/blog/plotly-python-tutorial-for-machine-learning-specialists


# https://pauliacomi.com/2020/06/07/plotly-v-bokeh.html

# # scatter, bar, histogram, line, subplots, legend, axis label, title, markers, 


# Bokeh
# Dash