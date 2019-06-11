import sqlite3


def get_student_BSCinfo(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select * from student where Sno = \'" + user_id + "\'"
    cursor.execute(s)
    single = cursor.fetchall()
    conn.commit()
    conn.close()
    # Sno, Spassword, Sname, Ssex, Sbirth, Sdept, Smajor, Stele, Semail
    info = (single[0][2], single[0][0], single[0][5]) # 元组(name,no,dept)
    return info


def get_student_info(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select * from student where Sno = \'" + user_id + "\'"
    cursor.execute(s)
    single = cursor.fetchall()
    conn.commit()
    conn.close()
    # Sno, Spassword, Sname, Ssex, Sbirth, Sdept, Smajor, Stele, Semail
    info = (single[0][2], single[0][0], single[0][3], single[0][4], single[0][5], single[0][6], single[0][7], single[0][8])  # 除psd
    return info


def get_teacher_BSCinfo(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select * from teacher where Tno = \'" + user_id + "\'"
    cursor.execute(s)
    single = cursor.fetchall()
    conn.commit()
    conn.close()
    # Tno, Tpassword, Tname, Tsex, Tbrith, Tdept, Ttele, Temail
    info = (single[0][2], single[0][0], single[0][5])  # name,no,dept
    return info


def get_teacher_info(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select * from teacher where Tno = \'" + user_id + "\'"
    cursor.execute(s)
    single = cursor.fetchall()
    conn.commit()
    conn.close()
    # Tno, Tpassword, Tname, Tsex, Tbrith, Tdept, Ttele, Temail
    info = (single[0][2], single[0][0], single[0][3], single[0][4], single[0][5], single[0][6], single[0][7])  # 除psd
    return info


def get_tch_course(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select * from course where Tno = \'" + user_id + "\'"
    cursor.execute(s)
    all_crs = cursor.fetchall()
    conn.commit()
    conn.close()
    # all_crs: [('001', '信息安全数学基础', None, 2, '1999201122'), ('002', '密码学', '信息安全数学基础', 3, '1999201122')]
    info = []
    for i in range(len(all_crs)):
        single = []
        key = ""
        value = ""
        for j in range(len(all_crs[i])):
            if j == 0:
                key = all_crs[i][j]
            elif j == len(all_crs[i]) - 2:
                value += str(all_crs[i][j])
                all_crs[i] = value
                break
            else:
                value += str(all_crs[i][j]) + "___"
        single.append(key)
        single.append(value)
        info.append(single)
    return info


def get_crs_stds(crs_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select distinct sc.Sno, Sname, grade from sc, student where Cno = \'" + crs_id + "\' and sc.Sno = student.Sno"
    cursor.execute(s)
    all_std = cursor.fetchall()
    conn.commit()
    conn.close()
    # all_std: [('2017202039', '刘李'), ('2017202046', '李一')]
    info = []

    for i in range(len(all_std)):
        single = []
        key = str(all_std[i][0]) + "___" + str(all_std[i][1])
        try:
            value = all_std[2]
        except IndexError:
            value = None
        single.append(key)
        single.append(value)
        info.append(single)
    return info


def get_courses(user_id, c_e):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select c.Cno, Cname, Cpname, Ccredit, Tname, t.Tno from student s, mc, course c, teacher t where s.Smajor = mc.Smajor and mc.Cno = c.Cno and c.Tno = t.Tno and c_e = \'" + c_e + "\' and s.Sno = \'" + user_id + "\'"
    cursor.execute(s)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    print(result)
    # [('001', '信息安全数学基础', None, 2, '1999201122')]
    # [('002', '密码学', '信息安全数学基础', 3, '1999201122')]
    info = []
    for i in range(len(result)):
        single = ""
        for j in range(len(result[i])):
            if j == len(result[i]) - 1:
                single += str(result[i][j])
                result[i] = single
                break
            else:
                single += str(result[i][j]) + "___"
        info.append(single)
    return info


def get_std_course(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select c.Cno, Cname, Cpname, Ccredit, Tname, t.Tno from student s, sc, course c, teacher t where s.Sno = sc.Sno and sc.Cno = c.Cno and c.Tno = t.Tno  and s.Sno = \'" + user_id + "\'"
    cursor.execute(s)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    info = []
    for i in range(len(result)):
        single = ""
        for j in range(len(result[i])):
            if j == len(result[i]) - 1:
                single += str(result[i][j])
                result[i] = single
                break
            else:
                single += str(result[i][j]) + "___"
        info.append(single)
    return info


def get_GPA(grade):
    if grade >= 90:
        return 4.0
    elif grade >= 86:
        return 3.7
    elif grade >= 83:
        return 3.3
    elif grade >= 80:
        return 3.0
    elif grade >= 76:
        return 2.7
    elif grade >= 73:
        return 2.3
    elif grade >= 70:
        return 2.0
    elif grade >= 66:
        return 1.7
    elif grade >= 63:
        return 1.3
    elif grade >= 60:
        return 1.0
    else:
        return 0.0


def get_std_grade(user_id):
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    s = "select c.Cno, grade from sc, course c where c.Cno = sc.Cno and sc.Sno = \'" + user_id + "\'"
    cursor.execute(s)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    info = []
    for i in range(len(result)):
        single = []
        grade_G = ""
        single.append(result[i][0])
        grade_G += str(result[i][1])
        if result[i][1] != None:
            grade_G +='___'
            grade_G += str(get_GPA(result[i][1]))
        single.append(grade_G)
        info.append(single)
    return info   # [['001', '90___4.0'], ['110', 'None']]
