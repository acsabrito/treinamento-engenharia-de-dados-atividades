import pandas as pd
import json

""""Atividade 0"""
def fibonacci(n):
	if not isinstance(n, int) or n < 0:
		raise ValueError("O valor de n deve ser um inteiro não negativo.")
		if n == 0:
			return 0
		elif n == 1:
			return 1
		
	a, b = 0, 1
	for _ in range(2, n + 1):
		a, b = b, a + b
	return b
	
""""Geral"""	
def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
	""""Carrega os dados de um arquivo CSV e retorna um DataFrame."""
	return pd.read_csv(caminho_arquivo)

	
""""Atividade 1"""	
def calcular_valor_total(df: pd.DataFrame) -> pd.DataFrame:
	""""Adiciona uma coluna 'valor_total' ao DataFrame, calculada como quantidade * preco_unitario."""
	df['valor_total'] = df['quantidade'] * df['preco_unitario']
	return df

def filtrar_vendas(df: pd.DataFrame) -> pd.DataFrame:
	""""Filtra os registros onde o valor_total é superior a R$500."""
	return df[df['valor_total'] > 500] 

def salvar_resultado(df: pd.DataFrame, caminho_arquivo: str):
	""""Salva o DataFrame filtrado em um novo arquivo CSV."""
	df.to_csv(caminho_arquivo, index=False)
	
""""Atividade 2"""		
def calcular_media(df):
	""""Calcula a média das notas para cada aluno e adiciona uma coluna 'media'."""
	df['media'] = df[['nota1', 'nota2', 'nota3']].mean(axis=1)
	return df

def identificar_aprovados(df):
	""""Identifica os alunos com média maior ou igual a 7."""
	return df[df['media'] >= 7]

def gerar_relatorio(df):
	""""Gera um relatório com o nome do aluno, a média calculada e o status."""
	df['status'] = df['media'].apply(lambda x: 'Aprovado' if x > 6 else 'Reprovado')
	return df[['aluno', 'media', 'status']]
	
""""Atividade 3"""	
def carregar_dados_json(caminho_arquivo: str) -> pd.DataFrame:
	""""Carrega os dados de um arquivo JSON e retorna um DataFrame."""
	# Lendo o arquivo JSON para um DataFrame
	df_json = pd.read_json('usuarios.json')
	# Se o JSON estiver aninhado, pode ser necessário converter:
	df_json = pd.json_normalize(df_json['usuarios'])
	return df_json

def filtrar_usuarios(df: pd.DataFrame) -> pd.DataFrame:
	""""Filtra os usuarios com idade maior que 18 anos."""
	return df[df['idade'] > 18]
	
def ordenar_usuarios(df: pd.DataFrame) -> pd.DataFrame:
	""""Ordena os usuários por idade."""
	return df.sort_values(by='idade')

def gerar_relatorio_dic(df: pd.DataFrame) -> list:
	""""Gera um relatório final em formato de lista de dicionários."""
	return df.to_dict(orient='records')
	
""""Atividade 4"""
def realizar_agregacoes(df: pd.DataFrame) -> pd.DataFrame:
	""""Realiza agregações de soma e média dos valores por categoria."""
	agregacoes = df.groupby('categoria').agg(soma_valor=('valor', 'sum'),media_valor=('valor', 'mean')).reset_index()
	return agregacoes

def salvar_dados_parquet(df: pd.DataFrame, caminho_arquivo: str) -> pd.DataFrame:
	""""Salva o DataFrame em um arquivo parquet."""
	df.to_parquet(caminho_arquivo, index=False)

def carregar_dados_parquet(caminho_arquivo: str) -> pd.DataFrame:
	""""Carrega os dados do arquivo parquet em um DataFrame"""
	return pd.read_parquet(caminho_arquivo)