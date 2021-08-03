import pandas as pd

dfClientes = pd.read_excel('caso_estudo.xlsx',sheet_name ='clientes')
dfLojas = pd.read_excel('caso_estudo.xlsx',sheet_name ='lojas')
dfProdutos = pd.read_excel('caso_estudo.xlsx',sheet_name ='produtos')
dfVendas = pd.read_excel('caso_estudo.xlsx',sheet_name ='vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx',sheet_name ='pagamentos')
