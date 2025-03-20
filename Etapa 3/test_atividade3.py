import pytest
import pandas as pd
from utils import carregar_dados_json, filtrar_usuarios, ordenar_usuarios, gerar_relatorio_dic

def test_carregar_dados_json():
	df = carregar_dados_json('usuarios.json')
	print("DataFrame usuarios:")
	print(df)
	assert list(df.columns) == ['id', 'nome', 'idade']
	assert len(df) == 4

def test_filtrar_usuarios():
	df_dados_usuarios = carregar_dados_json('usuarios.json')
	df_filtrado = filtrar_usuarios(df_dados_usuarios)
	print("DataFrame df_filtrado:")
	print(df_filtrado)
	assert len(df_filtrado) == 2
	assert all(df_filtrado['idade'] > 18)

def test_orderar_usuarios():
	df_dados_usuarios = carregar_dados_json('usuarios.json')
	df_ordernado = ordenar_usuarios(df_dados_usuarios)
	print("DataFrame df_ordernado:")
	print(df_ordernado)
	assert df_ordernado.iloc[0]['nome'] == 'Daniel'
	assert df_ordernado.iloc[-1]['nome'] == 'Carla'

def test_gerar_relatorio_dic():
	df_dados_usuarios = carregar_dados_json('usuarios.json')
	df_filtrado = filtrar_usuarios(df_dados_usuarios)
	df_ordernado = ordenar_usuarios(df_filtrado)
	relatorio = gerar_relatorio_dic(df_ordernado)
	print("DataFrame relatorio:")
	print(relatorio)
	assert isinstance(relatorio, list)
	assert isinstance(relatorio[0], dict)
	assert relatorio[0]['nome'] == 'Alice'
	
