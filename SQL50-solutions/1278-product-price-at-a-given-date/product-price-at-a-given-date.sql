-- Join the subquery with the original table and use CASE to handle missing values
SELECT p.product_id, 
CASE WHEN l.product_id IS NULL THEN 10 ELSE l.new_price END AS price
FROM Products p
LEFT JOIN (
  SELECT product_id, new_price, change_date
  FROM Products
  WHERE (product_id, change_date) IN (
    -- Use the subquery as a condition
    SELECT product_id, MAX(change_date) AS max_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
  )
) l -- Add a closing parenthesis here
ON p.product_id = l.product_id
GROUP BY p.product_id
