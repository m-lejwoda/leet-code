with FirstOrders as (SELECT d.customer_id, d.delivery_id,
       CASE
           WHEN d.order_date = d.customer_pref_delivery_date THEN 'immediate'
           ELSE 'scheduled'
       END AS res,
       d.order_date AS first_order_date
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) first_orders
ON d.customer_id = first_orders.customer_id
AND d.order_date = first_orders.first_order_date
)

SELECT
    Round(immediate_ratio * 100,2) AS immediate_percentage
FROM (
    SELECT
        COUNT(*) AS total_orders,
        AVG(CASE WHEN res = 'immediate' THEN 1.0 ELSE 0 END) AS immediate_ratio
    FROM FirstOrders
) subquery;
