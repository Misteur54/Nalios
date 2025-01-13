SELECT p.id, p.name, COUNT(pc.category_id) AS public_category_count
FROM products p
JOIN product_categories pc ON p.id = pc.product_id
JOIN categories c ON pc.category_id = c.id
WHERE c.is_private = FALSE
GROUP BY p.id, p.name
HAVING COUNT(pc.category_id) > 5;
