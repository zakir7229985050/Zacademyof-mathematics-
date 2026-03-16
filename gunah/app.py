"""
Coaching Institute Website - Flask Backend
IIT/NEET Success - Professional Coaching Institute
"""

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_from_directory
import sqlite3
import os
import random
from datetime import datetime
import hashlib

app = Flask(__name__)

# Secret key
app.secret_key = os.getenv('SECRET_KEY', 'gravity_coaching_secret_key')

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


# ---------------- DATABASE ---------------- #

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT UNIQUE,
            password TEXT,
            is_admin INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            duration TEXT,
            price INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            course_id INTEGER,
            payment_status TEXT,
            progress INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- ROUTES ---------------- #

@app.route("/")
def index():
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return render_template("index.html", courses=courses)


@app.route("/courses")
def courses():
    conn = get_db_connection()
    courses = conn.execute("SELECT * FROM courses").fetchall()
    conn.close()
    return render_template("courses.html", courses=courses)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        phone = request.form.get("phone")
        password = hash_password(request.form.get("password"))

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE phone=? AND password=?",
            (phone, password)
        ).fetchone()

        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]

            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    enrollments = conn.execute(
        """SELECT e.*, c.title
           FROM enrollments e
           JOIN courses c ON e.course_id = c.id
           WHERE e.user_id=?""",
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template("dashboard.html", enrollments=enrollments)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ---------------- ADMIN ---------------- #

def create_admin():

    conn = get_db_connection()

    admin = conn.execute(
        "SELECT * FROM users WHERE is_admin=1"
    ).fetchone()

    if not admin:
        conn.execute(
            "INSERT INTO users (name,email,phone,password,is_admin) VALUES (?,?,?,?,?)",
            ("Admin", "admin@gravity.com", "9999999999", hash_password("admin123"), 1)
        )
        conn.commit()

    conn.close()


# ---------------- STATIC FILES ---------------- #

@app.route("/static/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename)


@app.route("/static/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory("static/pdfs", filename)


# ---------------- RUN ---------------- #

init_db()
create_admin()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
