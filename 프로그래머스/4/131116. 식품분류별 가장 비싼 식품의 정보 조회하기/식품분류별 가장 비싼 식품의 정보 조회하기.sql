-- 코드를 입력하세요
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, PRICE) in (
    select CATEGORY, max(PRICE)
    from FOOD_PRODUCT
    GROUP BY CATEGORY
)
and (CATEGORY ='과자' or CATEGORY ='국' or CATEGORY ='김치' or CATEGORY ='식용유')
order by MAX_PRICE desc
