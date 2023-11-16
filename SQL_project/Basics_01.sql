show databases;

create database employee_db;

drop database employee_db;
drop database employee_data;
create database employee_data;

use employee_data;
create table employee_info(
id int, 
first_name varchar(25), 
last_name varchar(25),
birth_data date,
hire date,
salary float, 
post varchar(50)
);



# Show the imported table
use employee_data;
show tables;

## Insert data into the table
insert into employee_info(id, first_name, last_name, birth_data, hire, salary, post) values(001, "Viraj", "Awate", "1998-12-31", "2023-07-24", 2000000, "DataScientist");
insert into employee_info(id, first_name, last_name, birth_data, hire, salary, post) values(002, "Shashank", "Awate", "2003-01-07", "2025-01-12", 400000, "ChartAcc");
insert into employee_info(id, first_name, last_name, birth_data, hire, salary, post) values(003, "Ravi", "Awate", "2003-01-02", "2025-11-12", 400000, "ChartAc");

# Select  a employee  with salary more than 20000
select * from employee_info where salary > 20000;

# Arange the data in order
select * from employee_info order by salary desc;

# Manipulate the data
SET SQL_SAFE_UPDATES = 0;
update employee_info set salary = 5000000 where first_name = "Viraj";
select * from employee_info;
alter table employee_info add dept varchar(80);
select * from emlpoyee_info;

update employee_info set dept = "Robotics" where first_name = "Viraj";
update employee_info set dept = "Finance" where first_name = "Shashank";

