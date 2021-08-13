                   Análises de Vendas e Receitas
                   Lojas e produtos que mais vendem
graf_dados=df.groupby('lojas_cidade').count().produto_valor.sort_values(ascending=False)
graf_dados

import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Vendas por Loja')
                    Produtos que mais vendem
graf_dados=df.groupby('produto_produto').count().produto_valor.sort_values(ascending=False)

plt.figure(figsize=(15,5))
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Produtos que mais Vendem')
                     Receita por Loja
graf_dados = df[['lojas_cidade','produto_valor']].groupby('lojas_cidade').sum().produto_valor.sort_values(ascending=False)
graf_dados

plt.figure(figsize=(15,5))
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Receita por Loja')
print('O maior valor é %i sendo %.2f vezes a média dos demais,que é %i' % (graf_dados.max(),graf_dados.max()/graf_dados[graf_dados != graf_dados.max()].mean(),graf_dados[graf_dados != graf_dados.max()].mean()))
                     Receita por Produto
graf_dados=df[['produto_produto','produto_valor']].groupby('produto_produto').sum().produto_valor.sort_values(ascending=False)

plt.figure(figsize=(15,5))
plt.bar(graf_dados.index,graf_dados.values)
plt.title('Receitas por Produto')
                     
