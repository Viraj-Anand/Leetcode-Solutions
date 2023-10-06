WITH CustomerProductCount AS (
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) AS bought_count
    FROM
        Customer
    GROUP BY
        customer_id
)

SELECT
    cpc.customer_id
FROM
    CustomerProductCount cpc
JOIN
    (SELECT COUNT(DISTINCT product_key) AS total_products FROM Product) p
ON
    cpc.bought_count = p.total_products;
