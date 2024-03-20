# Write your MySQL query statement below
Select s.user_id, Round(Avg(If(c.action = 'confirmed', 1, 0)), 2) as confirmation_rate
From Signups as s
Left Join Confirmations as c On s.user_id = c.user_id
Group by s.user_id
