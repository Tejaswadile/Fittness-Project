from flask import *
from DBM import *
app=Flask(__name__,static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register")
def sec():
    return render_template("register.html")
@app.route("/login")
def third():
    return render_template("login.html")
@app.route("/admin")
def adlog():
    t=selectAllEmp()
    return render_template("showdetails.html",elist=t)

@app.route("/adddata",methods=["post"])
def add():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    phno=request.form["phno"]
    t=(name,email,password,phno)
    addEmp(t)
    return redirect("/")
    
@app.route("/welcome")
def welcome():
    email=request.args.get("email")
    t=getdetails(email)
    return render_template("welcome.html",t=t)


@app.route("/log",methods=["post"])
def lg():
    email=request.form["email"]
    password=request.form["password"]
    t1=checklg(email)
    if email in t1:
        return redirect(f"/welcome?email={email}")
    else:
        return redirect("/login")
@app.route("/edit")
def ed():
    email=request.args.get("email")
    el=selectEmpById(email)
    return render_template("editform.html",t=el)

@app.route("/upd",methods=["post"])
def upd():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    phno=request.form["phno"]
    t=(name,email,password,phno,email)
    updateEmp(t)
    return redirect ("/showdetails")
@app.route("/del")
def se():
    email=request.args.get("email")
    print(email) 
    deleteEmp(email)
    return redirect ("/admin")
  
@app.route("/addlogcheck",methods=["post"])
def addlogcheck():
    email=request.form["email"]
    password=request.form["password"]
    ademail="powerlift@gmail.com"
    adpassword="power"
    if email==ademail and password==adpassword:
        return redirect("/admin")
    else:
        return redirect("/adminlog")

@app.route("/adminlog")
def adminlog():
    return render_template("adminlogin.html")







if __name__=="__main__":
    app.run(debug=True)
