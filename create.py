#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('D:\\1.db')
cursor = conn.cursor()

#创建表teacher、student、course、sc、mc
cursor.execute('create table teacher(Tno char(10) primary key, Tpassword char(30), Tname char(20), Tsex char(2), Tage smallint, Tdept char(20))')
cursor.execute('create table student(Sno char(10) primary key, Spassword char(30), Sname char(20), Ssex char(2), Sage smallint, Sdept char(20), Smajor char(20))')
cursor.execute('create table course(Cno char(3) primary key, Cname char(40), Cpno char(3), Ccredit smallint, foreign key (Cpno) references course(Cno))')
cursor.execute('create table sc(Sno char(10), Tno char(10), Cno char(3), primary key(Sno,Tno,Cno), Fgrade smallint, foreign key (Sno) references student(Sno), foreign key (Tno) references teacher(Tno), foreign key (Cno) references course(Cno))')
cursor.execute('create table mc(Smajor char(20), Cno char(4), primary key(Sdept,Cno), c_e char(1), foreign key (Sdept) references student(Sdept), foreign key (Cno) references course(Cno))')

#往teacher表中写入信息
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1999201122\', \'1999201122\', \'李明\', \'男\', 32, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1980201027\', \'1980201027\', \'王敏\', \'女\', 39, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1999201001\', \'1999201001\', \'张三\', \'女\', 37, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1984201046\', \'1984201046\', \'李四\', \'男\', 47, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1989201037\', \'1989201037\', \'王五\', \'男\', 42, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1987201056\', \'1987201056\', \'赵六\', \'女\', 45, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1989201114\', \'1989201114\', \'李明\', \'女\', 46, \'信息学院\')')
#往course表中写入信息,course表信息确定
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'001\', \'信息安全数学基础\', 2)')
cursor.execute('insert into course(Cno, Cname, Cpno, Ccredit, Ctno) values(\'002\', \'密码学\', \'0010\', 3)')#有先修课
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'099\', \'数学分析1\', 4)')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'100\', \'数学分析2\', 4)')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'101\', \'数学分析3\', 5)')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'102\', \'高等代数\', 4)')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'110\',\'操作系统\', 4)')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'111\',\'数据科学导论\', 4)')
#往mc表中写入信息,mc表信息确定
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'099\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'100\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'101\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'102\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'信息安全\', \'001\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'信息安全\', \'002\', \'e\')')#选修
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'计算机\', \'110\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数据科学导论\', \'111\', \'c\')')

a = 'insert into student(Sno, Spassword) values('
value = input('ID：')
a = a + '\'' + value + '\''
value = input('密码：')
a = a + ',' + '\'' + value + '\'' +')'
cursor.execute(a)

cursor.execute('select * from student')
cursor.execute('select * from course')
cursor.execute('select * from teacher')
cursor.execute('select * from mc')
values = cursor.fetchall()
print(values)
conn.commit()
conn.close()
