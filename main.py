#import flask
from flask import Flask,render_template
import socket
app=Flask(__name__)

def fetchdetails():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)


@app.route("/")
def index():
    a=20
    b=30
    final=a+b
    return render_template("index.html",score=final)

@app.route("/career")
def career():
    kolo="System engineer needed in our company"
    
    # Json code to list employee scores

    return render_template("career.html",career=kolo)

@app.route("/hostfetch")
def details():
    hostname,hostip=fetchdetails()
    return render_template("hostfetch.html", hostadd=hostname,ip=hostip)


@app.route("/contactus")
def contactus():
    kiki="Office: 23, regent house, London"
    phone= "+44-804-5637-892"
    
    return render_template("contactus.html", contactus=kiki,telephone=phone)

if __name__== '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)