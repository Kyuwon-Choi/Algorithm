-- 코드를 작성해주세요
select distinct d.id as ID, d.email as EMAIL, d.first_name as FIRST_NAME, d.last_name as LAST_NAME
from skillcodes as s, developers as d
where d.skill_code & (select sum(code) from skillcodes where category like "FRONT END")
order by ID