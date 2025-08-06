from flask import Flask, render_template, request, redirect, url_for
from routes.todo_routes import todo_bp
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Todo Module Routes
app.register_blueprint(todo_bp)
if __name__ == '__main__':
    app.run(debug=True)
    