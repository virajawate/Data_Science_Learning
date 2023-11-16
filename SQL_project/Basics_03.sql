## Stored Prodcedure--Compiled format
## Functions
## Troiggers
## Joins
## CTE Windows Functions
show databases;
drop database day_3;
create database day_3;
drop database day_3;
create database day_3;
use day_3;
## Features: ID, FIRST_NAME, LAST_NAME, STUDENT_CODE, SUBJECTS, MARKS, STUDENT_INFO

create table student_info(
id int,
first_name varchar(20),
last_name varchar(30),
student_code int,
subjects varchar(30),
marks float,
remark varchar(30));

insert into student_info values(1, "flat", "base", 11, "Sci", 33.3, "pass"),
(2, "flat", "top", 12, "Sci", 83, "pass"),
(3, "flat", "right", 13, "Sci", 67.3, "pass"),
(4, "flat", "left", 14, "Sci", 99, "pass"),
(5, "glut", "base", 15, "Sci", 30.3, "fail"),
(6, "flat", "inside", 16, "Sci", 22.3, "fail");

select * from student_info;
## Sorting is done in the stored procedures (works as funtions)
call passed_students();
## Stored Procedures with input
call merit_students(55);

call get_students(3);

call highest_marks(@topper);
select @topper; 

set @vir = "11";
call display_marks(@vir);
select @vir;

select * from student_info;

desc student_info; # Describe the table with data type and keys

create index idx_firstname on student_info(first_name);

