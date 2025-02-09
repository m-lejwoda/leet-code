# Write your MySQL query statement below
Select p.project_id, Round(Avg(experience_years),2) as average_years from Employee e Left Join Project p on e.employee_id = p.employee_id
Group by p.project_id
having p.project_id is not null
