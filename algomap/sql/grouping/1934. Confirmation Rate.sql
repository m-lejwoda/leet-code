# Write your MySQL query statement below

SELECT
    s.user_id,
    Round(COALESCE(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) * 1.0 / COUNT(s.user_id), 0),2) AS confirmation_rate
FROM
    Signups s
LEFT JOIN
    Confirmations c ON c.user_id = s.user_id
GROUP BY
    s.user_id;