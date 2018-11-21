# Add logic to the query string
@app.route("/say-hello")
def sayHello():
    user=request.args.get('user')
    if user == "Daan":
        return Response("We don't like you Daan", status=401, content_type="text/plain; charset=utf-8")
    return Response("Hello " + user, status=200, content_type="text/plain")