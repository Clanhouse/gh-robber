from . import api


@api.route("/hello-world/")
def hello_world():
    return {"hello": "world"}
