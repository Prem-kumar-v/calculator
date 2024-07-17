from flask import Flask,render_template,url_for,redirect,session,request,flash
from flask_mail import Mail,Message
import random

app=Flask(__name__,static_folder="static")

@app.route("/",methods=["GET","POST"])
def index():
    if 'calc' in request.form:
        if request.method=="POST":
            
            fname=request.form["fname"]
            lname=request.form["lname"]
            
            app.config['MAIL_SERVER']='smtp.gmail.com'  
            app.config['MAIL_PORT']=465  
            app.config['MAIL_USERNAME'] ='sportsclub3115@gmail.com'
            app.config['MAIL_PASSWORD'] ='lkbq ewpe spbz qsya'
            app.config['MAIL_USE_TLS'] = False  
            app.config['MAIL_USE_SSL'] = True  
            mail=Mail(app) 

            msg=Message('WELCOME TO SPORTSCLUB TURF UNIVERSE',sender='sportsclub3115@gmail.com',recipients=['kumar6603517@gmail.com'])    
            msg.body=fname + lname
                         
                         
            mail.send(msg)
            return redirect(url_for("love"))
            
            
    return render_template("home.html") 
    
    
@app.route("/love",methods=["GET","POST"])
def love():
      
      number = ['90','91','92','93','94','95','96','97','98','99','100']
      char=random.choice(number)
    
    
    
      return render_template("show.html",data=char)
    
if(__name__=='__main__'):
     app.secret_key="flask"
     app.run(debug=True)