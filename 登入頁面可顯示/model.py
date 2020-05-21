from flask_login import UserMixin
from app import db
    
class MemberData(db.Model, UserMixin):  
    __tablename__ = 'MemberData'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.String(120), nullable=False)#會員姓名
    MemberName = db.Column(db.String(120), nullable=False)#會員姓名
    MemberPhone = db.Column(db.String(120), nullable=True)#會員手機
    MemberMail = db.Column(db.String(120), nullable=False)#會員E-mail
    MemberAccount = db.Column(db.String(256), nullable=False)#會員帳號
    MemberPassword = db.Column(db.String(120), nullable=False)#會員密碼

    def __repr__(self):
        return 'MemberName:%s, email:%s' % (self.MemberName, self.email)