# Write your MySQL query statement below
Select *
From Cinema as C
Where C.id % 2 != 0 And C.description != "boring"
Order by rating desc