from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import your models so that they are registered with the db instance
from .user_model import User
from .category_model import Category
from .role_model import Role
from .summery_model import Summary
from .transaction_model import Transaction
from .account_model import Account