# Write your MySQL query statement below
Select class
From Courses
Where class In (
    Select class
    From Courses
    Group by class
    Having count(class) >= 5
)
Group by class

-- Count() function only uses in Group by, Having, and Select
