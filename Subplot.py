                      SUBPLOT
plt.figure(figsize = (10,7))

plt.subplot(2,2,1)
graf_dados=df.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Vendas por Loja')
plt.xticks(rotation=90)

plt.subplot(2,2,2)
graf_dados=df.groupby('produto_produto').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Produtos que mais Vendem')
plt.xticks(rotation=90)

plt.subplot(2,2,3)
graf_dados = df[['lojas_cidade','produto_valor']].groupby('lojas_cidade').sum().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Receita por Loja')
plt.xticks(rotation=90)

plt.subplot(2,2,4)
graf_dados=df[['produto_produto','produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.xticks(rotation=90)
plt.title('Receitas por Produto')
plt.tight_layout()                      
                     
