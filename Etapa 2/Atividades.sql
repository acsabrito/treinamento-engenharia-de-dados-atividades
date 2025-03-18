/* ATIVIDADE 1 
 * Listar os nomes e cidades de todos os clientes em uma só consulta
 */
SELECT * FROM Clientes

/* ATIVIDADE 2 
 * Listar os pedidos com valor acima de R$100
 */
SELECT * FROM Pedidos p WHERE valor > 100

/* ATIVIDADE 3 
 * Listar os pedidos ordenados pelo valor (decrescente)
 */
SELECT * FROM Pedidos p ORDER BY valor DESC

/* ATIVIDADE 4 
 * Listar os 3 primeiros produtos cadastrados
 */
SELECT * FROM Produtos p LIMIT 3

/* ATIVIDADE 5 
 * Listar o total de valor gasto por cada cliente em pedidos.
 */
SELECT id_cliente, sum(valor) AS valorTotal FROM Pedidos p GROUP BY id_cliente

/* ATIVIDADE 6
 * Encontrar o cliente com o maior valor gasto
 */
SELECT p.id_cliente, sum(p.valor) AS valorTotal FROM Pedidos p GROUP BY p.id_cliente ORDER BY 2 DESC LIMIT 1

/* ATIVIDADE 7
 * Utilizar CTE para calcular o total de vendas por produto
 */
WITH TotalVendas AS (
	SELECT ip.id_pedido, p.valor, sum(ip.quantidade) AS qtdTotal  FROM ItensPedido ip JOIN Pedidos p ON ip.id_pedido = p.id_pedido GROUP BY ip.id_pedido, p.valor
)
SELECT ip.id_produto, sum((tv.valor/qtdTotal)*ip.quantidade) AS ValorVendasTotal FROM TotalVendas tv JOIN ItensPedido ip ON tv.id_pedido = ip.id_pedido GROUP BY ip.id_produto

/* ATIVIDADE 8
 *Listar todos os produtos comprados por cada cliente
 */
SELECT c.nome AS Cliente, prod.nome_produto AS Produto
  FROM Clientes c 
  JOIN Pedidos p ON c.id_cliente = p.id_cliente 
  JOIN ItensPedido ip ON p.id_pedido = ip.id_pedido 
  JOIN Produtos prod ON ip.id_produto = prod.id_produto

/* ATIVIDADE 9
Ranquear clientes pelo valor total gasto começando pelo rank 1 para o maior valor.
*/
WITH RankPedidosClientes AS (
	SELECT id_cliente, sum(valor) AS valorTotal FROM Pedidos p GROUP BY id_cliente
)
SELECT c.id_cliente, c.nome, rpc.valorTotal FROM Clientes c JOIN RankPedidosClientes rpc ON c.id_cliente = rpc.id_cliente ORDER BY rpc.valorTotal desc, c.nome

/* ATIVIDADE 10
Número de pedidos por cliente, considerando apenas aqueles com mais de 1 pedido
*/
SELECT id_cliente, count(*) AS QtdPedido FROM Pedidos p GROUP BY p.id_cliente HAVING COUNT(*) > 1

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
 Ifnull (Cast ((JulianDay(pc.data_pedido) - JulianDay(pc.data_pedido_anterior)) As Integer), 0) as DifDatas
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