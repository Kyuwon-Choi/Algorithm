-- 코드를 입력하세요
select FLAVOR
from(
select FLAVOR, sum(TOTAL_ORDER) as sum
from 
(SELECT FLAVOR, TOTAL_ORDER
from FIRST_HALF as f
union all
select FLAVOR, TOTAL_ORDER
from JULY as j ) as t
group by FLAVOR
order by sum DESC) as combine
limit 3
    