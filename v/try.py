import sqlite3

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
    print( info )

get_std_grade('2017202046')

