from flask import Flask, render_template, request
from employee import Employee

app = Flask(__name__)

employees = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        hourly_rate = float(request.form["hourly_rate"])
        hours_worked = float(request.form["hours_worked"])
        emp = Employee(name, hourly_rate, hours_worked)
        employees.append(emp)

    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
