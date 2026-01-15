import pandas as pd
import os

os.system('cls')

df_planilha_moveis = pd.read_csv('./aula14/planilha_moveis.csv')

df_planilha_moveis['Valor Total'] = (
    df_planilha_moveis['Vendidos'] *
    df_planilha_moveis['Preco']
).round(2)

print(df_planilha_moveis[['Produto', 'Valor Total']])

total_vendas = df_planilha_moveis['Valor Total'].sum()
media_vendas = df_planilha_moveis['Valor Total'].mean()
menor_vendas = df_planilha_moveis['Valor Total'].min()
maior_vendas = df_planilha_moveis['Valor Total'].max()

print(40*'-')
print('\nResumo:')
print(f'Total vendido: {total_vendas} R$')
print(f'Média das vendas: {media_vendas} R$')
print(f'Menor valor de venda: {menor_vendas} R$')
print(f'Maior valor de venda: {maior_vendas} R$')
