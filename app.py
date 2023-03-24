import psycopg2
from flask import Flask, render_template, session, redirect, url_for

app = Flask('SalonUnique')
app.secret_key = '99989'

conn = psycopg2.connect(
    host="localhost",
    database="project",
    user="postgres",
    password="projectwon5"
)

@app.route('/private/')
def private():
    if session.get('username') != 'owner':
        return redirect(url_for('login'))
    else:
        return render_template('private.html')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '0000':
            session['username'] = 'admin'
            return redirect(url_for('private'))
        else:
            return render_template('login.html', error='Invalid Credentials')
    else:
        return render_template('login.html')

@app.route('/home/')
def home():
    return render_template('home.html', title='Salon Unique')

@app.route('/clients/')
def clients():
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    return render_template('clients.html', clients=clients)