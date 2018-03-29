from flask import Flask, render_template 
from app import app

from systeminfo.main import get_platform

@app.route('/') 
def index(): 
    returnDict = {} 
    returnDict['user'] ='COMP30670'# Feel free to put your name here! 
    returnDict['title'] = 'Home'
    returnDict['platform']=get_platform()
    return render_template("index.html", **returnDict)
