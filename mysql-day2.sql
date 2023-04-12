-- 数据查询语言DQL(熟练)
-- 条件查询(续集)
-- 空值判断(is null,is not null)
-- where条件会运算出三种结果:真,假,空值,只显示结果为真的数据
-- 空值:定义了一个存储空间,没有赋任何值,0和空格都不是空值
-- 查询奖金高于500的员工信息
select * from scott.emp where comm>=500;
-- 查询奖金为空的员工信息
select * from scott.emp where comm is null;
-- 查询奖金不为空的员工信息
select * from scott.emp where comm is not null;
 
--select distinct 表示查询结果中，去掉了重复的行

-- 多条件查询(and,or,in,between...and...,not)
-- and:多个条件同时满足
-- 查询部门编号为10且职位为clerk的员工信息
select * from scott.emp where deptno=10 and job='clerk';
-- or:多个条件至少有一个满足
-- 查询工资在3000以上或1000以下的员工信息
select * from scott.emp where sal>=3000 or sal<=1000;
-- in:在多个数据中取值
-- 查询工号为7839,7844,7876,7900,7902的员工信息
select * from scott.emp where empno in(7839,7844,7876,7900,7902);
-- between...and...:用于数值类型,取值范围是闭区间
-- 查询工资在1300到3000之间的员工信息
select * from scott.emp where sal between 1300 and 3000;
select * from scott.emp where 1300<=sal<=3000;-- 错误案例
-- not:取反
-- 查询岗位不是salesman的员工信息
select * from scott.emp where not(job='salesman');

-- 模糊查询(like)
-- %可以表示0到多个字符,_可以表示一个字符
-- 查询名字中含有字母M的员工信息
select * from scott.emp where ename like '%M%';
-- 查询名字由四个字符组成的员工信息
select * from scott.emp where ename like '____';

-- 集合函数/分组函数
-- count()统计个数,avg()求平均值,max()求最大值,min()求最小值,sum()求总和
-- 查询所有员工的人数,平均工资,最大工资,最小工资,工资总和
select count(*),avg(sal),max(sal),min(sal),sum(sal) from scott.emp;

-- 分组查询(将数据分类)(group by,having)
-- 在分组查询中,select后面只能接被group by的列或者分组函数
-- where后面不能接分组函数
-- 在分组查询中,having后面只能接被group by的列或者分组函数
-- 查询各岗位的人数
select job,count(*) from scott.emp group by job;
-- 查询人数大于2的岗位
select job,count(*) from scott.emp group by job having count(*)>2;

-- 排序查询(order by)
-- asc表示升序,desc表示降序,默认是升序
-- 查询所有员工信息,按照工资升序排列
select * from scott.emp order by sal;
select * from scott.emp order by sal asc;
-- 查询所有员工信息,按照工资降序排列
select * from scott.emp order by sal desc;
-- 查询所有员工信息,先按部门升序排列,再按工资降序排列
select * from scott.emp order by deptno asc,sal desc;

-- 指定查询范围(limit)
-- limit a:表示显示前a条记录
-- limit a,b:表示从第a条记录开始显示后面b条记录,初始记录行的编号是0
-- 查询工资前5的员工信息
select * from scott.emp order by sal desc limit 5;
select * from scott.emp order by sal desc limit 0,5;

-- 查询语句语法格式
-- select 要查询的内容
-- from 从哪里查询
-- where 需要满足的条件
-- group by 根据什么分组
-- having 分组需要满足什么条件
-- order by 根据什么排序
-- limit 查询几条记录

-- 综合案例
-- 1.查询10部门工作为CLERK的员工和30部门工资在2000以上的员工信息
select *
from scott.emp
where (deptno=10 and job='clerk') or (deptno=30 and sal>2000);

-- 2.查询工资在1000以下或者3000以上的员工中,哪些是30部门的
select *
from scott.emp
where (sal<1000 or sal>3000) and deptno=30;

-- 3.查询除去10部门工作为CLERK和20部门没有奖金的员工之外的员工信息
select *
from scott.emp
where not((deptno=10 and job='clerk') or (deptno=20 and comm is null));

-- 4.查询工号为7521,7654,7876,7902的员工中哪些是10部门的
select *
from scott.emp
where empno in(7521,7654,7876,7902) and deptno=10;

-- 5.查询名字倒数第二个字符是E的员工信息
select *
from scott.emp
where ename like '%E_';

-- 6.查询10部门的员工人数,平均工资,最高工资,最低工资,工资总和
select count(*),avg(sal),max(sal),min(sal),sum(sal)
from scott.emp
where deptno=10;

-- 7.查询各部门各岗位人数和平均工资
select deptno,job,count(*),avg(sal)
from scott.emp
group by deptno,job;

-- 8.查询除掉名字中含有K的员工后,员工人数大于3的各种工作,按工作降序排列
select job,count(*)
from scott.emp
where not (ename like '%K%')
group by job
having count(*)>3
order by job desc;

-- 子查询/嵌套查询:查询语句中包含查询语句(分析时化整为零,解答时化零为整)
-- 查询工号是7902的员工的领导名字
-- 1.根据7902查询领导工号
select mgr from scott.emp where empno=7902;
-- 2.根据领导工号查询领导名字
select ename from scott.emp where empno=(select mgr from scott.emp where empno=7902);
-- 子查询返回的一列数据只有一个值时,用=连接

-- 查询哪些员工在广州工作
-- 1.根据广州查询部门编号
select deptno from scott.dept where loc='广州';
-- 2.根据部门编号查询员工信息
select * from scott.emp where deptno=(select deptno from scott.dept where loc='广州');

