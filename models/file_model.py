from .import db

class File(db.Model):
    __tablename__ = 'Files'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FileName = db.Column(db.String(100), nullable=False)
    TransactionId = db.Column(db.Integer, db.ForeignKey('Transactions.Id'))

    def __init__(self, FileName=None, TransactionId=None):
        self.FileName = FileName
        self.TransactionId = TransactionId

