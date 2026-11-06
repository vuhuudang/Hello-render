from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Xin chao tu Render! Bai thuc hanh PaaS."
