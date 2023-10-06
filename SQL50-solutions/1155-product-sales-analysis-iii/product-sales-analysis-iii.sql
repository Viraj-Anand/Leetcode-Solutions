# Write your MySQL query statement below
with f as (select product_id,min(year) as year
from sales
group by product_id)

select f.product_id,f.year as first_year,s.quantity,s.price
from sales as s
join f on s.product_id=f.product_id and f.year=s.year
