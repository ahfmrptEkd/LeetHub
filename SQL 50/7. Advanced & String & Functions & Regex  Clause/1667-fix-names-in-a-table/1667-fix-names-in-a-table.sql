# Write your MySQL query statement below
Select user_id, Concat(Upper(Substring(name, 1, 1)), Lower(Substring(name, 2))) as name
From Users
Order by user_id

-- Separating the first character from the rest