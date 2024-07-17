from flask import Flask
from Models.task import Task
app = Flask(__name__)

tasks = []




if __name__ == "__main__":
    app.run(debug=True)