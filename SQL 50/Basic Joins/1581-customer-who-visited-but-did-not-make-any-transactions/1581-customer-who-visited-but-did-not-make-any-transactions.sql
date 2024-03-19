# Write your MySQL query statement below
-- 새로운 컬럼이 필요함.
Select 
    v.customer_id, 
    Count(*) AS count_no_trans 
From Visits AS v
    Left Join Transactions AS t On v.visit_id = t.visit_id
where
    t.visit_id IS NULL
Group by
    customer_id