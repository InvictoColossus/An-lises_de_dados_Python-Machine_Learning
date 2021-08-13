                     Mapa de Calor de inadiplência
graf_dados=df.pivot_table(index='produto_produto',columns='lojas_cidade',values='pg',aggfunc='mean')
sns.heatmap(graf_dados,annot=True)
plt.show

graf_dados=df.pivot_table(index='produto_produto',columns='cliente_idade',values='pg',aggfunc='mean')
sns.heatmap(graf_dados)
plt.show


                   

