-- 코드를 작성해주세요
select d.dept_id as DEPT_ID, d.dept_name_en as DEPT_NAME_EN, round(avg(e.SAL)) as AVG_SAL
from hr_department d, hr_employees e
where d.dept_id = e.dept_id
group by DEPT_ID
order by AVG_SAL desc