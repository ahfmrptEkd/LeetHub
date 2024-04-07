Select
    a.visited_on as visited_on,
    Sum(b.day_sum) as amount,
    Round(Avg(b.day_sum), 2) as average_amount
From 
    (Select visited_on, Sum(amount) as day_sum
     From Customer
     Group by visited_on) as a,
     (Select visited_on, Sum(amount) as day_sum
     From Customer
     Group by visited_on) as b
Where DATEDIFF(a.visited_on, b.visited_on) Between 0 And 6 # To make sure the rolling sum and rolling avg are only calculated in a 7-day window 
Group by a.visited_on
Having Count(b.visited_on) = 7
# This is to make sure it starts from the 7th day since only if it reaches the 7th day there will be 7 days that are 0-6 days
# prior to the current days