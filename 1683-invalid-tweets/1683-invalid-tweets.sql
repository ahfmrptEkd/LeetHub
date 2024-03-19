# Write your MySQL query statement below
select tweet_id
from Tweets
where length(content) > 15

-- length(변수)를 통해 문자열의 개수를 구할 수 있음. == len() 
-- CHAR_LENGTH(str)를 통해 문자열의 개수를 구할 수 도 있음.