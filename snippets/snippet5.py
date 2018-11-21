# Make a route to get all of the Todo items
@app.route("/todos", methods=["GET", "POST"])
def get_todos():
    if request.method == "GET":
        return Response(json.dumps(todos), status=200, content_type="application/json")
    
    new_todo_item = json.loads(request.get_data())
    new_todo_item["done"] = False
    maxTodo = max(todos, key=lambda todo: todo["id"])
    nextId = maxTodo["id"] + 1
    new_todo_item["id"] = nextId
    todos.append(new_todo_item)
    return Response(json.dumps({ "id": nextId }), status=201, content_type="application/json")