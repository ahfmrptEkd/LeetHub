# Write your MySQL query statement below
SELECT *, IF((((abs(x) + abs(y)) > abs(z)) And 
            ((abs(x) + abs(z)) > abs(y)) And
            ((abs(y) + abs(z)) > abs(x))), "Yes", "No") AS triangle
FROM Triangle;

-- SELECT x,y,z,
-- case WHEN (x+y) > z AND (x+z) > y AND (y+z) > x THEN 'Yes' ELSE 'No' end AS triangle
-- FROM Triangle 
-- 조건문을 이용한 방식
