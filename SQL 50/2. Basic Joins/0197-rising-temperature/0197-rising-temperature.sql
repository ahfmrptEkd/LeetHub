# Write your MySQL query statement below
Select w1.id
From Weather as w1
    Join Weather as w2 On Datediff(w1.recordDate, w2.recordDate) = 1
Where w1.temperature > w2.temperature

