from flask import Flask, render_template, url_for, redirect, request
import smtplib


app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = "098&^%^6543%%$#$t455#$%#%$^%%$%^Y"
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
@app.route('/sendmail', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')




