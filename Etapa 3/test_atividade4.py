import pytest
import pandas as pd
from utils import carregar_dados, realizar_agregacoes, salvar_dados_parquet, carregar_dados_parquet

def test_carregar_dados():
	df = carregar_dados('dados_agregacao.csv')
	assert list(df.columns) == ['id', 'categoria','valor']
	assert len(df) == 6

def test_realizar_agregacoes():
	df = carregar_dados('dados_agregacao.csv')
	df_agregado = realizar_agregacoes(df)
	assert list(df_agregado.columns) == ['categoria','soma_valor','media_valor']
	assert df_agregado.loc[df_agregado['categoria'] == 'A', 'soma_valor'].values[0] == 450
	assert df_agregado.loc[df_agregado['categoria'] == 'A', 'media_valor'].values[0] == 150

def test_salvar_e_carregar_parquet():
	df = carregar_dados('dados_agregacao.csv')
	df_agregado = realizar_agregacoes(df)
	salvar_dados_parquet(df_agregado, 'dados_agregacao.parquet')
	df_carregado = carregar_dados_parquet('dados_agregacao.parquet')
	pd.testing.assert_frame_equal(df_agregado, df_carregado)