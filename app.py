from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🚀 My Flask API</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(120deg, #6a11cb, #2575fc);
                background-size: 200% 200%;
                animation: gradientShift 8s ease infinite;
                color: #fff;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            .container {
                max-width: 850px;
                margin: 60px auto;
                background: rgba(255, 255, 255, 0.1);
                padding: 35px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            p.subtitle {
                color: #e0e0e0;
                margin-bottom: 30px;
            }
            .endpoint {
                background: rgba(255,255,255,0.15);
                border-radius: 12px;
                padding: 15px;
                margin: 15px 0;
                text-align: left;
                transition: all 0.3s ease;
            }
            .method {
                display: inline-block;
                padding: 5px 12px;
                border-radius: 6px;
                font-weight: bold;
                margin-right: 10px;
                font-size: 0.9em;
            }
            .GET { background: #28a745; }
            .POST { background: #ff9800; }
            code {
                background: rgba(0,0,0,0.3);
                padding: 3px 6px;
                border-radius: 5px;
                color: #fff;
            }
            form {
                text-align: left;
                margin-top: 15px;
            }
            label {
                display: block;
                margin: 8px 0 4px;
                font-weight: 500;
            }
            input {
                width: 100%;
                padding: 10px;
                border-radius: 8px;
                border: none;
                font-size: 1em;
                margin-bottom: 10px;
            }
            button {
                margin-top: 8px;
                padding: 10px 18px;
                border: none;
                border-radius: 6px;
                background-color: #007bff;
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.2s ease;
            }
            button:hover {
                background-color: #0056b3;
            }
            pre {
                text-align: left;
                background: rgba(0,0,0,0.4);
                padding: 10px;
                border-radius: 8px;
                overflow-x: auto;
                color: #aef5ff;
                margin-top: 15px;
            }
            footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #ddd;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to My Flask API</h1>
            <p class="subtitle">This API allows you to explore student data dynamically.</p>

            <h3 style="text-align:left;">📚 Available Endpoints</h3>

            <div class="endpoint">
                <span class="method GET">GET</span><code>/student/&lt;name&gt;</code> — Fetch a student's info.
                <button onclick="fetchStudent('John')">Try Example</button>
                <pre id="output1"></pre>
            </div>

            <div class="endpoint">
                <span class="method POST">POST</span><code>/student</code> — Add a new student.
                <form id="studentForm" onsubmit="submitForm(event)">
                    <label for="name">Name:</label>
                    <input type="text" id="name" placeholder="Enter name" required>

                    <label for="grade">Grade:</label>
                    <input type="number" id="grade" placeholder="Enter grade" required>

                    <label for="section">Section:</label>
                    <input type="text" id="section" placeholder="Enter section" required>

                    <button type="submit">Submit Student</button>
                </form>
                <pre id="output2"></pre>
            </div>

            <div class="endpoint">
                <span class="method GET">GET</span><code>/</code> — API Dashboard (this page).
            </div>

            <footer>Made with ❤️ using Flask</footer>
        </div>

        <script>
            async function fetchStudent(name) {
                const res = await fetch(`/student/${name}`);
                const data = await res.json();
                document.getElementById('output1').textContent = JSON.stringify(data, null, 2);
            }

            async function submitForm(event) {
                event.preventDefault();
                const name = document.getElementById('name').value;
                const grade = document.getElementById('grade').value;
                const section = document.getElementById('section').value;

                const res = await fetch('/student', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name, grade, section })
                });
                const data = await res.json();
                document.getElementById('output2').textContent = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)


@app.route('/student/<name>')
def get_student(name):
    return jsonify({
        "name": name,
        "grade": 10,
        "section": "Zechariah",
        "message": f"Hello {name}, welcome to the Flask API!"
    })


@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    return jsonify({
        "message": "Student added successfully",
        "data": data
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
