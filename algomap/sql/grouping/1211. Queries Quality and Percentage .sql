Select query_name,
Round(avg(rating/position),2) as quality,
Round(avg(rating<3)*100,2) as poor_query_percentage
from queries
Group by query_name