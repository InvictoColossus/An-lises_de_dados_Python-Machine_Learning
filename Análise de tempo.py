                    ANÁLISE DE TEMPO
                  TEMPO MÉDIO DE PAGAMENTO
df.tempo_pg.mean()
plt.boxplot('tempo_pg')
plt.title('Tempo de Pagamento')

sns.histplot(data=df.tempo_pg,kde=True)
plt.title('Histograma para tempo de pagamento')
                  TEMPO DE PAGAMENTO POR CIDADE E PRODUTO
df.groupby('lojas_cidade').mean().tempo_pg                  

plt.figure(figsize=(7,4))
df[['lojas_cidade','tempo_pg']].groupby('lojas_cidade').boxplot('tempo_pg')
plt.title('Boxplot para tempo de pagamento por cidade')
plt.xticks(rotation=90)
plt.show

df.groupby('produto_produto').mean().tempo_pg

plt.figure(figsize=(7,4))
df[['produto_produto','tempo_pg']].groupby('produto_produto').boxplot('tempo_pg')
plt.title('Boxplot para tempo de pagamento por produto')
plt.xticks(rotation=90)
plt.show
