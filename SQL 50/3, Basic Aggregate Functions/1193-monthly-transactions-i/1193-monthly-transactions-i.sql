# Write your MySQL query statement below
Select DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        Count(state) as trans_count,
        sum(state = "approved") as approved_count,
        sum(amount) as trans_total_amount,
        sum(CASE 
                WHEN state = 'approved' 
                THEN amount 
                ELSE 0 
            END) AS approved_total_amount
From Transactions
Group by month, country
-- DATE_FORMAT 을 이용해서 날짜의 설정을 변경 할 수 있음.