from models import db, User, Products, Cart

def show_all_users():
    all_users = db.session.query(User).all()
    return all_users

def add_user(user:User):
    db.session.add(user)
    db.session.commit()

def delete_user(user:User):
    db.session.delete(user)
    db.session.commit()

def update_password(user:User, newpass):
    user.password = newpass
    db.session.commit()

def add_to_cart(cart:Cart):
    db.session.add(cart)
    db.session.commit()

def delete_from_cart(cart_to_delete:Cart):
    db.session.delete(cart_to_delete)
    db.session.commit()