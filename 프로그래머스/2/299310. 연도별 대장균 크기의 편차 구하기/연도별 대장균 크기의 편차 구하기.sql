-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as YEAR, abs(SIZE_OF_COLONY -(first_value(SIZE_OF_COLONY) over (partition by year(DIFFERENTIATION_DATE) order by SIZE_OF_COLONY desc)) )as YEAR_DEV ,ID
from ECOLI_DATA
order by YEAR, YEAR_DEV