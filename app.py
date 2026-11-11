from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return """
    <center>
        <h2>Hello world</h2>
        <a href="register.html">Register</a>
    </center>
        """
@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/success.html",methods=["POST"])
def success():
    name=request.form["name"]
    year=request.form["year"]
    return render_template("success.html",name=name,year=year)
if __name__=="__main__":
    app.run(debug=True)