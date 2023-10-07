# Write your MySQL query statement below
select
person_name 
from queue as q
where (select sum(weight) from queue where q.turn>=turn)<=1000
order by turn desc
limit 1