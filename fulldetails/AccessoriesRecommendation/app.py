import MySQLdb
import mysql.connector
from flask import Flask, request, render_template, url_for, session, redirect
from flask_wtf import CSRFProtect
import os

app=Flask(__name__)
app.secret_key="abcd12345"
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/newuser", methods=["GET","POST"])
def new_user():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()

        name = request.form["name"]
        gender = request.form["gender"]
        dob = request.form["dob"]
        age = request.form["age"]
        city = request.form["city"]
        mailid = request.form["mailid"]
        mobileno = request.form["mobileno"]
        uid = request.form["uid"]
        pwd = request.form["pwd"]
        c1.execute("INSERT INTO NewUser VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name, gender, dob, age, city, mailid, mobileno, uid, pwd))
        db.commit()
        return render_template("newuser.html", msg="User Details Registered!!!")
    return render_template("newuser.html")

@app.route("/userlogin", methods=["GET","POST"])
def user_login():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()

        uid=request.form["uid"]
        pwd=request.form["pwd"]
        c1.execute("select * from NewUser where userid='%s' and password='%s'"%(uid,pwd))
        if c1.rowcount>=1:
            row=c1.fetchone()
            session["userid"]=uid
            session['gender']=row[1]
            return render_template("userhome.html")
        else:
            return render_template("userlogin.html", msg="Your Login attempt was not successful. Please try again!!")
    return render_template("userlogin.html")

@app.route("/adminlogin", methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        uid=request.form["uid"]
        pwd=request.form["pwd"]

        if uid=="Admin" and pwd=="Admin":
            return render_template("adminhome.html")
        else:
            return render_template("adminlogin.html", msg="Your Login attempt was not successful. Please try again!!")
    return render_template("adminlogin.html")


@app.route("/myprofile")
def my_profile():
    db=MySQLdb.connect("localhost","root","","AccessoriesRecommendation")
    c1 = db.cursor()
    uid=str(session["userid"])
    c1.execute("select * from NewUser where userid='%s'"%uid)
    if c1!=None:
        row=c1.fetchone()
        return render_template("myprofile.html", name=row[0], gender=row[1], dob=row[2], age=row[3], city=row[4], mailid=row[5], mobileno=row[6])

@app.route("/upload_dress", methods = ['GET', 'POST'])
def upload_dress():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()
        dress_name = request.form["dress_name"]
        gender = request.form["gender"]
        dress_category = request.form["dress_category"]
        f = request.files['file']
        f.save(os.getcwd() + "\\static\\dresses\\" + f.filename)
        c1.execute("insert into DressDetails values('%s','%s','%s','%s')" % (dress_name, gender, dress_category, f.filename))
        db.commit()
        return render_template("upload_dress.html", msg="Dress Dataset Uploaded Successfully!!")
    else:
        return render_template("upload_dress.html")

@app.route("/upload", methods = ['GET', 'POST'])
def upload_accessories():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()
        aid=int(request.form["aid"])
        aname=request.form["aname"]
        gender=request.form["gender"]
        dress=request.form["dress"]
        f = request.files['file']
        f.save(os.getcwd()+"\\static\\accessories\\"+f.filename)
        c1.execute("insert into Accessories values(%d,'%s','%s','%s','%s')"%(aid,aname,gender,dress,f.filename))
        db.commit()

        c1.execute("select ifnull(max(accessory_id),0)+1 from Accessories")
        row = c1.fetchone()
        aid = row[0]
        return render_template("upload_accessories.html",aid=aid,msg="Accessories Uploaded Successfully!!")
    else:
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()
        c1.execute("select ifnull(max(accessory_id),0)+1 from Accessories")
        row=c1.fetchone()
        aid=row[0]
        return render_template("upload_accessories.html",aid=aid)

@app.route("/view_dresses")
def view_dresses():
    db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
    c1 = db.cursor()
    c1.execute("select * from DressDetails")
    data = c1.fetchall()
    return render_template("view_dresses.html", data=data,path=os.getcwd())

@app.route("/view_accessories")
def view_accessories():
    db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
    c1 = db.cursor()
    c1.execute("select * from Accessories")
    data = c1.fetchall()
    return render_template("view_accessories.html", data=data,path=os.getcwd())

@app.route("/recommendation", methods = ['GET', 'POST'])
def recommendation():
    if request.method == "POST":
        db = MySQLdb.connect("localhost", "root", "", "AccessoriesRecommendation")
        c1 = db.cursor()
        f = request.files['file']
        DressName=""
        DressCategory=""
        gender=""
        c1.execute("select DressName,DressCategory,gender from DressDetails where DressImage='%s'"%(f.filename))
        if c1!=None:
            row=c1.fetchone()
            DressName=row[0]
            DressCategory=row[1]
            gender=row[2]

        c1.execute("select * from Accessories where DressType=(select DressCategory from DressDetails where DressImage='%s') \
        and gender=(select gender from DressDetails where DressImage='%s')"%(f.filename,f.filename))
        data=c1.fetchall()
        return render_template("prediction.html", DressName=DressName, DressCategory=DressCategory, gender=gender, data=data)
    else:
        return render_template("recommendation.html")

@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)