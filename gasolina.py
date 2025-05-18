import seaborn as sns
import pandas as pd

data = pd.read_csv('gasolina.csv')

gasolina = data[['dia', 'venda']].groupby('dia').mean().reset_index()

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina, x='dia', y='venda')
  grafico.set_title('Preço médio da gasolina', fontsize = 10, fontweight = 'bold')
  grafico.set_xlabel('Dia', fontsize = 10)
  grafico.set_ylabel('Preço', fontsize = 10)
 
  grafico.figure.savefig('gasolina.png')