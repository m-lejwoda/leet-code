# Write your MySQL query statement below
select p.product_id, ifnull(round(sum(units * price)/sum(units),2),0) as average_price From Prices  p
Left join UnitsSold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id

