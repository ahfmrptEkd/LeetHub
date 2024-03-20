# Write your MySQL query statement below
SELECT e.name
FROM Employee as e
Left Join Employee as e2 On e.id = e2.managerId
Group by e.id
Having Count(*) >= 5

--  조건문 같은 경우를 having을 통해 풀 수 있다.