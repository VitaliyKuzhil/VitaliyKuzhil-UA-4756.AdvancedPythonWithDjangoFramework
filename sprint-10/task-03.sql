SELECT o.order_num, o.amount, c.name
FROM orders AS o INNER JOIN customers AS c
ON o.customer_id = c.id
WHERE o.amount BETWEEN 500 and 2000
ORDER BY o.order_num