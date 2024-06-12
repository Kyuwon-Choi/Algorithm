-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, sum(b.SALES_AMOUNT)*a.PRICE as SALES
from PRODUCT as a, OFFLINE_SALE as b
where a.PRODUCT_ID = b.PRODUCT_ID
group by b.PRODUCT_ID
order by SALES desc, a.PRODUCT_CODE