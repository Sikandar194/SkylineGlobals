import redis
import logging
from models import db
from flask import Flask
from config import Config
from flask_mail import Mail
from flask_session import Session
from blueprints.transaction.transactions import transaction_bp
from blueprints.category.categories import category_bp
from blueprints.account.accounts import account_bp




app = Flask(__name__)


app.config.from_object(Config)

app.jinja_env.autoescape = True


# Configure logging
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=log_format)

# Create a logger instance for your application
logger = logging.getLogger(__name__)


Session(app)

mail = Mail()
mail.init_app(app)


app.register_blueprint(transaction_bp) 
app.register_blueprint(category_bp) 
app.register_blueprint(account_bp) 


db.init_app(app)


if __name__ =="__main__":
    app.run(debug=True)
    
