import logging
from flask import Blueprint, abort, render_template, flash, redirect, request, url_for
from models.account_model import Account, db
from models.category_model import Category

account_bp = Blueprint("account", __name__, template_folder="templates/accounts")
logger = logging.getLogger(__name__)

@account_bp.route('/addAccount', methods=['GET', 'POST'])
def addAccount():
    if request.method == 'POST':
        name = request.form['name']
        description  = request.form['description']
        
        new_account = Account(
            Name=name, 
            Description=description, 
            Amount = 0
            )
        db.session.add(new_account)
        db.session.commit()
        flash('Account added successfully.', 'success')
        return redirect(url_for('account.listAccounts'))
    return render_template('addAccount.html')


@account_bp.route('/listAccounts', methods=['GET'])
def listAccounts():
    accounts = Account.query.all()
    return render_template('listAccounts.html', accounts=accounts)


@account_bp.route('/deleteAccount/<int:id>', methods=['POST'])
def deleteAccount(id):
    account = Account.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    flash('account deleted successfully.', 'success')
    return redirect(url_for('account.listAccounts'))



@account_bp.route('/editAccount/<int:id>', methods=['GET', 'POST'])
def editAccount(id):
    # Fetch the transaction from the database using the provided ID
    account = Account.query.get(id)
  
    if account is None:
        # If the transaction is not found, return a 404 Not Found page
        abort(404)


    if request.method == 'POST':
        # Update the transaction with the edited values
        name = request.form['name']
        description = request.form['description']
        account.Name = name
        account.Description = description
        db.session.commit()
        flash('account updated successfully.')
        return redirect(url_for('account.listAccounts'))

    return render_template('editAccount.html', account=account)


