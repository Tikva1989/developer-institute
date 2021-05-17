-- select first_name as "First name", last_name as "Last name" from employees ;
-- select distinct department_id from employees;
-- select * from employees order by first_name desc;

-- create function PF(salary int, fn varchar(50), ln varchar(50)) return int as $PF$ 
-- begin employees.salary * 0.15 end;

-- select employee_id, first_name, last_name, salary from employees order by salary;
-- select sum(salary) from employees;
-- select min(salary), max(salary) from employees;
-- select avg(salary)::numeric(10,2) from employees; 
-- select count(employee_id) from employees;

-- select regexp_replace(employees.first_name, [:lower:],[:upper:]), 'g');

