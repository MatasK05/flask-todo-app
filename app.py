import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.form["title"],
        "completed": False,
    }
    tasks.append(new_task)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)