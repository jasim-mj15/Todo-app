from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # Store tasks

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task').strip()  # Remove extra spaces
    if task:  # Only add if task is not empty
        tasks.append(task)
    return redirect('/')


@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)  # Remove task permanently
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
