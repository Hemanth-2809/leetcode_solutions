# Write your MySQL query statement below
select Employee.name,Bonus.bonus
From Employee
left outer join Bonus
on Employee.empId = Bonus.empID
where Bonus.bonus <1000 or Bonus.empID is null
