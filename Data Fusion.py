df=dfVendas.join(dfClientes.add_prefix('cliente_'),on='id_cliente')
df=df.join(dfLojas.add_prefix('lojas_'),on='id_loja')
df=df.join(dfProdutos.add_prefix('produto_'),on='id_produto')

df = df.join(dfPagamentos.set_index('id_venda'))
