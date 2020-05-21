from flask import Flask, render_template, flash, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, current_user, LoginManager, logout_user


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from model import MemberData

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login'
login.login_message_category = 'info'


@login.user_loader
def load_user(user_id):
    return MemberData.query.filter(id == int(user_id)).first()


@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    from form import FormRegister
    from model import MemberData  
    
    form =FormRegister()
    if form.validate_on_submit():
        user = MemberData(
            UserID = form.UserID.data,
            MemberName = form.MemberName.data,
            MemberPhone = form.MemberPhone.data,
            MemberMail = form.MemberMail.data,
            MemberAccount = form.MemberAccount.data,
            MemberPassword = bcrypt.generate_password_hash(form.MemberPassword.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Congrates, registration success', category='success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])#########################
def login():
    from form import FormLogin
    from model import MemberData  
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormLogin()
    if form.validate_on_submit():
        MemberAccount = form.MemberAccount.data
        MemberPassword = form.MemberPassword.data
        remember = form.remember.data
        user = MemberData.query.filter_by(MemberAccount=MemberAccount).first()
        if user and bcrypt.check_password_hash(user.MemberPassword, MemberPassword ):
            login_user(user, remember=remember)
            flash('Login success', category='info')
            if request.args.get('next'):
                flask.flash('Logged in successfully.')
                next = flask.request.args.get('next')
            return redirect(url_for('index'))
        flash('User not exists or password not match', category='danger')
    return render_template('login.html', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()