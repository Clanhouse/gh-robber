from . import main


@main.route("/")
def hello_world():
    return "Hello World!"
