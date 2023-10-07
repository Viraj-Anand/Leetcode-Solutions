# Write your MySQL query statement below
select 
t1.employee_id,
t1.name,
count((t2.reports_to)) as reports_count,
round(avg(t2.age)) as average_age
from employees as t1
left join employees as t2
on t1.employee_id=t2.reports_to
where t2.employee_id is not null
group by t1.employee_id,t1.name
order by t1.employee_id