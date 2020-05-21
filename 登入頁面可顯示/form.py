from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, BooleanField
from wtforms.validators import ValidationError
from wtforms.fields.html5 import EmailField
from model import MemberData

class FormRegister(FlaskForm):
    """依照Model來建置相對應的Form
    
    password2: 用來確認兩次的密碼輸入相同
    """
    UserID = StringField('UserID', validators=[
        validators.DataRequired(),
        validators.Length(1, 30)
    ])
    MemberName = StringField('MemberName', validators=[
        validators.DataRequired(),
        validators.Length(1, 30)
    ])
    MemberPhone = StringField('MemberPhone', validators=[
        validators.DataRequired(),
        validators.Length(8, 30)
    ])
    MemberMail = EmailField('MemberMail', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    MemberAccount= StringField('MemberAccount', validators=[
        validators.DataRequired(),
        validators.Length(1, 30)
    ])   
    MemberPassword = PasswordField('MemberPassword', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('MemberPassword2', message='MemberPassword NEED MATCH')
    ])
    MemberPassword2 = PasswordField('Confirm MemberPassword', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')


    def validate_UserID(self, field):
        if MemberData.query.filter_by(UserID=field.data).first():
            raise  ValidationError('UserID already register by somebody')
    def validate_MemberName(self, field):
        if MemberData.query.filter_by(MemberName=field.data).first():
            raise  ValidationError('MemberName already register by somebody')
    def validate_MemberPhone(self, field):
        if MemberData.query.filter_by(MemberPhone=field.data).first():
            raise  ValidationError('MemberPhone already register by somebody')
    def validate_MemberMail(self, field):
        if MemberData.query.filter_by(MemberMail=field.data).first():
            raise ValidationError('MemberMail already register by somebody')
    def validate_MemberAccount(self, field):
        if MemberData.query.filter_by(MemberAccount=field.data).first():
            raise  ValidationError('MemberPhone already register by somebody')

    def validate_UserID(self, field):
        if MemberData.query.filter_by(UserID=field.data).first():
            raise  ValidationError('UserID already register by somebody')
    def validate_MemberName(self, field):
        if MemberData.query.filter_by(MemberName=field.data).first():
            raise  ValidationError('MemberName already register by somebody')
    def validate_MemberPhone(self, field):
        if MemberData.query.filter_by(MemberPhone=field.data).first():
            raise  ValidationError('MemberPhone already register by somebody')
    def validate_MemberMail(self, field):
        if MemberData.query.filter_by(MemberMail=field.data).first():
            raise ValidationError('MemberMail already register by somebody')
    def validate_MemberAccount(self, field):
        if MemberData.query.filter_by(MemberAccount=field.data).first():
            raise  ValidationError('MemberPhone already register by somebody')
    
class FormLogin(FlaskForm):

    MemberAccount= StringField('MemberAccount', validators=[
        validators.DataRequired(),
        validators.Length(1, 30)
    ])   
    MemberPassword = PasswordField('MemberPassword', validators=[
        validators.DataRequired(),
        validators.Length(5, 10)
        ])
    remember = BooleanField('Remember')
    submit = SubmitField('登入')