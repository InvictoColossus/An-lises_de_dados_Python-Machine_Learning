                        RECEITA COMBINANDO PRODUTO E LOJA
graf_dados=pd.DataFrame(columns=('loja','produto','receita'))
for cidade in dfLojas.cidade:
    for produto in dfProdutos.produto:
        graf_dados = graf_dados.append({
            'loja': cidade,
            'produto': produto,
            'receita': df.produto_valor[(df.lojas_cidade==cidade) & (df.produto_produto==produto)].sum()
        },ignore_index=True)
       
graf_dados

import seaborn as sns
graf_dados=graf_dados.pivot_table(index='loja',columns='produto',values='receita',aggfunc='sum')
sns.heatmap(graf_dados)                  
