-- # Write your MySQL query statement below
(Select name as results
From MovieRating
    Join Users Using(user_id)
Group by name
Order by Count(*) Desc, name
Limit 1)

Union All

(Select title as results
From MovieRating
    Join Movies Using(movie_id)
Where Extract(Year_Month From created_at) = 202002
Group by title
Order by Avg(rating) Desc, title
Limit 1)