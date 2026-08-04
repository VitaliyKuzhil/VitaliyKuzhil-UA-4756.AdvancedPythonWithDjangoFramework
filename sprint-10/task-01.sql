SELECT name, city, grade
FROM customers
WHERE city IN ('London', 'Paris')
ORDER BY name ASC