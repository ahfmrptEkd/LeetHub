# Write your MySQL query statement below
Select
    sell_date,
    Count(Distinct product) as num_sold,
    GROUP_CONCAT(Distinct product Order by product Separator ',') as products
From Activities
Group by sell_date
Order by sell_date Asc


-- COUNT(DISTINCT product) to count the number of unique products sold on each sell date.
-- GROUP_CONCAT to combine multiple values from multiple rows into a single string.