-- 코드를 입력하세요
SELECT year(b.SALES_DATE) as YEAR, month(b.SALES_DATE) as MONTH, count(distinct b.USER_ID) as PURCHASED_USERS, round(count(distinct b.USER_ID)/(
    select count(USER_ID)
    from USER_INFO
    where year(JOINED)='2021'
),1) as PUCHASED_RATIO
from USER_INFO as a, ONLINE_SALE as b
where a.USER_ID = b.USER_ID and year(a.JOINED)='2021'
group by YEAR, MONTH
order by YEAR, MONTH
