from flask import Flask, render_template, request, redirect, url_for
from routes.todo_routes import todo_bp
from routes.password_routes  import password_bp
from routes.converter_routes import converter_bp
from routes.expense_route import expense_bp
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Todo Module Routes
app.register_blueprint(todo_bp)

#password module Route
app.register_blueprint(password_bp)

#converter module Route
app.register_blueprint(converter_bp)

#expense tracker module Route
app.register_blueprint(expense_bp)
if __name__ == '__main__':
    app.run(debug=True)
    