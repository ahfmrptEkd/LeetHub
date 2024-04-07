# Write your MySQL query statement below
Select employee_id
From Employees
Where salary < 30000 And
    manager_id Not in (
            Select employee_id
            From Employees
    )
Order by employee_id