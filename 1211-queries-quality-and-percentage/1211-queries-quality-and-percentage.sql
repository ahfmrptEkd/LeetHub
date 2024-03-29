# Write your MySQL query statement below
Select query_name, 
    Round(Sum(rating / position) / Count(query_name), 2) as quality, 
    Round((Sum(rating < 3) / Count(query_name)) * 100, 2) as poor_query_percentage
From Queries
Where query_name is not Null
Group by query_name
