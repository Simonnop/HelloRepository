--1 查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
select a.*,d.Cname,b.score from Student a,sc b,sc c ,Course d where a.SId=b.SId and b.CId = d.CId and b.CId='01' and c.CId='02' and b.score>c.score

Select a.*,b.score,c.score
FROM Student a,SC b,SC c
WHERE a.SId=b.SId AND b.SId=c.SId AND b.CId='01' AND c.CId='02' And b.score>c.score

--2 查询同时存在" 01 "课程和" 02 "课程的情况
select a.*,b.CId,b.score from SC a,SC b where a.SId=b.SId and a.CId='01' and b.CId='02'

--3 查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )
select a.*,b.CId from SC a left join SC b on a.SId=b.SId and a.CId='01' and b.CId = '02' where a.CId='01'

--4 查询不存在" 01 "课程但存在" 02 "课程的情况
select * from sc where SId not in (select sid from Sc where CId='01') and cid='02'

--5 查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
select a.sid,b.sname,avg(score) avgScore from Sc a, student b where a.sid=b.sid group by a.Sid,b.sname having avg(score)>=60

select a.sid,a.sname,avg(b.score) 平均成绩
from student a,sc b
where a.sid=b.sid
group by b.sid,a.sname,a.sid
having avg(b.score)>=60

--6 查询在 SC 表存在成绩的学生信息
select * from Student where sid in (select distinct sid from SC)


--7 查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为 null )
select a.sid,a.sname,count(b.cid),sum(c.score) from student a left join sc c on a.sid=c.sid left join Course b on b.cid=c.cid group by a.sid,a.sname order by a.sid

--8 查有成绩的学生信息
select * from Student a where exists (select sid from SC b where a.sid=b.sid)

--9 查询「李」姓老师的数量
select count(1) from Teacher where Tname like '李%'

--10 查询学过「张三」老师授课的同学的信息
select d.* from Teacher a join Course b on a.Tid=b.Tid join sc c on b.cid=c.cid join student d on c.sid=d.sid where a.tname='张三'

--11 查询没有学全所有课程的同学的信息
select * from student a where not exists(select 1 from sc where sid=a.sid group by sid having count(cid) =(select count(1) from course))

--12 查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
select * from student where sid in (select sid from sc where cid in ( select cid from sc where sid='01'))

SELECT distinct a.*
FROM Student a, SC b
WHERE a.SId=b.SId AND b.cid IN (
    select CId
    FROM SC
    where sid='01'
)

--13 查询和" 01 "号的同学学习的课程 完全相同的其他同学的信息
select * from Student where SId in(
select sid from sc where cid in (select cid from sc where sid='01') group by SId having COUNT(cid)= (select COUNT(cid) from sc where sid='01') and sid<>'01')

--14 查询没学过"张三"老师讲授的任一门课程的学生姓名
select * from student where sid not in (select sid from sc where cid in (select cid from course where tid in (select tid from Teacher where tname='张三')))

--15 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select b.sid,b.sname,avg(a.score) from sc a,student b where a.score<60 and a.sid=b.sid group by b.sid,b.sname having count(1)>1

--16 检索" 01 "课程分数小于 60，按分数降序排列的学生信息
select b.*  from sc a, student b where a.sid=b.sid and cid='01' and score<60 order by score desc

--17 按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
select * from (select avg(score) avgscore,sid from sc group by sid ) a,sc b where a.sid=b.sid order by avgscore desc

--18 查询各科成绩最高分、最低分和平均分：
--以如下形式显示：课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
--及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
--要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
select CId,MAX(score),MIN(score),AVG(score) from  SC group by CId

 select b.CId 课程ID,(select Cname from Course where CId=b.CId ) 课程,MAX(b.score) 最高分,MIN(b.score) 最低分,AVG(b.score) 平均分,COUNT(1) 选修人数,SUM(case when score>=60 then 1 else 0 end)*1.0/COUNT(1) 及格率,sum(case when score between 70 and 79 then 1 else 0 end)*1.0/COUNT(1) 中等率,sum(case when score between 80 and 89 then 1 else 0 end)*1.0/COUNT(1) 优良率,sum(case when score >=90 then 1 else 0 end)*1.0/COUNT(1) 优秀率 from SC b group by b.CId order by COUNT(1) desc,CId

 select sc.CId ,max(sc.score)as 最高分,min(sc.score)as 最低分,AVG(sc.score)as 平均分,count(*)as 选修人数,sum(case when sc.score>=60 then 1 else 0 end )*1.0/count(*) as 及格率,sum(case when sc.score>=70 and sc.score<80 then 1 else 0 end )*1.0/count(*) as 中等率,sum(case when sc.score>=80 and sc.score<90 then 1 else 0 end )*1.0/count(*)as 优良率,sum(case when sc.score>=90 then 1 else 0 end )*1.0/count(*)as 优秀率 from sc GROUP BY sc.CId ORDER BY count(*)DESC, sc.CId ASC

--19 按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺
select cid, score,rank() over(partition by cid order by score desc) dx from SC

--20 按各科成绩进行排序，并显示排名， Score 重复时合并名次
select cid, score,dense_rank() over(partition by cid order by score desc) dx from SC

--21 查询学生的总成绩，并进行排名，总分重复时保留名次空缺
select sid,sum(score),rank() over(order by sum(score) desc) dx from SC group by sid

--22 查询学生的总成绩，并进行排名，总分重复时不保留名次空缺
select sid,sum(score),dense_rank() over(order by sum(score) desc) dx from SC group by sid

