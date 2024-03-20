# Write your MySQL query statement below
# Write your MySQL query statement below
Select E.name, B.bonus
From Employee as E
    Left Join Bonus as B On E.empId = B.empId
Where bonus < 1000 or bonus Is NULL