from flask import Flask, url_for, redirect,render_template
app= Flask(__name__)

@app.route('/')
def home():
    return render_template("Homepage.html")

@app.route('/hospital_page',methods=["POST","GET"])
def hospital_page():
    if request.method=="POST":
        user=request.form["hosp"]
    else:
        return render_template('hospital.html')

if __name__=='__main__':
    app.run(debug=True)