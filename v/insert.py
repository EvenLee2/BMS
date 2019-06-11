
import sqlite3
import hashlib


def insert_student_md5(no, psd, name, sex, dept):
    # m = hashlib.md5()
    # m.update(name.encode('utf-8'))
    # name = m.hexdigest()  由于姓名要直接输出，所以改为直接存储
    m = hashlib.md5()   # 将姓名、密码MD5加密保存的话，必须换一个m，不然会改变password——MD5
    m.update(psd.encode('utf-8'))
    psd = m.hexdigest()
    s = 'insert into student(Sno, Spassword, Sname, Ssex, Sdept) values('
    s = s + '\'' + no + '\',\'' + psd + '\',\'' + name + '\',\'' + sex + '\',\'' + dept + '\')'
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute(s)
    conn.commit()
    conn.close()


def insert_teacher_md5(no, psd, name, sex, dept):
    # 将密码MD5加密保存
    m = hashlib.md5()
    m.update(psd.encode('utf-8'))
    psd = m.hexdigest()
    s = 'insert into teacher(Tno, Tpassword, Tname, Tsex, Tdept) values('
    s = s + '\'' + no + '\'' + ',' + '\'' + psd + '\'' + ',' + '\'' + name + '\'' + ',' + '\'' + sex + '\'' + ',' + '\'' + dept + '\'' + ')'
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute(s)
    conn.commit()


def insert_stu_psd_md5(no, psd):
    # 修改密码
    m = hashlib.md5()   # 将姓名、密码MD5加密保存的话，必须换一个m，不然会改变password——MD5
    m.update(psd.encode('utf-8'))
    psd = m.hexdigest()
    s = "UPDATE student SET Spassword = \'" + psd + "\' WHERE Sno =\'" + no + "\'"
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute(s)
    conn.commit()
    conn.close()


def insert_std_last(no, birth, major, tele, email):
    s = "UPDATE student SET Sbirth = \'" + birth + "\' , Smajor = \'" + major + "\' , Stele = \'" + tele + "\' , Semail = \'" + email   + "\' WHERE Sno =\'" + no + "\'"
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute(s)
    conn.commit()
    conn.close()