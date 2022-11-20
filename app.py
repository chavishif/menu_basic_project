from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/salad")
def salad():
    return render_template('page2.html')

@app.route("/main_dishes")
def main_dishes():
     return render_template('page3.html')

@app.route("/Deserts")
def Deserts():
     return render_template('page4.html')


if __name__ == "__main__":
    app.run(debug=True)