-- 查询James所在部门的最高薪水
-- 1.根据James查询部门编号
select deptno from scott.emp where ename='James';
-- 2.根据部门编号查询最高薪水
select max(sal) from scott.emp where deptno=(select deptno from scott.emp where ename='James');

-- 查询哪些员工既不在北京工作,又不在上海工作
-- 1.根据北京和上海查询部门编号
select deptno from scott.dept where loc in ('北京','上海');
-- 2.根据部门编号查询员工信息
select * from scott.emp where deptno not in (select deptno from scott.dept where loc in ('北京','上海'));
-- 子查询返回的一列数据有多个值时,用in连接

-- 查询工资在公司平均工资以上的员工信息
-- 1.查询公司的平均工资
select avg(sal) from scott.emp;
-- 2.根据平均工资查询员工信息
select * from scott.emp where sal>(select avg(sal) from scott.emp);

-- 查询各部门有多少个岗位只有1人(较难)
-- 1.查询各部门各岗位的人数
select deptno,job,count(*) from scott.emp group by deptno,job;
-- 2.查询各部门只有1人的岗位数
select abc.deptno,count(*) from (select deptno,job,count(*) c from scott.emp group by deptno,job) abc
where c=1 group by abc.deptno;
-- 子查询返回的结果是一张表时,需要给这张临时表取别名

-- 函数运用
-- 1.if(条件,x,y):条件成立时返回x的值,不成立时返回y的值
-- 查询员工的姓名及是否有奖金的情况(奖金为空显示为否,奖金不为空显示为是)
select ename,if(comm is null,'否','是') 是否有奖金 from scott.emp;
-- 2.concat(a,b,c):将a,b,c拼接成一个字符串
-- 查询10部门的员工信息,要求岗位,姓名,薪水符合下列格式:岗位-姓名-薪水
select concat(job,'-',ename,'-',sal) from scott.emp where deptno=10;
-- 3.abs(x):返回x的绝对值
-- 查询工号与领导工号差距在100以内的员工信息
select * from scott.emp where empno-mgr between -100 and 100;
select * from scott.emp where abs(empno-mgr)<=100;
-- 4.ifnull(a,b):a不是空值则返回a本身,a是空值则返回b
-- 查询员工薪水和奖金的总和
select ename,sal+ifnull(comm,0) from scott.emp;
-- 5.sysdate():返回系统当前时间
select sysdate() from dual;-- dual是一个虚拟表,没有任何意义
-- 6.date_format(a,b):将日期类型的a按照格式b转换,格式b有如下写法:
-- %Y表示4位年,%y表示2位年,%m表示月,%d表示日
-- %H表示24小时制,%h表示12小时制,%i表示分钟,%s表示秒
-- 查询各年份入职的员工人数
select date_format(hiredate,'%Y'),count(*) from scott.emp group by date_format(hiredate,'%Y');
-- 查询员工的姓名,入职时间,入职天数
select ename,hiredate,datediff(date_format(sysdate(),'%Y-%m-%d'),hiredate) from scott.emp;

-- 多表查询
-- 在实际项目中,存在多张表,这些表不是独立的,而是有关联关系的,n张表至少需要n-1个关联关系
-- 多表查询是针对有关联关系的多张表而言的,from后面接多个表,where后面必须写明表的关联关系
-- 在多表查询中,对于同名的列,列名前面必须加上表名,用点连接
-- 点的用法:数据库名.表名(scott.emp),表名.列名(emp.deptno),数据库名.表名.列名(scott.emp.deptno)
-- 查询每个员工的工号,姓名,岗位,部门编号,部门名称
select empno,ename,job,e.deptno,dname from scott.emp e,scott.dept d
where e.deptno=d.deptno;
-- 查询工号是7369的员工的姓名和领导的姓名
select a.ename 员工,b.ename 领导
from scott.emp a,scott.emp b
where a.mgr=b.empno and a.empno=7369;
-- 查询工资比所在部门平均工资高的员工信息
select e.*,m.*
from scott.emp e,(select deptno,avg(sal) a from scott.emp group by deptno) m
where e.deptno=m.deptno and e.sal>m.a;

-- 连接查询
-- 测试人员在工作中用连接查询较少,它是开发常用的查询逻辑,面试时被问到的概率很高
-- 多表查询只能显示满足关联关系的数据,想要显示更全面的数据,可用连接查询
-- 内连接(inner join on)
-- 仅显示两张表中满足关联关系的数据
select e.*,d.* from scott.emp e inner join scott.dept d on e.deptno=d.deptno;
-- 左外连接(left join on/left outer join on)
-- 显示左边表所有数据以及右边表满足关联关系的数据
select e.*,d.* from scott.emp e left join scott.dept d on e.deptno=d.deptno;
-- 右外连接(right join on/right outer join on)
-- 显示右边表所有数据以及左边表满足关联关系的数据
select e.*,d.* from scott.emp e right join scott.dept d on e.deptno=d.deptno;
-- mysql没有全外连接,要显示两张表的所有数据,
-- 可以使用union关键字连接左外连接和右外连接
(select e.*,d.* from scott.emp e left join scott.dept d on e.deptno=d.deptno)
UNION
(select e.*,d.* from scott.emp e right join scott.dept d on e.deptno=d.deptno);

-- 视图(view):虚拟表,对应一段SQL语句
-- 创建视图
create view scott.shitu as 
select empno,ename,job,e.deptno,dname from scott.emp e,scott.dept d
where e.deptno=d.deptno;
-- 使用视图
select * from scott.shitu;
-- 删除视图
drop view scott.shitu;

-- 索引(index):类似表的标签,可提升查询的效率
-- 创建索引
create index suoyin on scott.emp(job);

select ename,sal from scott.emp;
select ename,job from scott.emp;




