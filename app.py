from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline!"

if _name_ == "_main_":
    app.run(debug=True)
