#!/usr/bin/python

import sqlite3
conn = sqlite3.connect('D:\\v\1.db')
cursor = conn.cursor()

#创建表teacher、student、course、mc
cursor.execute('create table teacher(Tno char(10) primary key, Tpassword char(30), Tname char(20), Tsex char(2), Tage smallint, Tdept char(20))')
cursor.execute('create table student(Sno char(10) primary key, Spassword char(30), Sname char(20), Ssex char(2), Sage smallint, Sdept char(20), Smajor char(20))')
cursor.execute('create table course(Cno char(4) primary key, Cname char(40), Cpno char(4), Ccredit smallint, Ctno char(10), foreign key Cpno references course(Cno), foreign key Ctno references teacher(Tno))')
cursor.execute('create table sc(Sno char(10), Cno char(4), primary key(Sno,Cno), Mgrade smallint, Fgrade smallint, foreign key Sno references student(Sno), foreign key Cno references course(Cno))')
cursor.execute('create table mc(Smajor char(20), Cno char(4), primary key(Sdept,Cno), c_e char(1), foreign key Sdept references student(Sdept), foreign key Cno references course(Cno))')

#往teacher表中写入信息
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1999201122\', \'1999201122\', \'李明\', \'男\', 32, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1980201027\', \'1980201027\', \'王敏\', \'女\', 39, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1999201001\', \'1999201001\', \'张三\', \'女\', 37, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1984201046\', \'1984201046\', \'李四\', \'男\', 47, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1989201037\', \'1989201037\', \'王五\', \'男\', 42, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1987201056\', \'1987201056\', \'赵六\', \'女\', 45, \'信息学院\')')
cursor.execute('insert into teacher(Tno, Tpassword, Tname, Tsex, Tage, Tdept) values(\'1989201114\', \'1989201114\', \'李明\', \'女\', 46, \'信息学院\')')
#往course表中写入信息,course表信息确定
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'0990\', \'数学分析1\', 4, \'1999201122\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1000\', \'数学分析2\', 4, \'1980201027\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1010\', \'数学分析3\', 5, \'1980201027\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'0010\', \'信息安全数学基础\', 2, \'1999201001\')')
cursor.execute('insert into course(Cno, Cname, Cpno, Ccredit, Ctno) values(\'0020\', \'密码学\', \'0001\', 4, \'1999201001\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1100\',\'操作系统\', 4, \'1984201046\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1101\',\'操作系统\', 4, \'1989201037\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1110\',\'数据科学导论\', 4, \'1987201056\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Ctno) values(\'1111\',\'数据科学导论\', 4, \'1989201114\')')
#往mc表中写入信息,mc表信息确定
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'0990\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'0990\', \'c\')')

a = 'insert into student(Sno, Spassword) values('
value = input('ID：')
a = a + '\'' + value + '\''
value = input('密码：')
a = a + ',' + '\'' + value + '\'' +')'
cursor.execute(a)

cursor.execute('select * from course')
cursor.execute('select * from teacher')
cursor.execute('select * from mc')
values = cursor.fetchall()
print(values)
conn.commit()
conn.close()
