import sqlite3
import hashlib
import get
import re


def login_md5(user_id, password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    password = m.hexdigest()   # 密码是加密过的
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute('select Sno, Spassword from student')
    values1 = cursor.fetchall()
    cursor.execute('select Tno, Tpassword from teacher')
    values2 = cursor.fetchall()
    conn.commit()
    conn.close()
    if (user_id, password) in values1:
        return 1
    elif(user_id, password) in values2:
        return 2
    else:
        return -1


def validate_email(email_str):
    if len(email_str) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email_str) != None:
            return True
    return False


def info_s_edit(user_id, name, std_id, dept, tele, email, s_psd, s_psd2):
    BSCinfo = get.get_student_BSCinfo(user_id)  # 元组(name,no,dept)
    if name != BSCinfo[0]:
        return 1
    elif std_id != user_id:
        return 2
    elif dept != BSCinfo[3]:
        return 3
    elif len(tele) != 11 or not tele.isdigit:
        return 4
    elif not validate_email(email):
        return 5
    elif s_psd != s_psd2 or not s_psd.isalnum() or len(s_psd) > 20 or len(s_psd) < 3:
        return 6
    else:
        return 7