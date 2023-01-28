from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Satish/Downloads/firsttask/second task/database.db'
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
        #if not pic:
            #return 'no pic uploaded'

        if adhar==None:
            filename = secure_filename(pic.filename)
            mimetype=pic.mimetype
            img=adhar2(adhar=adharnum,pic=pic.read(),mimetype=mimetype,name=filename)
            db.session.add(img)
            db.session.commit()
            return 'Image uploaded successfully'

        return 'already uploaded'


    return render_template("adharform.html")
#employee deatail page page 
@app.route('/jdlwdate',methods=['POST','GET'])
def jdlwdate():
    if request.method == "POST":

        cname = request.form['heading']
        jdate= request.form['date1']
        ldate=request.form['date2']
        print('hello')
        print(cname)
        print(jdate)
        print(ldate)
        emp=employ(compname=cname,joindate=jdate,lastdate=ldate)
        
        db.session.add(emp)
        db.session.commit()
        
       

    return render_template("jdlwdate.html")
    
	
#success page 
@app.route('/success',methods=['POST','GET'])
def success():
	return render_template('success.html')


while True:
    with app.app_context():
    	db.create_all()
    	app.run(debug='True')

