                   Dados Nulos
dfClientes.loc[dfClientes.nome.isnull(),'nome']='Sem Nome'
dfClientes.loc[dfClientes.sexo.isnull(),'sexo']='O'
dfClientes.loc[dfClientes.dt_nasc.isnull(),'dt_nasc']='1/1/2020'
                   Outliers
dfProdutos.loc[9,'valor']=dfProdutos.valor[9]/10000
                   Consistência
dfVendas[~dfVendas.id_cliente.isin(dfClientes.id)]
dfVendas[dfVendas.id_loja.isin(dfLojas.id)]
dfVendas[~dfVendas.id_produto.isin(dfProdutos.id)]

dfVendas[~dfVendas.id.isin(dfPagamentos.id_venda)].count()
                   DadosDuplicados
dfClientes[dfClientes.nome.duplicated()]
dfClientes.drop('id',axis=1).duplicated().sum()
dfVendas[(dfVendas.id_cliente ==559)&(dfVendas.id_loja==2)&(dfVendas.id_produto==5)]
                   Formato de Dados
dfClientes.dt_nasc = pd.to_datetime(dfClientes.dt_nasc, format = '%m/%d/%Y')
                   Indexes
dfClientes=dfClientes.set_index('id')
dfLojas=dfLojas.set_index('id')
dfProdutos=dfProdutos.set_index('id')
dfVendas=dfVendas.set_index('id')
dfPagamentos=dfPagamentos.set_index('id')


