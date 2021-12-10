# bar chart and pandas
import pandas as pd


colors = ["#006D2C", "#31A354","#74C476"]

# just dataframe
data = [[15, 10], [30, 15], [40, 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
df.plot.bar(stacked=True, color=colors, figsize=(10,7))

df = pd.read_excel(r"D:\Documents\python\repo\Introduction_Python\2_Data_and_Control_Flow\data\data.xlsx")
df[['age', 'yearsInCompany','salary']].plot.bar(stacked=True)


# yet another
data = [[2000, 2000, 2000, 2001, 2001, 2001, 2002, 2002, 2002],
        ['Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar', 'Jan', 'Feb', 'Mar'],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]]

rows = zip(data[0], data[1], data[2])
headers = ['Year', 'Month', 'Value']
df = pd.DataFrame(rows, columns=headers)

pivot_df = df.pivot(index='Year', columns='Month', values='Value')
pivot_df.loc[:,['Jan','Feb', 'Mar']].plot.bar(stacked=True, color=colors, figsize=(10,7))