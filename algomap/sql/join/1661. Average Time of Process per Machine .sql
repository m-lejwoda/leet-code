# Write your MySQL query statement below
Select a.machine_id, ROUND(AVG(b.timestamp - a.timestamp),3) as processing_time
From activity a join Activity b on a.machine_id = b.machine_id and a.process_id = b.process_id
Where a.activity_type = 'start' and b.activity_type = 'end'
Group by a.machine_id