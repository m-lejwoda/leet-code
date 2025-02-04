# Write your MySQL query statement below
Select customer_id, count(Visits.visit_id) as count_no_trans From Visits Left join Transactions on Visits.visit_id = Transactions.visit_id
Where Transactions.transaction_id is Null
Group by Visits.customer_id