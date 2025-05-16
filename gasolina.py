import seaborn as sns
import pandas as pd

data = pd.read_csv('gasolina.csv')

gasolina = data[['dia', 'venda']].groupby('dia').mean().reset_index()

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina, x='dia', y='venda')
  grafico.figure.savefig('gasolina.png')