from flask import Flask, url_for, redirect,render_template
app= Flask(__name__)

@app.route('/')
def home():
    return render_template("Homepage.html")

if __name__=='__main__':
    app.run(debug=True)