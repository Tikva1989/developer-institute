<!-- Instructions -->
<!-- Create 3 different tables, each one with a different relationship.
Join them with all the types of PostgreSQL Joins you’ve learned. -->

-- create table students(
-- id integer primary key not null,
-- firs_name varchar (100) not null,
-- last_name varchar (150) not null,
-- subject_id int,
-- grade int
-- );

-- create table grades(
-- student_id int,
-- subject_id int,
-- grade int
-- );

-- create table subjects(
-- subject_id serial primary key,
-- subject_name varchar(150) not null,
-- grade int
-- );

-- alter table students add constraint fk_subjects foreign key (subject_id) references subjects(subject_id);

-- alter table grades add constraint 
-- fk_students foreign key (student_id) references students(id),
-- add constraint
-- fk_subjects foreign key (subject_id) references subjects(subject_id);

-- alter table grades add constraint pk primary key (grade) ;

-- alter table subjects add constraint fk_grades foreign key (grade) references grades(grade);

-- select * from students inner join grades on students.id=grades.student_id inner join subjects on grades.grade=subjects.grade;


