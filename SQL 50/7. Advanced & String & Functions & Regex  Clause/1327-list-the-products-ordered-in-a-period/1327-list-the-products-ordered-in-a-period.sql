# Write your MySQL query statement below
Select 
    p.product_name as product_name, 
    Sum(o.unit) as unit
From Products as p
    Join Orders as o Using(product_id)
Where Year(o.order_date)='2020' And Month(o.order_date)='02'
Group by p.product_id
Having Sum(o.unit)>=100