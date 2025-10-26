from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Home route: shows the form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            return redirect(url_for('welcome', student_name=name))
    
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Form</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(120deg, #6a11cb, #2575fc);
                color: white;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0;
            }
            .form-container {
                background: rgba(255, 255, 255, 0.15);
                padding: 30px 40px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.2);
                text-align: center;
                width: 350px;
            }
            h1 {
                margin-bottom: 20px;
            }
            input {
                width: 90%;
                padding: 10px;
                border: none;
                border-radius: 8px;
                margin-bottom: 20px;
                font-size: 1em;
            }
            button {
                background: #007bff;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
                transition: background 0.3s ease;
            }
            button:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>🎓 Enter Student Name</h1>
            <form method="POST">
                <input type="text" name="name" placeholder="Enter student name" required><br>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """)


# Welcome route: shows message and back button
@app.route('/welcome/<student_name>')
def welcome(student_name):
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
                background: linear-gradient(120deg, #2575fc, #6a11cb);
                color: white;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0;
                flex-direction: column;
            }}
            h1 {{
                font-size: 2em;
                margin-bottom: 20px;
            }}
            button {{
                background: #ff9800;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
                transition: background 0.3s ease;
            }}
            button:hover {{
                background: #e68900;
            }}
        </style>
    </head>
    <body>
        <h1>🎉 Welcome, {student_name}!</h1>
        <form action="/">
            <button type="submit">⬅️ Back</button>
        </form>
    </body>
    </html>
    """)


if __name__ == '__main__':
    app.run(debug=True)
