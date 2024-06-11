-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_INS as a, ANIMAL_OUTS as b
where a.ANIMAL_ID = b.ANIMAL_ID and a.DATETIME>b.DATETIME
order by a.DATETIME