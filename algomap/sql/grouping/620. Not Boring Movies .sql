# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE description != 'boring' and mod(Round(id,0),2) = 1
Order by rating DESC;