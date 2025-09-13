-- 코드를 입력하세요
SELECT year(o.sales_date) as YEAR, date_format(o.sales_date, '%m') as MONTH, u.gender as GENDER, count(distinct(u.user_id)) as USERS
from ONLINE_SALE as o, user_info as u
where u.user_id = o.user_id and u.gender is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER