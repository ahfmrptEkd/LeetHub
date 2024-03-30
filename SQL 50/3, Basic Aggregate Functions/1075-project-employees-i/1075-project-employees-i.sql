# Write your MySQL query statement below
Select p.project_id,  Round(sum(e.experience_years)/ count(e.experience_years), 2) as "average_years"
From Project as p
Left Join Employee as e on p.employee_id = e.employee_id
Group by p.project_id
