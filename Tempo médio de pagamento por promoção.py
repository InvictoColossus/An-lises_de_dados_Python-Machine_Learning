                  TEMPO MÉDIO DE PAGAMENTO POR PROMOÇÃO
dfPromo=pd.read_csv('caso_estudo_venda_promocao.csv',sep=";")
dfPromo=dfPromo.set_index('id_venda')
df=df.join(dfPromo)
df

graf_dados=df[['promoção','tempo_pg']][[~df.tempo.isnull()]]
graf_dados.groupby('promoção').boxplot(column=['tempo_pg'])
plt.show

sns.histplot(data=graf_dados.tempo_pg[graf_dados['promoção']==0],kde=True)
plt.title('Tempo médio de pagamento para casos sem promoção')
plt.show

sns.histplot(data=graf_dados.tempo_pg[graf_dados['promoção']==1],kde=True)
plt.title('Tempo médio de pagamento para casos com promoção')
plt.show

