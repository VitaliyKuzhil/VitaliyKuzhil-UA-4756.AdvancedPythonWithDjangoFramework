SELECT c.name, c.city, SUM(o.amount) AS totalSum
FROM customers AS c INNER JOIN orders AS o
ON c.id = o.customer_id
WHERE o.amount BETWEEN 100 AND 3500
GROUP BY c.name
ORDER BY c.city