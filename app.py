from flask import Flask
from flask import Response
from flask import request
import simplejson as json 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Index"

# Add another to play with
@app.route("/another")
def another():
    return "Another text"

# Add logic to the query string
@app.route("/say-hello")
def sayHello():
    user=request.args.get('user')
    if user == "Daan":
        return Response("We don't like you Daan", status=401, content_type="text/plain; charset=utf-8")
    return Response("Hello " + user, status=200, content_type="text/plain")

# initialize todo's
todos = [ 
    { 'id': 1, 'name': 'Make paint drawings', 'done': True },
    { 'id': 2, 'name': 'Finish paint drawings', 'done': False }
]

# Exten the route to add a new item to the todo list
# Make a route to get all of the Todo items
@app.route("/todos", methods=["GET", "POST", "DELETE"])
def get_todos():
    global todos
    if request.method == "GET":
        return Response(json.dumps(todos), status=200, content_type="application/json")
    
    elif request.method == "POST":
        new_todo_item = json.loads(request.get_data())
        new_todo_item["done"] = False
        maxTodo = max(todos, key=lambda todo: todo["id"])
        nextId = maxTodo["id"] + 1
        new_todo_item["id"] = nextId
        todos.append(new_todo_item)
        return Response(json.dumps({ "id": nextId }), status=201, content_type="application/json")
    else:
        todoId = request.args.get("id")
        nextTodos = [ ]
        for todo in todos: 
            if todo["id"] != todoId: 
                nextTodos.append(todo)

        todos = nextTodos
        return Response("", status=204)

 
if __name__ == "__main__":
    app.run()

