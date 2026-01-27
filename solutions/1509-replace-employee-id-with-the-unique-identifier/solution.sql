# Write your MySQL query statement below
select Employees.name,EmployeeUNI.unique_id
From Employees 
left outer join EmployeeUNI
on Employees.id = EmployeeUNI.id


