# Write your MySQL query statement below
Select s1.student_id, s1.student_name, sub.subject_name, Count(e.student_id) as attended_exams
From Students as s1
    Cross Join Subjects as sub
    Left Join Examinations as e On s1.student_id = e.student_id And sub.subject_name = e.subject_name
Group by s1.student_id, s1.student_name, sub.subject_name
Order by s1.student_id, sub.subject_name;

-- we use the DISTINCT keyword inside the COUNT() function to only count distinct rows.
-- The COALESCE() function is used to replace NULL values with 0, so that students who did not attend a particular exam are still included in the result set.