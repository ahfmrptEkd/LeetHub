# Write your MySQL query statement below
Select p.product_id, Ifnull(Round(sum((p.price * u.units))/sum(u.units),2), 0) as "average_price"
From Prices as p
    Left Join UnitsSold as u on p.product_id = u.product_id And u.purchase_date Between p.start_date And p.end_date
Group by p.product_id
