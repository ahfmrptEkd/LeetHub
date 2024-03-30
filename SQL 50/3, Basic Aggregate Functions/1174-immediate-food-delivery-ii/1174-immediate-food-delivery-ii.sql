# Write your MySQL query statement below
Select Round(Sum(
        Case
            When order_date = customer_pref_delivery_date 
            Then 1
            Else 0
        End
        )* 100 / Count(Distinct customer_id), 2) as immediate_percentage
From Delivery
Where (customer_id, order_date) In (
    Select customer_id, Min(order_date) as first_order_date
    From Delivery
    Group by customer_id
)