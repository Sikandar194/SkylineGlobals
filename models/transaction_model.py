from flask import Flask
from .import db
class Transaction(db.Model):
    __tablename__ = 'Transactions'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Amount = db.Column(db.Numeric(19, 4), nullable=False)
    DebitFrom = db.Column(db.Integer, db.ForeignKey('Account.Id'),nullable=True)
    CreditTo = db.Column(db.Integer, db.ForeignKey('Account.Id'),nullable=True)
    Description = db.Column(db.Text, nullable=False)
    ParentCategoryId = db.Column(db.Integer, db.ForeignKey('Categories.Id'))
    EditedOn = db.Column(db.DateTime)
    Date = db.Column(db.DateTime, nullable=False)

    def __init__(self, Amount=None, DebitFrom=None, CreditTo=None, Description=None, ParentCategoryId=None, SubCategoryId=None, CreatedOn=None, EditedOn=None, Date=None, TypeId=None):
        self.Amount = Amount
        self.DebitFrom = DebitFrom
        self.CreditTo = CreditTo
        self.Description = Description
        self.ParentCategoryId = ParentCategoryId
        self.EditedOn = EditedOn
        self.Date = Date

