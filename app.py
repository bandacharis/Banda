from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed to use sessions

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'students' not in session:
        session['students'] = []

    if request.method == 'POST':
        name = request.form.get('name')
        year = request.form.get('year')
        section = request.form.get('section')

        if name and year and section:
            students = session.get('students', [])
            students.append({'name': name, 'year': year, 'section': section})
            session['students'] = students
            return redirect(url_for('welcome', name=name))

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Registration</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                height: 100vh;
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                padding: 50px 60px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                text-align: center;
                width: 400px;
            }
            h1 {
                margin-bottom: 25px;
                font-size: 2em;
                background: linear-gradient(90deg, #00f2fe, #4facfe);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            input {
                width: 100%;
                padding: 12px;
                margin-bottom: 20px;
                border: none;
                border-radius: 8px;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                font-size: 1em;
                text-align: center;
                transition: box-shadow 0.3s ease, transform 0.3s ease;
            }
            input:focus {
                outline: none;
                box-shadow: 0 0 10px #00f2fe;
                transform: scale(1.03);
            }
            button {
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 10px;
                background: linear-gradient(45deg, #00f2fe, #4facfe);
                color: white;
                font-weight: bold;
                font-size: 1em;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            button:hover {
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
                background: linear-gradient(45deg, #4facfe, #00f2fe);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎓 Student Info</h1>
            <form method="POST">
                <input type="text" name="name" placeholder="Enter Name" required>
                <input type="text" name="year" placeholder="Enter Year" required>
                <input type="text" name="section" placeholder="Enter Section" required>
                <button type="submit">Submit</button>
            </form>
            <form action="/dashboard" style="margin-top:20px;">
                <button type="submit">📋 Go to Dashboard</button>
            </form>
        </div>
    </body>
    </html>
    """)

@app.route('/welcome')
def welcome():
    name = request.args.get('name')
    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #764ba2, #667eea);
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                color: white;
                margin: 0;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
                background: linear-gradient(90deg, #00f2fe, #4facfe);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            button {{
                background: linear-gradient(45deg, #ff9966, #ff5e62);
                border: none;
                color: white;
                padding: 12px 25px;
                border-radius: 10px;
                cursor: pointer;
                font-weight: bold;
                margin-top: 30px;
                transition: all 0.3s ease;
            }}
            button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }}
        </style>
    </head>
    <body>
        <h1>🎉 Hi {name}, Welcome!</h1>
        <form action="/">
            <button type="submit">⬅️ Back to Form</button>
        </form>
        <form action="/dashboard" style="margin-top:10px;">
            <button type="submit">📋 Go to Dashboard</button>
        </form>
    </body>
    </html>
    """)

@app.route('/dashboard')
def dashboard():
    students = session.get('students', [])
    student_rows = ""
    for s in students:
        student_rows += f"<tr><td>{s['name']}</td><td>{s['year']}</td><td>{s['section']}</td></tr>"

    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            h1 {{
                margin-bottom: 20px;
                background: linear-gradient(90deg, #00f2fe, #4facfe);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            table {{
                border-collapse: collapse;
                width: 90%;
                max-width: 700px;
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(10px);
                border-radius: 10px;
                overflow: hidden;
            }}
            th, td {{
                padding: 15px;
                text-align: center;
            }}
            th {{
                background: rgba(255,255,255,0.25);
            }}
            tr:nth-child(even) {{
                background: rgba(255,255,255,0.1);
            }}
            button {{
                margin-top: 20px;
                padding: 12px 25px;
                border: none;
                border-radius: 10px;
                background: linear-gradient(45deg, #ff9966, #ff5e62);
                color: white;
                cursor: pointer;
                font-weight: bold;
                transition: all 0.3s ease;
            }}
            button:hover {{
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }}
        </style>
    </head>
    <body>
        <h1>📋 Student Dashboard</h1>
        <table>
            <tr><th>Name</th><th>Year</th><th>Section</th></tr>
            {student_rows if student_rows else '<tr><td colspan="3">No students added yet</td></tr>'}
        </table>
        <form action="/" >
            <button type="submit">⬅️ Back to Form</button>
        </form>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
