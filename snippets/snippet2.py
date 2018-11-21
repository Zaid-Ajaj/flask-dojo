
@app.route("/say-hello")
def sayHello():
    user=request.args.get('user')
    return Response("Hello" + user, status=200, content_type="text/plain")