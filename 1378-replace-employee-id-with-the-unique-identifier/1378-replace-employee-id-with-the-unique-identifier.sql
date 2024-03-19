# Write your MySQL query statement below
Select EmployeeUNI.unique_id , Employees.name
From Employees
Left Join EmployeeUNI On EmployeeUNI.id = Employees.id