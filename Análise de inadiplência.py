                 Análise de Inadiplência
                Inadiplência por loja
plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
graf_dados=df[df.pg==0].groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('inadiplência por loja')
plt.xticks(rotation=90)


plt.subplot(1,2,2)
graf_dados=df.groupby('lojas_cidade').mean().pg.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Porcentagem de pagamento por loja')
plt.xticks(rotation=90)

plt.show

                   Inadiplência por produto
plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
graf_dados=df[df.pg==0].groupby('produto_produto').count().produto_valor.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('inadiplência por produto')
plt.xticks(rotation=90)

plt.subplot(1,2,2)
graf_dados=df.groupby('produto_produto').mean().pg.sort_values(ascending=False)
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Porcentagem de Pagamento por Produto')
plt.xticks(rotation=90)


plt.show

                   Inadiplência por Idade
graf_dados=df[['cliente_idade','pg']].groupby('cliente_idade').mean().sort_values('cliente_idade')
graf_dados.plot()


                   

