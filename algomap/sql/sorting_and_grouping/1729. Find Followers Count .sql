# Write your MySQL query statement below
Select user_id, count(distinct follower_id) as followers_count
From Followers
Group by user_id
Order by user_id asc