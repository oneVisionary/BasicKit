from flask import Blueprint, Flask, render_template, request, redirect, url_for

expense_bp = Blueprint('expense', __name__)


@expense_bp.route('/expense')
def expense():
    return render_template('expense-tracker.html')
