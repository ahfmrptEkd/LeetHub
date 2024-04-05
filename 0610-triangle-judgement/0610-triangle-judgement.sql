# Write your MySQL query statement below
SELECT *, IF((((abs(x) + abs(y)) > abs(z)) And 
            ((abs(x) + abs(z)) > abs(y)) And
            ((abs(y) + abs(z)) > abs(x))), "Yes", "No") AS triangle
FROM Triangle;
