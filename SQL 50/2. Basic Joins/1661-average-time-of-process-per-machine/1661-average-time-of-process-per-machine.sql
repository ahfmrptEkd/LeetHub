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

