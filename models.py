from flaskapp import db, app

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    login = db.Column(db.String(200), unique=True, nullable=False)
    user_name = db.Column(db.String(200))
    user_surname = db.Column(db.String(200))
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, email, login, user_name, user_surname, password):
        self.email = email
        self.login = login
        self.user_name = user_name
        self.user_surname = user_surname
        self.password = password


class Doctors(db.Model):
    __tablename__ = 'doctors'
    doctor_id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(200), nullable=True)
    doctor_surname = db.Column(db.String(200), nullable=True)
    doctor_specialization = db.Column(db.String(200), nullable=True)

    def __init__(self, doctor_name, doctor_surname, doctor_specialization):
        self.deoctor_name = doctor_name
        self.doctor_surname = doctor_surname
        self.doctor_specialization = doctor_specialization


class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=True)
    product_price = db.Column(db.Integer, nullable=True)
    product_description = db.Column(db.String(200), nullable=True)
    product_image = db.Column(db.String(200), nullable=True)

    def __init__(self, product_name, product_price, product_description):
        self.product_name = product_name
        self.prodcut_price = product_price
        self.product_description = product_description


class Creators(db.Model):
    __tablename__ = 'creators'
    creator_id = db.Column(db.Integer, primary_key=True)
    creator_name = db.Column(db.String(200), nullable=True)
    creator_surname = db.Column(db.String(200), nullable=True)
    creator_role = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)

    def __init__(self, creator_name, creator_surname, creator_role):
        self.creator_name = creator_name
        self.creator_surname = creator_surname
        self.creator_role = creator_role

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id', ondelete='CASCADE'))

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

with app.app_context():
    db.init_app(app)
    db.create_all()