from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/Home')
def home():
    return render_template("home.html", title="Home")

@app.route('/About')
def about():
    return render_template("about.html", title="About")

@app.route('/Charts')
def charts():
    return render_template("charts.html", title="Charts")

@app.route('/Contact')
def contact():
    return render_template("contact.html", title="Contact Me")



if __name__ == "__main__":
    app.run(debug=True)