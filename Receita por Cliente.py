                    RECEITA POR CLIENTE
graf_dados=df[['cliente_nome','produto_valor']].groupby('cliente_nome').sum().produto_valor.sort_values(ascending=False)
graf_dados

from matplotlib.ticker import PercentFormatter

fix,ax=plt.subplots(figsize=(15,5))
ax.plot(graf_dados.index,graf_dados.values,color='C0')
ax2 = ax.twinx()
ax2.plot(graf_dados.index,graf_dados.values.cumsum()/graf_dados.values.sum()*100,color='C1')
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.axes.get_xaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)
plt.title('Receita por Cliente')

receita_acumulada=graf_dados.cumsum()/graf_dados.sum()
receita_acumulada[receita_acumulada<0.60].count()/receita_acumulada.count()
