from . import db

class Category(db.Model):
    __tablename__ = 'Categories'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(75), nullable=False)

    def __init__(self, ParentId=None, Name=None):
        self.ParentId = ParentId
        self.Name = Name

