from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.jinja", schedule=json.loads(open('data.json', 'r').read().replace("'",'"')))

if __name__ == "__main__":
    app.run(debug=True)