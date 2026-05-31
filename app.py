import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)