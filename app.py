from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="maureen123",
    database="sentineleye"
)

cursor = db.cursor(dictionary=True)

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():


    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- THREATS ----------------

@app.route("/threats")
def threats():

    cursor.execute("SELECT * FROM threats")
    threats = cursor.fetchall()

    return render_template("threats.html", threats=threats)


# ---------------- ALERTS ----------------

@app.route("/alerts")
def alerts():

    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()

    return render_template("alerts.html", alerts=alerts)


# ---------------- LOGS ----------------

@app.route("/logs")
def logs():

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    return render_template("logs.html", logs=logs)


# ---------------- ADD THREAT ----------------

@app.route("/add-threat")
def add_threat():
    return render_template("add_threat.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)