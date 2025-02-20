-- 코드를 작성해주세요
select sum(c.score) as SCORE, c.emp_no as EMP_NO, b.emp_name as EMP_NAME, b.position as POSITION, b.email as EMAIL
from hr_employees as b, hr_grade as c
where b.emp_no = c.emp_no
group by c.emp_no
order by SCORE desc
limit 1