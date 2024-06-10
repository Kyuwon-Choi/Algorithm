-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
from ANIMAL_OUTS 
where ANIMAL_ID not in
(   SELECT b.ANIMAL_ID
    from ANIMAL_INS as a,ANIMAL_OUTS as b
    where b.ANIMAL_ID = a.ANIMAL_ID 
)
order by ANIMAL_ID