# initialize todo's
todos = [ 
    { 'id': 1, 'name': 'Make paint drawings', 'done': True },
    { 'id': 2, 'name': 'Finish paint drawings', 'done': False }
]

# Make a route to get all of the Todo items
@app.route("/todos")
def get_todos():
    return Response(json.dumps(todos), status=200, content_type="application/json")