# Write your MySQL query statement below
select
    p.firstName,
    p.lastName,
    city,
    state
from Person p
left join Address a on a.personId=p.personId