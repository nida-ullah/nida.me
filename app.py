from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>hello world</p>"

# if __name__ == ("__main__"):
