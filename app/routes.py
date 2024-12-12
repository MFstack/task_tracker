from flask import jsonify, request
from app import app, db
from app.models import User, Task

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        user_id=data['user_id'],
        title=data['title'],
        due_date=data.get('due_date')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully'}), 201
