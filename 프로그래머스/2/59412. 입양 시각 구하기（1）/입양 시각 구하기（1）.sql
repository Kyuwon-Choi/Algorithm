-- 코드를 입력하세요
SELECT hour(datetime) as HOUR, count(*) as COUNT
from animal_outs
where hour(datetime) between '9' and '20'
group by HOUR
order by HOUR 

