# Write your MySQL query statement below
Select IFNULL((
                Select Distinct salary
                From Employee
                Order by salary Desc
                Limit 1 Offset 1), Null
                ) as SecondHighestSalary


-- MySQL의 경우 서브쿼리가 Null을 반환할 경우, 이미 Null을 반환하므로, 굳이 "IFNULL" 처리가 필요없음.
-- OFFSET 1은 검색된 결과 집합에서 첫 번째 행을 건너뛰고 그 다음 행부터 결과를 가져오라는 의미입니다. 
-- 즉, ORDER BY Salary DESC로 인해 높은 급여부터 낮은 급여 순으로 정렬된 상태에서, 가장 높은 급여(첫 번째 행)를 제외하고 그 다음으로 높은 급여(두 번째 행)를 선택하게 됩니다.