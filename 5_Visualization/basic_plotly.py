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

# Drop down menu
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


# slider
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
