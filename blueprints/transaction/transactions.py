import datetime
import logging
from flask import Blueprint, abort, flash, render_template, redirect, request, url_for, session
from sqlalchemy import desc
from models.account_model import Account
from models.category_model import Category
from models.transaction_model import Transaction, db

transaction_bp = Blueprint("transaction", __name__)
logger = logging.getLogger(__name__)

@transaction_bp.route('/addTransaction', methods=['GET', 'POST'])
def addTransaction():
    # Fetch account data from the database
    accounts = Account.query.all()

    # Fetch category data from the database
    categories = Category.query.all()

    if request.method == 'POST':
        amount = request.form['amount']
        credit_to = request.form['creditTo']
        description = request.form['description']
        parent_category = request.form['parentCategory']
        debit_from = request.form['debitTo']

        # Handle empty values for creditTo and debitTo
        if credit_to == '':
            credit_to = None
        if debit_from == '':
            debit_from = None

        # Check the presence of creditTo
        if credit_to is None:
            print("Credit from is not present")
        if credit_to is not None:
            print("Credit from is present: " + credit_to)

        # Check if both creditTo and debitFrom are not selected
        if credit_to is None and debit_from is None:
            # Return to the page without saving in the database
            return render_template('addTransaction.html', accounts=accounts, categories=categories)

        # Check if debitFrom and creditTo are the same
        if debit_from == credit_to:
            flash('Debit account and Credit account cannot be the same.', 'error')
            return redirect(url_for('transaction.addTransaction'))  # Redirect to the addTransaction page after submission

        # Update the account balances
        if credit_to is not None:
            credit_to_account = Account.query.get(credit_to)
            credit_to_account.Amount += int(amount)

        if debit_from is not None:
            debit_from_account = Account.query.get(debit_from)
            # checking if enough amount is present or not
            if debit_from_account.Amount >= int(amount): 
                debit_from_account.Amount -= int(amount)
            else:
                flash('Not enought amount in account', 'error')
                return redirect(url_for('transaction.addTransaction'))
                

        # Create a new transaction
        new_transaction = Transaction(
            Amount=amount,
            CreditTo=credit_to,
            Description=description,
            ParentCategoryId=parent_category,
            Date=datetime.datetime.now(),
            CreatedOn=datetime.datetime.now(),
            DebitFrom=debit_from
        )

        db.session.add(new_transaction)
        db.session.commit()
        flash('Transaction added successfully.')

    return render_template('addTransaction.html', accounts=accounts, categories=categories)


@transaction_bp.route('/allTransactions', methods=['GET'])
def allTransactions():
    # Fetch all transactions from the database
    transactions = Transaction.query.order_by(desc(Transaction.Date)).all()
    
    return render_template('all_transactions.html', transactions=transactions)



@transaction_bp.route('/editTransaction/<int:id>', methods=['GET', 'POST'])
def editTransaction(id):
    # Fetch the transaction from the database using the provided ID
    transaction = Transaction.query.get(id)
    if transaction is None:
        # If the transaction is not found, return a 404 Not Found page
        abort(404)

    # Fetch account data from the Account table
    accounts = Account.query.all()

    # Fetch category data from the Category table
    categories = Category.query.all()


    if request.method == 'POST':
        # Update the transaction with the edited values
        amount = request.form['amount']
        credit_to = request.form['creditTo']
        description = request.form['description']
        parent_category = request.form['parentCategory']
        debit_from = request.form['debitFrom']
        
        if credit_to == '':
                credit_to = None  # Set to None if it's an empty string
        
        if debit_from == '':
            debit_from = None  # Set to None if it's an empty string
        
        transaction.Amount = amount
        transaction.DebitFrom = debit_from
        transaction.CreditTo = credit_to
        transaction.Description = description
        transaction.ParentCategoryId = parent_category
        transaction.EditedOn = datetime.datetime.now()
        
        db.session.commit()
        flash('Transaction updated successfully.')
        return redirect(url_for('transaction.allTransactions'))

    return render_template('edit_transaction.html', transaction=transaction, accounts=accounts, categories=categories)


