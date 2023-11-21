from flask import Flask, render_template, url_for, redirect, session, request
from flaskapp import *
from models import User, Doctors, Products, Creators, Cart
import crud

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<int:user_id>')
def user_page(user_id):
    cartItems = db.session.query(Products).filter_by(product_id=Cart.product_id).where(Cart.user_id == user_id).all()
    user = db.session.query(User).filter_by(user_id=session['uid']).first()
    return render_template('user page.html', cartItems=cartItems, user=user)

@app.route('/editUser', methods = ["POST", "GET"])
def editUser():
    user = User.query.get_or_404(session['uid'])
    
    if request.method == "POST":
        user.user_name = request.form['user_name'].capitalize()
        user.user_surname = request.form['user_surname'].capitalize()
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('user_page', user_id=user.user_id))

    return render_template('edit user.html', user=user)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and len(request.form)>2:
        name = request.form['name'].capitalize()
        surname = request.form['surname'].capitalize()
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']

        data = db.session.query(User).filter_by(login=request.form['login']).first()

        if data:
            return render_template('login.html', report='Already exists!')
        else: 
            new_user = User(email,login, name, surname, password)
            crud.add_user(new_user)
            return render_template('login.html', report='Registration successful')

        
    elif request.method == 'POST' and len(request.form) == 2:
        login = request.form['login']
        password = request.form['password']

        user = db.session.query(User).filter_by(login=login, password=password).first()
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['username'] = user.login
            return redirect(url_for('user_page', user_id=user.user_id))
        else:
            return render_template('login.html', report='Invalid username or password')
    
    return render_template('login.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/products', methods = ['POST', 'GET'])
def medicine():
    if request.method == "POST":
        searchRes = request.form['search']
        products = db.session.query(Products).filter(Products.product_name.like('%' + searchRes + '%'))
        return render_template('medicine.html', products=products)
    products = db.session.query(Products).all()
    return render_template('medicine.html', products = products)

@app.route('/addToCart/<int:product_id>')
def cart(product_id):
    try:
        if session['authenticated'] :
            item = db.session.query(Cart).filter_by(product_id=product_id).where(Cart.user_id == session['uid']).all()
            if item:
                return redirect(url_for('medicine'))
            else:
                product = Cart(session['uid'], product_id)
                crud.add_to_cart(product)
                return redirect(url_for('medicine'))
    except:
        return render_template('login.html', report='You are not logged in')
    
@app.route('/deleteFromCart/<int:id>')
def deleteFromCart(id):
    try:
        cart_to_delete = db.session.query(Cart).filter_by(product_id=id).where(Cart.user_id == session['uid']).first()
        crud.delete_from_cart(cart_to_delete)
        return redirect(url_for('user_page', user_id=session['uid']))
    except:
        return redirect(url_for('user_page', user_id=session['uid']))
    

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    creators = db.session.query(Creators).all()
    return render_template('contact.html', creators=creators)

@app.route('/forgot_password', methods=["POST", "GET"])
def forgotPass():
    if request.method == "POST":
        change = db.session.query(User).filter_by(login=request.form['login']).first()
        newpass = request.form['newPassword']

        if change:
            crud.update_password(change, newpass)
            return render_template('login.html', report='Password restored succesfuly')
        else:
            return render_template('login.html', report='Username does not exist')

    return render_template('change password.html')

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('home'))
