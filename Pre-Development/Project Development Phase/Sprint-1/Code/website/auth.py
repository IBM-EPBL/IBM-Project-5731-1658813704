from flask import Blueprint, render_template, request, flash, redirect, url_for,session
from . import conn
import ibm_db
import hashlib

auth = Blueprint('views', __name__)


@auth.route('/signin', methods=['POST', 'GET'])
def login():
    
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        password = bytes(password,'utf-8')
        password = hashlib.sha256(password).hexdigest()

        #query the db
        sql = "SELECT * FROM users WHERE email =? AND password=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        acc = ibm_db.fetch_assoc(stmt)
        if not acc:
           flash('User Does not exist in our Database Please Sign Up First', category='error')
        if acc:
            session['login_status'] = True
            session['username'] = email
            session['user_id'] = email.split('@')[0]
            user_id = email.split('@')[0]
            print(user_id)
            return redirect('/')
            
    return render_template('/components/signin.html')

@auth.route('/logout')
def logout():
    session.pop('login_status',None)
    session.pop('user_id',None)
    session.pop('username',None)


    return redirect(url_for('news.home'))

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        password = bytes(password,'utf-8')
        password = hashlib.sha256(password).hexdigest()
        
        sql = "SELECT * FROM users WHERE email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        acc = ibm_db.fetch_assoc(stmt)
        if acc:
            flash('Email Already exists in our Database Please Sign in', category='error')
      
        insert_sql = "INSERT INTO  users VALUES (?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, name)
        ibm_db.bind_param(prep_stmt, 2, email)
        ibm_db.bind_param(prep_stmt, 3, password)
        ibm_db.execute(prep_stmt)
        flash('Account Created Successfully !', category='success')
        return redirect(url_for('views.login'))
    return render_template('/components/register.html')
