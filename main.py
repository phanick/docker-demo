from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is Kubernetes demo on 18July"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
