import email
import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='fitness')
    
def addEmp(t):
    db=getConnection()
    sql='insert into user values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllEmp():
    db=getConnection()
    sql='select * from user'
    cr=db.cursor()
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

    
def deleteEmp(email):
    db=getConnection()
    sql='delete from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,email)
    db.commit()
    db.close()

def selectEmpById(email):
    db=getConnection()
    sql='select * from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,email)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update user set name=%s,email=%s,password=%s,phno=%s where email=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def checklg(t):
    db=getConnection()
    sql='select email,password from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]


def getdetails(email):
    db=getConnection()
    sql='select name,email,phno from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0]