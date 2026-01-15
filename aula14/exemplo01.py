import pandas as pd
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
print(df_planilha_custos[['Produto', 'Custo Total (R$)']].head())

total_custos = df_planilha_custos['Custo Total (R$)'].sum()
media_custos = df_planilha_custos['Custo Total (R$)'].mean()
menor_custos = df_planilha_custos['Custo Total (R$)'].min()
maior_custos = df_planilha_custos['Custo Total (R$)'].max()

print(40*"=")
print('\nResumo: (R$)')
print(f'Total: {total_custos}')
print(f'Média de Custo: {media_custos}')
print(f'Menor Custo: {menor_custos}')
print(f'Maior Custo: {maior_custos}')
