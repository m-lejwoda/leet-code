# Write your MySQL query statement below
Select name, bonus From Employee e Left Join Bonus b On e.empId = b.empId
Where bonus < 1000 or bonus Is NUll