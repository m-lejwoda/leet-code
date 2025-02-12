# Write your MySQL query statement below
Select product_id, year as first_year, quantity, price from Sales Where (product_id, year) in
(Select product_id, Min(year) as year from sales Group by product_id)