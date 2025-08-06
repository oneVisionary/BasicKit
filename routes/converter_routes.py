from flask import Blueprint, Flask, render_template, request, redirect, url_for

converter_bp = Blueprint('converter', __name__)


@converter_bp.route('/converter')
def converter():
    return render_template('unit-converter.html')
