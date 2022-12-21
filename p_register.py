from flask import Flask,render_template,redirect,request
import pymysql
app=Flask(__name__)
@app.route('/')
def dash():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        sql="select * from register"
        cus.execute(sql)
        data=cus.fetchall()
        db.commit()
        #cxvgsgsprint(data)
        return render_template('pdash.html',d=data)
    except Exception:
        print("error")
@app.route('/form')
def form():
    return render_template("form.html")
@app.route('/store',methods=['POST'])
def reg():
    n=request.form['name']
    a=request.form['age']
    t=request.form['treatment']
    da=request.form['entry_date']
    mob=request.form['mob_no']
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        insql="insert into register(patient_name,age,treatment,entry_date,mob_no)values('{}','{}','{}','{}','{}')".format(n,a,t,da,mob)
        cus.execute(insql)
        db.commit()
        return redirect("/")
    except Exception:
        print("error")
@app.route("/msg")
def show():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        sql="select * from register"
        cus.execute(sql)
        data=cus.fetchall()
        db.commit()
        print(data)
        return render_template("register_msg.html",d=data)
    except Exception:
        print("error")
@app.route('/delete/<rid>')
def delete(rid):
    #return "Id is"+rid
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        dsql="delete from register where p_id={}".format(rid)
        cus.execute(dsql)
        db.commit()
        return redirect('/msg')
    except Exception:
        print("The error is",Exception)
@app.route("/edit/<rid>")
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        esql="select * from register where p_id='{}'".format(rid)
        cus.execute(esql)
        data=cus.fetchone()
        print(data)
        return render_template('edit.html',d=data)
    except Exception as e:
        print("error")
@app.route('/update/<rid>', methods=['POST'])
def update(rid):
    n=request.form['name']
    a=request.form['age']
    t=request.form['treatment']
    da=request.form['entry_date']
    mob=request.form['mob_no']
    #return n+a+t+da+mob
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cu=db.cursor()
        usql="update register set patient_name='{}',age='{}',treatment='{}',entry_date='{}',mob_no='{}' where p_id='{}'".format(n,a,t,da,mob,rid)
        cu.execute(usql)
        db.commit()
        return redirect('/')
    except Exception:
        print("error")
        
@app.route("/fever")
def fev():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        sql="select * from register where treatment='fever'"
        cus.execute(sql)
        data=cus.fetchall()
        db.commit()
        print(data)
        return render_template("fever.html",d=data)
    except Exception:
        print("error")
@app.route("/sugar")
def sugar():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="project")
        cus=db.cursor()
        sql="select * from register where treatment='sugar'"
        cus.execute(sql)
        data=cus.fetchall()
        db.commit()
        print(data)
        return render_template("sugar.html",d=data)
    except Exception:
        print("error")
app.run(debug=True)
