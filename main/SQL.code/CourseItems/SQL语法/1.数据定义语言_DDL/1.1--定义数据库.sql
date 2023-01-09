create table Student_Info(
	StuID char(8),
	StuName varchar(10) not null,
	Sex char(1)	check (Sex in ('male','female')),
	School varchar(20) not null,
	PRIMARY KEY(StuID));