                    SAZONALIDADE
plt.figure(figsize=(10,5))
graf_dados = df[['produto_valor','dt_venda']].groupby('dt_venda').sum().rolling(30).mean()
plt.plot(graf_dados.index,graf_dados.values)
plt.title('Média Móvel (30)dias de Receita')
plt.show

fig,ax=plt.subplots(figsize=(10,5))
graf_dados=df[['produto_valor','lojas_cidade','dt_venda']].groupby(['dt_venda','lojas_cidade']).sum.rolling(30).
