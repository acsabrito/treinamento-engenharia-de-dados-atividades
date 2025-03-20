import pytest
import pandas as pd
from utils import carregar_dados, calcular_valor_total, filtrar_vendas, salvar_resultado
# Testes Unitários

@pytest.fixture
def dados_vendas():
	# Configuração inicial para os testes
	dados_vendas = pd.DataFrame({
		'produto':['Produto A', 'Produto B', 'Produto C', 'Produto D'],
		'quantidade': [10,5,8,12],
		'preco_unitario': [50.0, 150.0,80.0, 30.0]
	})
	return dados_vendas
	
def test_carregar_dados():
	df = carregar_dados('vendas.csv')
	assert list(df.columns) == ['produto', 'quantidade','preco_unitario']
	
def test_calcular_valor_total(dados_vendas):
	df = calcular_valor_total(dados_vendas)
	assert 'valor_total' in df.columns
	assert df.loc[0,'valor_total'] == 500.0
	
def test_filtrar_vendas(dados_vendas):
	df = calcular_valor_total(dados_vendas)
	df_filtrado = filtrar_vendas(df)
	assert len(df_filtrado) == 2
	assert all(df_filtrado['valor_total'] > 500)
	
def test_salvar_resultado(dados_vendas):
	df = calcular_valor_total(dados_vendas)
	df_filtrado = filtrar_vendas(df)
	salvar_resultado(df_filtrado, 'resultado.csv')
	df_resultado = pd.read_csv('resultado.csv')
	assert len(df_resultado) == 2
	assert 'valor_total' in df_resultado.columns