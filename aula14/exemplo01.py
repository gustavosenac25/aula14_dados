import pandas as pd
import numpy as np
import os

os.system('cls')
df_planilha_custos = pd.read_csv('./aula14/planilha_de_custos.csv') #como a planilha_de_custos.csv está dentro de uma pasta (no caso da aula14), tem que colocar o endereço completo com ./
# print(df_planilha_custos)

df_planilha_custos['Custo Total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] +
    (df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)']) / 100 +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
).round(2)

#print(df_planilha_custos.head())
# print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head())

# total_custos = df_planilha_custos['Custo Total (R$)'].sum()
# media_custos = df_planilha_custos['Custo Total (R$)'].mean()
# menor_custos = df_planilha_custos['Custo Total (R$)'].min()
# maior_custos = df_planilha_custos['Custo Total (R$)'].max()

# print(40*"=")
# print('\nResumo: (R$)')
# print(f'Total: {total_custos}')
# print(f'Média de Custo: {media_custos}')
# print(f'Menor Custo: {menor_custos}')
# print(f'Maior Custo: {maior_custos}')

#---------------- Medidas estatísticas - Biblioteca Numpy
array_custo_total = np.array(df_planilha_custos['Custo Total (R$)']) #array transforma em uma lista os números da tabela
# print(array_custo_total)

media = np.mean(array_custo_total)
mediana = np.median(array_custo_total) #50% dos produtos têm um custo menor que isso, 50% dos produtos têm um custo maior que esse

#Calculando Quartis
q1 = np.quantile(array_custo_total, 0.25) #25% dos produtos tem um custo de até isso e 75%$ custam mais que isso
q2 = np.quantile(array_custo_total, 0.50) #50% dos produtos tem um custo de até isso e 50%$ custam mais que isso
q3 = np.quantile(array_custo_total, 0.75) #75% dos produtos tem um custo de até isso e 25%$ custam mais que isso

df_maiores = df_planilha_custos[df_planilha_custos ['Custo Total (R$)'] > q3]

print(40*'-')
print('\nMedidas Estatísticas:')
print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(df_maiores)