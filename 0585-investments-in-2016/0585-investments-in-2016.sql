# Write your MySQL query statement below
Select Round(Sum(tiv_2016), 2) as tiv_2016
From (
    Select *,
        Count(*) Over(Partition by tiv_2015) as tiv_2015_cnt,
        Count(*) Over(Partition by lat, lon) as loc_cnt
    From Insurance) as t1
Where tiv_2015_cnt > 1 And loc_cnt = 1