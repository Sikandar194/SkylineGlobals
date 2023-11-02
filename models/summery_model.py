from . import db

class Summary(db.Model):
    __tablename__ = 'Summaries'

    AccountId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    StartingBalance = db.Column(db.Numeric(19, 4), nullable=False)
    AmountCredited = db.Column(db.Numeric(19, 4))
    AmountDebited = db.Column(db.Numeric(19, 4))
    CurrentBalance = db.Column(db.Numeric(19, 4))
    Transactions = db.Column(db.Integer)

    def __init__(self, Name=None, StartingBalance=None, AmountCredited=None, AmountDebited=None, CurrentBalance=None, Transactions=None):
        self.Name = Name
        self.StartingBalance = StartingBalance
        self.AmountCredited = AmountCredited
        self.AmountDebited = AmountDebited
        self.CurrentBalance = CurrentBalance
        self.Transactions = Transactions


