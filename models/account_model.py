from . import db


class Account(db.Model):
    __tablename__ = 'Account'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.Text)
    Amount = db.Column(db.Integer, nullable=True)

    def __init__(self, Name, Description=None, StartingBalance=None, UserId=None, Amount = None):
        self.Name = Name
        self.Description = Description
        self.UserId = UserId
        self.Amount = Amount
