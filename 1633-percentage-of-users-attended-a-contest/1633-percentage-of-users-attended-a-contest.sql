# Write your MySQL query statement below
Select Register.contest_id, Round(Count(Distinct Register.user_id)*100 / (
    Select Count(user_id)
    From Users
    ), 2) as percentage
From Register
Group by contest_id
Order by percentage desc, contest_id 