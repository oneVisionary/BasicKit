from flask import Blueprint, Flask, render_template, request, redirect, url_for
from utils.file_utils import load_json, save_json
import uuid

todo_bp = Blueprint('todo', __name__)
DATA_PATH = 'data/todo.json'

@todo_bp.route('/todo')
def todo():
    tasks = load_json(DATA_PATH, [])
    return render_template('todo.html',tasks=tasks)

@todo_bp.route('/add_todo',methods=['POST'] )
def add_todo():
    title = request.get_json().get('title', '').strip()
    print(f"Adding todo: {title}")
    tasks = load_json(DATA_PATH, [])
    print(tasks)
    if title:
        newtask = {'id': 'task_'+str(uuid.uuid4()), 'title': title, 'completed': False}
        tasks.append(newtask)
        save_json(DATA_PATH, tasks)
    return redirect(url_for('todo.todo'))


@todo_bp.route('/update_todo',methods=['POST'] )
def update_todo():
    data = request.get_json()
    taskid = data.get('id', '')
    status = data.get('completed')
    print(f"Adding todo: {taskid},{status}")
    tasks = load_json(DATA_PATH, [])
    print(tasks)
    for task in tasks:
        if task['id']==taskid:
            task['completed']= status
            break
    save_json(DATA_PATH, tasks)
    return redirect(url_for('todo.todo'))


@todo_bp.route('/delete_todo',methods=['POST'] )
def delete_todo():
    data = request.get_json()
    taskid = data.get('id', '')
    
    tasks = load_json(DATA_PATH, [])
    print(taskid)
    print("******************")
    tasks = [tt for tt in tasks if tt['id']!=taskid]
    print(tasks)
    save_json(DATA_PATH, tasks)
    return redirect(url_for('todo.todo'))
