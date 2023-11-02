from . import db 

class User(db.Model):
    __tablename__ = 'User'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    RoleId = db.Column(db.Integer, db.ForeignKey('Role.Id'))
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    Number = db.Column(db.String(50))

    def __init__(self, UserName=None, Password=None, RoleId=None, FirstName=None, LastName=None, Email=None, Number=None):
        self.UserName = UserName
        self.Password = Password
        self.RoleId = RoleId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Number = Number

