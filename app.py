from flask import Flask
import os

app = Flask(name)

@app.route('/')
def hello_world():
    return "Hello from AJ TECH WORLD"

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
