# Write your MySQL query statement below
select distinct author_id as id
from Views
where author_id = viewer_id
order by id
-- distinc 가 중복을 없애주는 제어문
-- 또는 group by 로 할 수 도 있으나 속도면에서는 느리다.