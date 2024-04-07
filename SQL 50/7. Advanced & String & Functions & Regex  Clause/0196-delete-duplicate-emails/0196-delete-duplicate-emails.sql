# Write your MySQL query statement below
DELETE p1 
FROM person p1,
     person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

-- Self Join: person 테이블을 p1과 p2라는 별칭으로 self join 함. 이는 테이블의 각 행을 다른 모든 행과 비교할 수 있게 해줍니다.