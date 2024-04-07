# Write your MySQL query statement below
Select d.name as 'Department',
        e1.name as 'Employee',
        e1.salary as 'Salary'
From Employee as e1
Join Department as d On e1.departmentId = d.id
Where
    3 > (Select Count(Distinct e2.salary)
        From Employee as e2
        Where e2.salary > e1.salary And e1.departmentId = e2.departmentId)