서브 쿼리에 대해서 먼저 잡는다고 모양을 잡는다고 생각하는게 좋다.  

Here we can see clearly that when we subtract a day from every first login dates. For player 1 there's a date common in event date and day_before_first_login column. That is 2016-03-01

Which proves that the player logged in on 2016-03-01 and 2016-03-02, making it two consecutive days.

<br>

- Is it necessary to use Date_sub? Can't we use Date_Add?

If you just replace Date_Sub with Date_Add, it'll fetch you result as 0 because we are grouping by min(event_date) which is 2016-03-01, add 1 to it and you don't have a date to compare.
