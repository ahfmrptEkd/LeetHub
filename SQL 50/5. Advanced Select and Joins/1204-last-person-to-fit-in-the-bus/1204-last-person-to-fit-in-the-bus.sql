# Write your MySQL query statement below
Select person_name
From (
        Select person_id, person_name,
                Sum(weight) over (order by turn) as sum_weight
        From Queue) as t1
Where sum_weight <= 1000
Order by sum_weight Desc Limit 1

-- 서브 쿼리를 통해 from에서 테이블 생성
-- where을 통해 1000보다 작은 것들만 가져옴
--      거기서 역순으로 첫줄만 생성 해서 1000이 안되는 것들의 합들의 테스트 케이스들을 통과