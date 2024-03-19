# Write your MySQL query statement below
Select
    a.machine_id,
    Round(AVG(b.timestamp - a.timestamp), 3) as processing_time

From Activity as a
    Join Activity as b on (a.machine_id = b.machine_id AND
                            a.process_id = b.process_id AND
                            a.activity_type = 'start' AND
                            b.activity_type = 'end'
    )
Group by a.machine_id

-- 1. (i[2]-i[1]) 2번째에서 전에 있는 row와 비교해서 값을 뺌. 1개의 값 = x
-- 2. (i[2]-i[1]) 4번째에서 전에 있는 row와 비교해서 값을 뺌. 1개의 값 = y
-- 3. 이 2값을 더하고 (x+y) 2로 나누고 /2 = 소수점 3자리로 (:3.f) 표현해서 그것을 processing_time의 값으로 넣으면 됨.

-- Join a on b를 통해서 where 대신으로 씀.
    -- 아래처럼 where 로도 가능은 함
    --     FROM Activity a, 
    --         Activity b
    --     WHERE 
    --         a.machine_id = b.machine_id
    --     AND 
    --         a.process_id = b.process_id
    --     AND 
    --         a.activity_type = 'start'
    --     AND 
    --         b.activity_type = 'end'