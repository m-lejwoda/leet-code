# Write your MySQL query statement below
With CTE as (
    Select id, recordDate as cur_recordDate,
    temperature AS cur_temp,
    LAG(temperature,1) Over (ORDER by recordDate) as prev_temp,
    LAG(recordDate,1) Over(Order by recordDate) as prev_recordDate from Weather
)

Select id
from CTE
Where DATEDIFF(cur_recordDate, prev_recordDate) = 1 and cur_temp > prev_temp