#!/usr/bin/python

import sqlite3
import insert
conn = sqlite3.connect('tables.db')
cursor = conn.cursor()

# 创建表teacher、student、course、sc、mc
cursor.execute('create table teacher(Tno char(10) primary key, Tpassword char(20), Tname char(20), Tsex char(2), Tbrith date, Tdept char(20), Ttele char(11), Temail char(30))')
cursor.execute('create table student(Sno char(10) primary key, Spassword char(20), Sname char(20), Ssex char(2), Sbirth date, Sdept char(20), Smajor char(20), Stele char(11), Semail char(30))')
cursor.execute('create table course(Cno char(3) primary key, Cname char(40), Cpname char(40), Ccredit smallint, Tno char(10), foreign key (Tno) references teacher(Tno))')#Cpname不是外码，但是添加时要验证其正确性
cursor.execute('create table sc(Sno char(10), Cno char(3), grade smallint, foreign key (Sno) references student(Sno), primary key(Sno, Cno), foreign key (Cno) references course(Cno))')
cursor.execute('create table mc(Smajor char(20), Cno char(4), c_e char(1), primary key(Smajor, Cno), foreign key (Smajor) references student(Smajor), foreign key (Cno) references course(Cno))')

# 往teacher表中写入基本信息
with open("teacher.txt", 'r') as f:
        for line in f:
            no = line.split()[0]
            psd = line.split()[0]
            name = line.split()[1]
            sex = line.split()[2]
            dept = line.split()[3]
            insert.insert_teacher_md5(no,psd,name,sex,dept)


# 往student表中写入基本信息
with open("student.txt", 'r') as f:
        for line in f:
            no = line.split()[0]
            psd = line.split()[0]
            name = line.split()[1]
            sex = line.split()[2]
            dept = line.split()[3]
            insert.insert_student_md5(no, psd, name, sex, dept)
cursor.execute('insert into student(Sno, Sname, Smajor) values(\'2018202001\', \'李玉\', \'信息安全\')')
cursor.execute('UPDATE student SET Sbirth = \'19991208\', Smajor = \'信息安全\', Stele = \'18162359079\', Semail = \'1111111@qq.com\' WHERE Sno =\'2017202046\'' )
# 往course表中写入信息,course表信息确定
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'001\', \'信息安全数学基础\', 2, \'1999201122\')')
cursor.execute('insert into course(Cno, Cname, Cpname, Ccredit, Tno) values(\'002\', \'密码学\', \'信息安全数学基础\', 3, \'1999201122\')')# 有先修课
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'099\', \'数学分析1\', 4, \'1980201027\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'100\', \'数学分析2\', 4, \'1999201001\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'101\', \'数学分析3\', 5, \'1984201046\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'102\', \'高等代数\', 4, \'1989201037\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'110\',\'操作系统\', 4, \'1987201056\')')
cursor.execute('insert into course(Cno, Cname, Ccredit, Tno) values(\'111\',\'数据科学导论\', 4, \'1989201114\')')

# 往sc表中写入信息,假定
cursor.execute('insert into sc(Sno, Cno, grade) values(\'2017202046\', \'001\', 90)')
cursor.execute('insert into sc(Sno, Cno) values(\'2017202039\', \'001\')')
cursor.execute('insert into sc(Sno, Cno) values(\'2017202046\', \'110\')')

# 往mc表中写入信息,mc表信息确定
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'099\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'100\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'101\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'数学\', \'102\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'信息安全\', \'001\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'信息安全\', \'002\', \'e\')')#选修
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'计算机\', \'110\', \'c\')')
cursor.execute('insert into mc(Smajor, Cno, c_e) values(\'计算机\', \'111\', \'c\')')


cursor.execute('select * from student')
# cursor.execute('select * from sc')
# cursor.execute('select * from teacher')
# cursor.execute('select * from mc')
values = cursor.fetchall()
print(values)
conn.commit()
conn.close()
