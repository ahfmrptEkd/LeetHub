# Write your MySQL query statement below
SELECT Distinct
    i1.num as ConsecutiveNums 
FROM 
    logs i1,
    logs i2,
    logs i3
WHERE 
    i1.id=i2.id+1 AND 
    i2.id=i3.id+1 AND 
    i1.num=i2.num AND 
    i2.num=i3.num

-- 아래 처럼 겹치는 경우도 있을 수 있어, Distinct를 쓴다.
-- | ConsecutiveNums |
-- | --------------- |
-- | 3               |
-- | 3               |