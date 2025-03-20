import pytest
import pandas as pd
from utils import calcular_media, identificar_aprovados, gerar_relatorio

# Testes Unitários

@pytest.fixture
def dados_aluno():
	# Configuração inicial para os testes
	dados_aluno = pd.DataFrame({
		'aluno': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
		'nota1': [8.0, 6.0, 7.5, 9.0],
		'nota2': [7.0, 5.5, 8.0, 9.5],
		'nota3': [9.0, 6.5, 7.0, 8.5]
	})
	return dados_aluno
			
def test_calcular_media():
	df_dados_aluno = pd.read_csv('alunos.csv')
	df_media = calcular_media(df_dados_aluno)
	assert 'media' in df_media.columns
	assert df_media.loc[0, 'media'] == 8.0
	assert df_media.loc[1, 'media'] == 6.0
			
def test_identificar_aprovados(dados_aluno):
	df_media = calcular_media(dados_aluno)
	df_aprovados = identificar_aprovados(df_media)
	assert len(df_aprovados) == 3
	assert all(df_aprovados['media'] >= 7)
		
def test_gerar_relatorio(dados_aluno):
	df_media = calcular_media(dados_aluno)
	df_relatorio = gerar_relatorio(df_media)
	assert list(df_relatorio.columns) == ['aluno','media', 'status']
	assert df_relatorio.loc[0, 'status'] == 'Aprovado'
	assert df_relatorio.loc[1, 'status'] == 'Reprovado'
