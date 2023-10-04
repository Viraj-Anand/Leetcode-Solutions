# Write your MySQL query statement below
select t1.id
from weather t1,weather t2
where DATEDIFF(t1.recordDate,t2.recordDate)=1 and t1.temperature>t2.temperature