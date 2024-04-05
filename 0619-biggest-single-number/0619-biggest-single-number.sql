# Write your MySQL query statement below
Select Max(num) as num
From MyNumbers
Where num In (
    Select 
        num
    From 
        MyNumbers
    Group by 
        num
    Having count(*) = 1
)