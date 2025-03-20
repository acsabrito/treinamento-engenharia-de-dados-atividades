/* ATIVIDADE 1 
 * Listar os nomes e cidades de todos os clientes em uma só consulta
 */
SELECT nome, cidade FROM Clientes;

/* ATIVIDADE 2 
 * Listar os pedidos com valor acima de R$100
 */
SELECT * FROM Pedidos p WHERE valor > 100;

/* ATIVIDADE 3 
 * Listar os pedidos ordenados pelo valor (decrescente)
 */
SELECT * FROM Pedidos p ORDER BY valor DESC;

/* ATIVIDADE 4 
 * Listar os 3 primeiros produtos cadastrados
 */
SELECT * FROM Produtos p ORDER BY id_produto LIMIT 3;

/* ATIVIDADE 5 
 * Listar o total de valor gasto por cada cliente em pedidos.
 */
SELECT c.id_cliente, c.nome, sum(valor) AS valorTotal 
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente
  GROUP BY c.id_cliente, c.nome;

/* ATIVIDADE 6
 * Encontrar o cliente com o maior valor gasto
 */
SELECT p.id_cliente, sum(p.valor) AS valorTotal 
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente
 GROUP BY c.id_cliente, c.nome
 ORDER BY 2 DESC LIMIT 1;

/* ATIVIDADE 7
 * Utilizar CTE para calcular o total de vendas por produto
 */
WITH VendasPorProduto AS (
	SELECT ip.id_produto,
		   SUM(ip.quantidade) AS qtd_total_vendido
	  FROM ItensPedido ip
	 GROUP BY ip.id_produto
)
SELECT p.id_produto, p.nome_produto, 
	   vp.qtd_total_vendido, (vp.qtd_total_vendido * p.preco) AS valor_total_vendas
  FROM Produtos p 
  JOIN VendasPorProduto vp ON p.id_produto = vp.id_produto
  
/* ATIVIDADE 8
 *Listar todos os produtos comprados por cada cliente
 */
SELECT c.id_cliente, c.nome AS Cliente, prod.id_produto, prod.nome_produto
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente 
  JOIN ItensPedido ip ON p.id_pedido = ip.id_pedido 
  JOIN Produtos prod ON ip.id_produto = prod.id_produto

/* ATIVIDADE 9
Ranquear clientes pelo valor total gasto começando pelo rank 1 para o maior valor.
*/
SELECT c.id_cliente, c.nome, SUM(p.valor) AS total_gasto,
	   RANK() OVER (ORDER BY SUM(p.valor) DESC) AS ranking
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente
 GROUP BY c.id_cliente, c.nome

/* ATIVIDADE 10
Número de pedidos por cliente, considerando apenas aqueles com mais de 1 pedido
*/
SELECT c.id_cliente, c.nome, count(*) AS QtdPedido 
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente
 GROUP BY c.id_cliente, c.nome
HAVING COUNT(p.id_pedido) > 1

/* ATIVIDADE 11
Calcular para cada cliente a quantidade de dias entre um pedido e o pedido imediatamente anterior
*/
WITH PedidosClientes AS (
SELECT 
    id_cliente,
    id_pedido,
    data_pedido,
    valor,
    LAG(data_pedido) OVER (PARTITION BY id_cliente ORDER BY data_pedido) AS data_pedido_anterior
  FROM Pedidos)
SELECT c.nome AS Cliente, pc.data_pedido AS DtPedidoAtual, pc.data_pedido_anterior AS DtPedidoAnterior,
 IFNULL (CAST ((JulianDay(pc.data_pedido) - JulianDay(pc.data_pedido_anterior)) AS Integer), 0) AS DifDatas
  FROM Clientes c 
  JOIN PedidosClientes pc ON c.id_cliente = pc.id_cliente

/* ATIVIDADE 12
Crie uma consulta que retorne um relatórios contedo as seguintes colunas (obs: use o padrão que preferir para nomear as colunas):
ID do cliente
Nome do cliente
Cidade do cliente
ID do pedido
Data do pedido
Valor do pedido
Preço do pedido sem desconto (pode ser recuperado somando a coluna "preço" de cada produto dentro do pedido)
Quantidade de dias entre o pedido e seu pedido imediatamente anterior
 */
WITH PedidoAnterior AS (
 SELECT p.id_pedido, p.id_cliente, p.data_pedido, LAG(p.data_pedido) OVER (PARTITION BY p.id_cliente ORDER BY p.data_pedido) AS data_pedido_anterior
   FROM Pedidos p
),
PrecoSemDesconto AS (
	SELECT ip.id_pedido, SUM(pr.preco*ip.quantidade) AS preco_sem_desconto
	  FROM ItensPedido ip
	  JOIN Produtos pr ON ip.id_produto = pr.id_produto
	 GROUP BY ip.id_pedido
)
	SELECT c.id_cliente, c.nome AS nome_cliente, c.cidade AS cidade_cliente,
		   p.id_pedido, p.data_pedido, p.valor AS valor_pedido,
		   psd.preco_sem_desconto,
		   (psd.preco_sem_desconto - p.valor) AS preco_desconto ,
		   CASE WHEN pa.data_pedido_anterior IS NOT NULL THEN JULIANDAY(p.data_pedido) - JULIANDAY(pa.data_pedido_anterior)
		   		ELSE NULL
		   END AS dias_entre_pedidos
	  FROM Pedidos p
	  JOIN Clientes c ON p.id_cliente = c.id_cliente
	  JOIN PrecoSemDesconto psd ON p.id_pedido = psd.id_pedido
 LEFT JOIN PedidoAnterior pa ON p.id_pedido = pa.id_pedido
     ORDER BY c.id_cliente, p.data_pedido