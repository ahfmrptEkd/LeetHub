# Write your MySQL query statement below
With all_ids as (
    Select requester_id as id
    From RequestAccepted
    Union All
    Select accepter_id as id
    From RequestAccepted)

Select id, num
From
    (
        Select id,
            Count(id) as num,
            Rank
            () over(order by Count(id) Desc) as rnk
        From all_ids
        Group by id
    ) as t0
Where rnk=1