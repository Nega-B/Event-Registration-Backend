from flask import Flask,render_template,request
import sqlite3

app= Flask(__name__)

def get_db_connection():
    conn=sqlite3.connect("event.db")
    return conn

@app.route("/")
def home():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM registrations")
        count = cursor.fetchone()[0]

        cursor.execute("SELECT * FROM registrations")
        students = cursor.fetchall()
        conn.close()
        
        return render_template("index.html", count=count,students=students )
        

@app.route("/register",methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    if '@' not in email or '.' not in email: 
         return "Please enter a valid email."
    department = request.form["department"]
    if not name or not email or not department : 
         return "Please fill in all fields."

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM registrations")
    count = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM registrations WHERE email = ?",(email,))
    if cursor.fetchone():
         conn.close()
         return "This email is already registered."

    if count>=50:
        conn.close()
        return "Sorry registrations are Full! Maximum 50 members allowed."
    cursor.execute("INSERT INTO registrations (name, email, department) VALUES (?, ?, ? )",(name,email,department))
    conn.commit()
    conn.close()

    return f"Registration received ! WELCOME {name}!"

if __name__=="__main__":
    app.run(debug=True, port=5001)
