import sqlite3
from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
# import create
import check
import get
import insert

app = Flask(__name__)
app.secret_key = 'course selection system'  # MD5加密


# 初始登陆界面
@app.route('/')
def home():
    return render_template('login.html', flag=0)


# 登陆界面
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html', flag=0)


@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']
    login_suc = check.login_md5(user_id, password)
    if login_suc == 1:  # student
        return render_template('me_s.html', user_id=user_id, flag=0)
    elif login_suc == 2:  # teacher
        return render_template('me_t.html', user_id=user_id, flag=0)
    else:
        return render_template('login.html', flag=-1)

# 学生成功登录之后的跳转页面
@app.route('/me_s/<user_id>')
def meStudent_form(user_id):
        return render_template('me_s.html', user_id=user_id)

# 老师成功登录之后的跳转页面
@app.route('/me_t/<user_id>')
def meTeacher_form(user_id):
        return render_template('me_t.html', user_id=user_id)

# 学生主页
@app.route('/meStudent/<user_id>')
def meStudent(user_id):
    class sBSCInfo(FlaskForm):
        pass

    Info = get.get_student_BSCinfo(user_id)
    setattr(sBSCInfo, "form" + str(0), StringField("姓名"))
    setattr(sBSCInfo, "form" + str(1), StringField("学号"))
    setattr(sBSCInfo, "form" + str(2), StringField("学院"))
    m_info = sBSCInfo()
    c = 0
    for field in m_info:
        if c == len(Info):
            break
        field.data = Info[c]
        c += 1
    return render_template('meStudent.html', user_information=m_info, user_id=user_id)


# 老师主页
@app.route('/meTeacher/<user_id>')
def meTeacher(user_id):
    class tBSCInfo(FlaskForm):
        pass

    Info = get.get_teacher_BSCinfo(user_id)
    setattr(tBSCInfo, "form" + str(0), StringField("姓名"))
    setattr(tBSCInfo, "form" + str(1), StringField("教职工号"))
    setattr(tBSCInfo, "form" + str(2), StringField("学院"))
    m_info = tBSCInfo()
    c = 0
    for field in m_info:
        if c == len(Info):
            break
        field.data = Info[c]
        c += 1
    return render_template('meTeacher.html', user_information=m_info, user_id=user_id)

# 学生个人信息
@app.route('/info_s/<user_id>')
def stu_info(user_id):
    class sInfo(FlaskForm):
        pass

    Info = get.get_student_info(user_id)
    setattr(sInfo, "form" + str(0), StringField("姓名"))
    setattr(sInfo, "form" + str(1), StringField("学号"))
    setattr(sInfo, "form" + str(2), StringField("性别"))
    setattr(sInfo, "form" + str(3), StringField("生日"))
    setattr(sInfo, "form" + str(4), StringField("学院"))
    setattr(sInfo, "form" + str(5), StringField("专业"))
    setattr(sInfo, "form" + str(6), StringField("电话号码"))
    setattr(sInfo, "form" + str(7), StringField("邮箱"))
    m_info = sInfo()
    c = 0
    for field in m_info:
        if c == len(Info):
            break
        field.data = Info[c]
        c += 1
    return render_template("info_s.html", user_information=m_info, user_id=user_id)

# 老师个人信息
@app.route('/info_t/<user_id>')
def tch_info(user_id):
    class tInfo(FlaskForm):
        pass

    Info = get.get_teacher_info(user_id)
    setattr(tInfo, "form" + str(0), StringField("姓名"))
    setattr(tInfo, "form" + str(1), StringField("学号"))
    setattr(tInfo, "form" + str(2), StringField("性别"))
    setattr(tInfo, "form" + str(3), StringField("生日"))
    setattr(tInfo, "form" + str(4), StringField("学院"))
    setattr(tInfo, "form" + str(5), StringField("电话号码"))
    setattr(tInfo, "form" + str(6), StringField("邮箱"))
    m_info = tInfo()
    c = 0
    for field in m_info:
        if c == len(Info):
            break
        field.data = Info[c]
        c += 1
    return render_template("info_t.html", user_information=m_info, user_id=user_id)

# 修改个人信息
@app.route('/info_s_edit/<user_id>')
def stu_info_edit_form(user_id):
    return render_template('info_s_edit.html', user_id=user_id, flag=0)


@app.route('/info_s_edit/<user_id>', methods=['POST'])
def stu_info_edit(user_id):
    name = request.form['name']
    std_id = request.form['std_id']
    sex = request.form['sex']
    birth = request.form['birth']
    dept = request.form['dept']
    major = request.form['major']
    tele = request.form['tele']
    email = request.form['email']
    s_psd = request.form['std_psd']
    s_psd2 = request.form['std_psd2']

    info_s_edit_suc = check.info_s_edit(user_id, name, std_id, dept, tele, email, s_psd, s_psd2)
    if info_s_edit_suc == 7:
        insert.insert_stu_psd_md5(std_id, s_psd)
        insert.insert_std_last(user_id, birth, major, tele, email)  # 将学生信息添加进去
        return render_template('info_s_edit.html', user_id=user_id, flag=0)
    elif info_s_edit_suc == 1:
        return render_template('info_s_edit.html', user_id=user_id, flag=1)
    elif info_s_edit_suc == 2:
        return render_template('info_s_edit.html', user_id=user_id, flag=2)
    elif info_s_edit_suc == 3:
        return render_template('info_s_edit.html', user_id=user_id, flag=3)
    elif info_s_edit_suc == 4:
        return render_template('info_s_edit.html', user_id=user_id, flag=4)
    elif info_s_edit_suc == 5:
        return render_template('info_s_edit.html', user_id=user_id, flag=5)
    elif info_s_edit_suc == 6:
        return render_template('info_s_edit.html', user_id=user_id, flag=6)


