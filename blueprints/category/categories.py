import logging
from flask import Blueprint, abort, render_template, flash, redirect, request, url_for
from models.category_model import Category, db

category_bp = Blueprint("category", __name__, template_folder="templates/categories")
logger = logging.getLogger(__name__)

@category_bp.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == 'POST':
        name = request.form['name']
        
        new_category = Category(Name=name)
        db.session.add(new_category)
        db.session.commit()
        flash('Category added successfully.', 'success')
        return redirect(url_for('category.listCategories'))
    return render_template('add_category.html')


@category_bp.route('/listCategories', methods=['GET'])
def listCategories():
    categories = Category.query.all()
    return render_template('listCategories.html', categories=categories)

@category_bp.route('/deleteCategory/<int:id>', methods=['POST'])
def deleteCategory(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully.', 'success')
    return redirect(url_for('category.listCategories'))



@category_bp.route('/editCategory/<int:id>', methods=['GET', 'POST'])
def editCategory(id):
    # Fetch the transaction from the database using the provided ID
    category = Category.query.get(id)
  
    if category is None:
        # If the transaction is not found, return a 404 Not Found page
        abort(404)


    if request.method == 'POST':
        # Update the transaction with the edited values
        name = request.form['name']
        category.Name = name
        db.session.commit()
        flash('Transaction updated successfully.')
        return redirect(url_for('category.listCategories'))

    return render_template('editCategory.html', category=category)


