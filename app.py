# for how can we integrate ML in websites
from flask import Flask, render_template, request, redirect, session

from db import Database
import api

app = Flask(__name__)
#session['logged_in']=0
dbo=Database()
#@app.route('/') # we create routes or url in flask, this means when someone enter / then this will be executed
#after url when / is written then this will be route this index page
#def index():
#    return "<h1 style='color:green'>Daniyal Khan</h1>"
#app.run(debug=True) #with debug when we change things then dont need to rerun if make changes in code


#flask run on server and it sends html css javascript files to client side
#now our server is pycharm and client is our safari browser

#we integrate page that we make with flask website so for that use render_template, it loads html files
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

#for registration we need a database to store things
#but now we will be using json file, a file and in that store things in dictionary form
#first we bring data from client side(registration page) to flask then to json file store
#we send data with get and post to server from clieant side
#with get we send through url while with post we send sensitive info like password as with get people can see in url

#now for receiving data we use request, and have to tell that by post data is coming to it
@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('user_ka_name')
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')

    response=dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message="registration complete kindly login now") #this is for opening login but
    #with extra info or message
    else:
        return render_template('register.html',message='regsitration not done email already exist')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')
    response=dbo.search(email,password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    #when login is successfully done then we will be sending user to its profile
    #so for sending from one route to another route we use redirect function
    else:
        return render_template('login.html',message='login unsuccessful try again')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text=request.form.get('ner_text')
        response=api.ner(text)
    #result=r''
    #for i in response['entities']:
     #   result+=i['name']+'---->'+i['category']+'\n' #this newline is not going to html show se we send directly respose
        #and do formatting in html code
        return render_template('ner.html',response =response)
    else:
        return redirect('/')
#but we can open /ner.html page from incognitive tab without logging in, so this is wrong, so to avoid this and make
#like only registered people can access we make sessions, sessions make this functionalty happen

#session is not implemented as error is showing but without session working fine

app.run(debug=True)
