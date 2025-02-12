Select manager.employee_id, manager.name,
Count(distinct employee.employee_id) as reports_count,
Round(avg(employee.age)) as average_age
From Employees employee
Join Employees manager
On employee.reports_to = manager.employee_id
Group by manager.employee_id, manager.name
Order by manager.employee_id