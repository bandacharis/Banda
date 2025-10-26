from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        grade = request.form.get('grade')
        year = request.form.get('year')
        section = request.form.get('section')
        if name and grade and year and section:
            return redirect(url_for('welcome', name=name, grade=grade, year=year, section=section))

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
                overflow: hidden;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .wave {
                position: absolute;
                width: 200%;
                height: 200%;
                top: -50%;
                left: -50%;
                background: radial-gradient(circle at center, rgba(255,255,255,0.1), transparent 70%);
                animation: rotate 15s linear infinite;
                z-index: 0;
            }
            @keyframes rotate {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .card {
                position: relative;
                z-index: 2;
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                padding: 50px 60px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                text-align: center;
                animation: fadeIn 1s ease;
                width: 400px;
            }
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(20px);}
                to {opacity: 1; transform: translateY(0);}
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
            input::placeholder {
                color: #e0e0e0;
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
        <div class="wave"></div>
        <div class="card">
            <h1>🎓 Student Info</h1>
            <form method="POST">
                <input type="text" name="name" placeholder="Enter Name" required>
                <input type="number" name="grade" placeholder="Enter Grade" required>
                <input type="text" name="year" placeholder="Enter Year" required>
                <input type="text" name="section" placeholder="Enter Section" required>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """)

@app.route('/welcome')
def welcome():
    name = request.args.get('name')
    grade = request.args.get('grade')
    year = request.args.get('year')
    section = request.args.get('section')
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
                overflow: hidden;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
                background: linear-gradient(90deg, #00f2fe, #4facfe);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: fadeIn 1.2s ease;
            }}
            p {{
                font-size: 1.2em;
                opacity: 0;
                animation: fadeInText 2s forwards 1s;
            }}
            @keyframes fadeIn {{
                from {{opacity: 0; transform: translateY(20px);}}
                to {{opacity: 1; transform: translateY(0);}}
            }}
            @keyframes fadeInText {{
                to {{opacity: 1;}}
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
            .wave {{
                position: absolute;
                width: 200%;
                height: 200%;
                top: -50%;
                left: -50%;
                background: radial-gradient(circle at center, rgba(255,255,255,0.1), transparent 70%);
                animation: rotate 15s linear infinite;
                z-index: 0;
            }}
            @keyframes rotate {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}
        </style>
    </head>
    <body>
        <div class="wave"></div>
        <h1>🎉 Welcome, {name}!</h1>
        <p>Grade: {grade} | Year: {year} | Section: {section}</p>
        <form action="/">
            <button type="submit">⬅️ Back to Form</button>
        </form>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