--23 统计各科成绩各分数段人数：课程编号，课程名称，[100-85]，[85-70]，[70-60]，[60-0] 及所占百分比
 select sc.CId,b.Cname, sum(case when sc.score>=60 then 1 else 0 end) [60-0],
 cast(convert(decimal(4,2),sum(case when sc.score>=60 then 1 else 0 end )*1.0/count(*)*100) as varchar(100))+'%' as 及格率,
 sum(case when sc.score>=70 and sc.score<80 then 1 else 0 end ) [70-60],
 cast(convert(decimal(4,2),sum(case when sc.score>=70 and sc.score<80 then 1 else 0 end)*1.0/count(*)*100) as varchar(100))+'%' as 中等率,
 sum(case when sc.score>=80 and sc.score<90 then 1 else 0 end ) [85-70],
 cast(convert(decimal(4,2),sum(case when sc.score>=80 and sc.score<90 then 1 else 0 end )*1.0/count(*)*100) as varchar(100))+'%' as 优良率,
 sum(case when sc.score>=90 then 1 else 0 end ) [100-85],
 cast(convert(decimal(4,2),sum(case when sc.score>=90 then 1 else 0 end)*1.0/count(*)*100) as varchar(100))+'%' as 优秀率 
 from sc , Course b where sc.CId=b.CId GROUP BY sc.CId,b.Cname ORDER BY count(*)DESC, sc.CId ASC

--24 查询各科成绩前三名的记录
select * from (select cid, score,rank() over(partition by cid order by score desc) dx from SC) a where dx<=3

--25 查询每门课程被选修的学生数
select Cid,COUNT(1) from SC group by CId

--26 查询出只选修两门课程的学生学号和姓名
select sc.sid,(select sname from Student where SId=sc.SId) sname from SC group by sc.sid having COUNT(1)=2

--27 查询男生、女生人数
select Ssex,COUNT(1)人数 from Student group by Ssex

--28 查询名字中含有「风」字的学生信息
select * from Student where Sname like '%风%'

--29 查询同名同性学生名单，并统计同名人数
select Sname,Ssex,COUNT(1) 人数 from Student group by Sname,Ssex having COUNT(1)>1

--30 查询 1990 年出生的学生名单
select * from  Student where YEAR(Sage)='1990'

--31 查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
select AVG(score),cid from SC group by CId order by AVG(score) desc,CId 

--32 查询平均成绩大于等于 85 的所有学生的学号、姓名和平均成绩
select a.sid,b.Sname,AVG(score) score from SC a,Student b where a.SId=b.SId  group by a.sid,b.Sname having avg(a.score)>85

--33 查询课程名称为「数学」，且分数低于 60 的学生姓名和分数
select c.Sname,a.score from SC a,Course b,Student c where a.CId=b.CId and a.SId=c.SId and b.Cname='数学' and a.score<60

--34 查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）
select * from Student a left join SC b on a.SId=b.SId left join Course c on b.CId=c.CId

--35 查询任何一门课程成绩在 70 分以上的姓名、课程名称和分数
select b.Sname,c.Cname,a.score from SC a,Student b,Course c where a.SId=b.SId and a.CId=c.CId and a.score>70

--36 查询不及格的课程
select distinct b.Cname from SC a,Course b where a.CId=b.CId and a.score<60

--37 查询课程编号为 01 且课程成绩在 80 分以上的学生的学号和姓名
select b.SId,b.Sname,score from SC a, Student b where a.SId=b.SId and a.CId='01' and a.score>=80

--38 求每门课程的学生人数
select a.CId,b.Cname ,str(COUNT(1))+'人' 选修人数 from SC a,Course b where a.CId=b.CId group by a.CId,b.Cname

--39 成绩不重复，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
select top 1 Sname,score from SC a,Course b,Student c,Teacher d where a.CId=b.CId and a.SId=c.SId and b.TId=d.TId and d.Tname='张三' order by score desc

--40 成绩有重复的情况下，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
select Sname,max(score) from SC a,Course b,Student c,Teacher d where a.CId=b.CId and a.SId=c.SId and b.TId=d.TId and d.Tname='张三' group by b.CId order by score desc

--41 查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
select distinct a.SId,a.CId,b.score from SC a,SC b where a.score=b.score and a.CId!=b.CId and a.SId=b.SId

--42 查询每门功成绩最好的前两名
select * from (select sid,cid, ROW_NUMBER() over(partition by cid order by score desc) mc from sc) a,Student b where a.SId=b.SId and mc<=2

--43 统计每门课程的学生选修人数（超过 5 人的课程才统计）。
select CId,COUNT(1) from SC group by CId having COUNT(1)>5

--44 检索至少选修两门课程的学生学号
select SId from SC group by SId having COUNT(1)>1

--45 查询选修了全部课程的学生信息
select b.* from SC a,Student b where a.SId=b.SId group by b.SId,b.Sname,b.Sage,b.Ssex having COUNT(1)>2

--46 查询各学生的年龄，只按年份来算
select sage, datediff(year, sage,getdate()) age from student 

--47 按照出生日期来算，当前月日 < 出生年月的月日则，年龄减一
select sage,case when month(sage)< month(getdate()) or (month(sage)= month(getdate()) and day(sage)= day(getdate())) then datediff(year, sage,getdate())  else datediff(year, sage,getdate())-1 end age from student

--48 查询本周过生日的学生
select * from student where datepart(week,sage) = datepart(week,getdate())

--49 查询下周过生日的学生
select * from student where datepart(week,sage) = datepart(week,getdate())+1

--50 查询本月过生日的学生
select * from student where month(sage) = month(getdate())

--51 查询下月过生日的学生
select * from student where month(sage) = month(dateadd(month,1, getdate()))