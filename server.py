from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>helooooooooooooooooooooooo!</p>"


app.run(host="0.0.0.0", port=9000)