@app.route('/info_t_edit/<user_id>', methods=['POST'])
def tch_info_edit(user_id):

    return render_template("info_t_edit.html", user_id=user_id)

# 录入新生
@app.route('/insert', methods=['GET'])
def inserts_form():
    return render_template('insert.html', flag=0)


@app.route('/insert', methods=['POST'])
def inserts():
    input_file_name = request.form['input_file_name']
    typeST = request.form['type']
    with open(input_file_name, 'w') as f:
        for line in f:
            no = line.split()[0]
            psd = line.split()[0]
            name = line.split()[1]
            sex = line.split()[2]
            dept = line.split()[3]
            if typeST == "student":
                insert.insert_student_md5(no, psd, name, sex, dept)
            elif typeST == "teacher":
                insert.insert_teacher_md5(no, psd, name, sex, dept)
            return render_template('insert.html', flag=1)

# 老师的课程
@app.route('/course_t/<user_id>')
def tch_course(user_id):
    class tCrs(FlaskForm):
        pass

    Info = get.get_tch_course(user_id)
    print(Info)
    # [['001', '信息安全数学基础___None___2___1999201122'], ['002', '密码学___信息安全数学基础___3___1999201122']]
    if len(Info) == 0:
        setattr(tCrs, "form" + str(0), StringField("无"))
        c_info = tCrs()
        for field in c_info:
            field.data = "无"
    else:
        for i in range(len(Info)):
            setattr(tCrs, "form" + str(i), StringField(Info[i][0]))
        c_info = tCrs()
        c = 0
        for field in c_info:
            if c == len(Info):
                break
            field.data = Info[c][1]
            c += 1
    return render_template("course_t.html", crs_information=c_info, user_id=user_id)

# 老师的课程详情：学生名单
@app.route('/one_course/<crs_id>')
def course_details(crs_id):
    class std_gra(FlaskForm):
        pass

    Info = get.get_crs_stds(crs_id)
    # [['2017202039___刘李', None], ['2017202046___李一', None]]
    for i in range(len(Info)):
        setattr(std_gra, "form" + str(i), StringField(Info[i][0]))
    sg_info = std_gra()
    c = 0
    for field in sg_info:
        if c == len(Info):
            break
        field.data = Info[c][1]
        c += 1
    return render_template("one_course.html", information=sg_info, crs_id=crs_id)
'''
# 打分
@app.route('/mark/<crs_id>', methods=['POST'])
def mark(crs_id):

    return render_template("mark.html", information=sg_info, crs_id=crs_id)
'''
# 我的课程表
@app.route('/course_s/<user_id>')
def stu_course(user_id):
    class sCrs(FlaskForm):
        pass

    Info = get.get_std_course(user_id)
    print(Info)
    if len(Info) == 0:
        setattr(sCrs, "form" + str(0), StringField(0))
        sc_info = sCrs()
        for field in sc_info:
            field.data = "无"
    else:
        for i in range(len(Info)):
            setattr(sCrs, "form" + str(i), StringField(i))
        sc_info = sCrs()
        c = 0
        for field in sc_info:
            if c == len(Info):
                break
            field.data = Info[c]
            c += 1
    return render_template("course_s.html", information=sc_info, user_id=user_id)

# 我的成绩
@app.route('/grade/<user_id>')
def stu_grade(user_id):
    class s_gra(FlaskForm):
        pass

    Info = get.get_std_grade(user_id)
    print(Info)
    if len(Info) == 0:
        setattr(s_gra, "form" + str(0), StringField("无"))
        sg_info = s_gra()
        for field in sg_info:
            field.data = "无"
    else:
        for i in range(len(Info)):
            setattr(s_gra, "form" + str(i), StringField(Info[i][0]))
        sg_info = s_gra()
        c = 0
        for field in sg_info:
            if c == len(Info):
                break
            field.data = Info[c][1]
            c += 1
    return render_template("grade.html", information=sg_info, user_id=user_id)


@app.route('/chos/<user_id>', methods=['GET'])
def choose(user_id):
    return render_template("chos.html", user_id=user_id, flag=0)
'''
# 选课界面
@app.route('/chos/<user_id>', methods=['POST'])
def choose(user_id):
    num = request.form['num']
    class Crs(FlaskForm):
        pass

    Info = get.get_courses(user_id, 'e')
    print(Info)
    if len(Info) == 0:
        setattr(Crs, "form" + str(0), StringField(0))
        c_info = Crs()
        for field in c_info:
            field.data = "无"
    else:
        for i in range(len(Info)):
            setattr(Crs, "form" + str(i), StringField(i))
        c_info = Crs()
        c = 0
        for field in c_info:
            if c == len(Info):
                break
            field.data = Info[c]
            c += 1
	 return render_template("chos.html", information=c_info, user_id=user_id, flag=0)
'''

if __name__ == '__main__':
    app.run()
