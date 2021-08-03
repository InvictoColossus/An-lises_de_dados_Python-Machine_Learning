Análises Preliminar

dfClientes.isnull().sum()
dfClientes[dfClientes.isnull().T.any()]
dfClientes.sexo.unique()
dfVendas[dfVendas.id_produto == 10].count()

