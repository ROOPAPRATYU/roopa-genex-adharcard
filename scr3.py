from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from datetime import date
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, MetaData, Table
import pandas as p


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Satish/Downloads/firsttask/second task/database4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


#create table called user
class user(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(200))
    password=db.Column(db.String(200))
    firstname=db.Column(db.String(200))
    lastname=db.Column(db.String(200))
    date1=db.Column(db.String(200))


#create table adhar card
class adhar2(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    adhar=db.Column(db.Text,nullable=False)
    pic=db.Column(db.Text,unique=True,nullable=False)

    name=db.Column(db.Text,nullable=False)
    mimetype=db.Column(db.Text,nullable=False)

class employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    pic1=db.Column(db.Text,unique=True,nullable=False)
    name1=db.Column(db.Text,nullable=False)
    mimetype1=db.Column(db.Text,nullable=False)
    compname=db.Column(db.String(200))
    joindate=db.Column(db.String(200))
    lastdate=db.Column(db.String(200))

class empdoc(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    e1=db.Column(db.String(200))
    e2=db.Column(db.String(200))
    e3=db.Column(db.String(200))
    epic1=db.Column(db.Text,unique=True,nullable=False)
    epic2=db.Column(db.Text,unique=True,nullable=False)
    epic3=db.Column(db.Text,unique=True,nullable=False)
    ed1=db.Column(db.String(200))
    ed2=db.Column(db.String(200))
    ed3=db.Column(db.String(200))
    edpic1=db.Column(db.Text,unique=True,nullable=False)
    edpic2=db.Column(db.Text,unique=True,nullable=False)
    edpic3=db.Column(db.Text,unique=True,nullable=False)
    pass1=db.Column(db.String(200))
    exdate=db.Column(db.String(200))
    passpic=db.Column(db.Text,unique=True,nullable=False)
    pannum=db.Column(db.String(200))
    panpic=db.Column(db.Text,unique=True,nullable=False)
    anum=db.Column(db.String(200))
    adpic=db.Column(db.Text,unique=True,nullable=False)
    form16=db.Column(db.Text,unique=True,nullable=False)




#index page
@app.route('/')
def index():
	return render_template('login.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        email=request.form['emailid']
        password=request.form['passuser']
        print(email)
        print(password)
        login=user.query.filter_by(email=email,password=password).first()
        print(login)
        

        if login is not None:
            return redirect(url_for("adharform"))
    return render_template("login.html")



#signup page
@app.route('/signup',methods=['POST','GET'])
def signup(): 
    if request.method == "POST":
        mail = request.form['email']
        passw = request.form['passwd']
        fname = request.form['fname']
        lname = request.form['lname']
        #mail=str(mail)


        repassw = request.form['repasswd']
        date2 = date.today()
        detail=user.query.filter_by(email=mail).first()
        print(detail)


        try: 
            if detail==None:
                print('hello')
                if passw==repassw:
                    register = user( email = mail, password = passw , firstname = fname, lastname = lname, date1 = date2)
                    db.session.add(register)
                    db.session.commit()
                    print('registration successfull')
            else:
                return render_template("a.html")
                    
            
        except:
            return render_template("a.html")


        return redirect(url_for("login"))
    return render_template("signup.html")

#adhar link page
@app.route('/adharform',methods=['POST','GET'])
def adharform():
    if request.method == "POST":
        adharnum = request.form['adharnum']
        pic = request.files['pict']
        print('hello')
        print(pic)
        print(adharnum)
        adhar = adhar2.query.filter_by(adhar=adharnum).first()
        print(adhar)

        if adhar==None:
            filename = secure_filename(pic.filename)
            mimetype=pic.mimetype
            img=adhar2(adhar=adharnum,pic=pic.read(),mimetype=mimetype,name=filename)
            db.session.add(img)
            db.session.commit()
            return redirect(url_for("emplook"))


        else:
            return render_template("a.html")
    return render_template("adharform.html")

#success page 
@app.route('/emplook',methods=['POST','GET'])
def emplook():
    if request.method == "POST":
        print("hello")
        if request.form["save"]=="SAVE":
            print("hello")
            pic1 = request.files['pictr']
            cname = request.form['company']
            jdate= request.form['jdate']
            ldate=request.form['ldate']
            print('hello')
            print(pic1)
            print(cname)
            print(jdate) 
            print(ldate)
            filename = secure_filename(pic1.filename)
            mimetype1=pic1.mimetype
            emp=employee(compname=cname,joindate=jdate,lastdate=ldate,pic1=pic1.read(),mimetype1=mimetype1,name1=filename)
            db.session.add(emp)
            db.session.commit()
            return redirect(url_for("alldoc"))
           
    
        if request.form["save"]=="UPDATE":
            print("hello")
        
            cname = request.form['company']
            jdate= request.form['jdate']
            ldate=request.form['ldate']
            print(cname)
            print(jdate)
            print(ldate)
            pic1 = request.files['pictr1']
            print('hello')

            filename = secure_filename(pic1.filename)
            mimetype1=pic1.mimetype
            cname1=employee.query.filter_by(compname=cname,joindate=jdate,lastdate=ldate).first()
            print(cname1)
            if cname1==None:
                print("hello")
                emp1=employee(compname=cname,joindate=jdate,lastdate=ldate,pic1=pic1.read(),mimetype1=mimetype1,name1=filename)
                db.session.add(emp1)
                db.session.commit()
                
        
        if request.form['save']=="EDIT":
            print("hello")
            cname = request.form['company']
            jdate= request.form['jdate']
            ldate=request.form['ldate']
            print(cname)
            print(jdate)
            print(ldate)
            pic1 = request.files['pictr1']
            print('hello')
            filename=secure_filename(pic1.filename)
            mimetype1=pic1.mimetype
            print(filename)
            print(mimetype1)
            emp=employee.query.filter_by(joindate=jdate,lastdate=ldate).first()
            print(emp)
            if emp is not None:
                db.session.delete(emp)
                db.session.commit()
                emp1=employee(compname=cname,joindate=jdate,lastdate=ldate,pic1=pic1.read(),mimetype1=mimetype1,name1=filename)
                db.session.add(emp1)
                db.session.commit()
            
            
    
    return render_template("emplook.html",employee=employee.query.all())
        
    

@app.route("/alldoc",methods=["POST","GET"])
def alldoc():
    if request.method == "POST":
        print("hello")
        e1=request.form["e1"]
        e2=request.form["e2"]
        e3=request.form["e3"]
        epic1=request.files["epic1"]
        epic2=request.files["epic2"]
        epic3=request.files["epic3"]
        ed1=request.form["ed1"]
        ed2=request.form["ed2"]
        ed3=request.form["ed3"]
        edpic1=request.files["edpic1"]
        edpic2=request.files["edpic2"]
        edpic3=request.files["edpic3"] 
        pass1=request.form["pass1"]
        exdate=request.form["edate"]
        passpic=request.files["passpic"]
        pannum=request.form["pannum"]
        panpic=request.files["panpic"]
        anum=request.form["anum"]
        apic=request.files["apic"]
        form16=request.files["frm16"]
        print("hello")
        details=empdoc(e1=e1,e2=e2,e3=e3,epic1=epic1.read(),epic2=epic2.read(),epic3=epic3.read(),ed1=ed1,ed2=ed2,ed3=ed3,edpic1=edpic1.read(),edpic2=edpic2.read(),edpic3=edpic3.read(),pass1=pass1,exdate=exdate,passpic=passpic.read(),pannum=pannum,panpic=panpic.read(),anum=anum,adpic=apic.read(),form16=form16.read())
        db.session.add(details)
        db.session.commit()
    return render_template("alldoc.html")
    
    

#success page 
@app.route('/success',methods=['POST','GET'])
def success():
	return render_template('success.html')


while True:
    with app.app_context():
    	db.create_all()
    	app.run(debug='True')
        

