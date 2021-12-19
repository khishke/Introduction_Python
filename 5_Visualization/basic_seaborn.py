# Seaborn 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips") # https://www.angela1c.com/projects/tips-project-files/part1/


sns.regplot(x="total_bill", y="tip", data=tips);
plt.show()

# gapminder - pip install gapminder
from gapminder import gapminder # data set

# data
data = gapminder.loc[gapminder.year == 2007]
dataAll = gapminder
dataChina = gapminder.loc[gapminder.country == 'China']

# use the scatterplot function to build the bubble map
sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, sizes=(20, 2000))

sns.scatterplot(data=dataAll, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'country', sizes=(20, 2000))
plt.show()

sns.scatterplot(data=dataChina, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'year', palette='colorblind', sizes=(20, 2000))
plt.show()

