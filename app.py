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
        <title>Flask API Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(to right, #6a11cb, #2575fc);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding-top: 60px;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                backdrop-filter: blur(10px);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
            }
            a {
                color: #fff;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
            .endpoint {
                background: rgba(255, 255, 255, 0.15);
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            code {
                background: rgba(0, 0, 0, 0.3);
                padding: 3px 6px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container text-center">
            <h1>🚀 Welcome to My Flask API</h1>
            <p>This API allows you to explore student data dynamically.</p>
            
            <div class="text-start mt-4">
                <h3>📚 Available Endpoints</h3>
                <div class="endpoint">
                    <code>GET /student/&lt;name&gt;</code> — Fetch a student’s info.
                </div>
                <div class="endpoint">
                    <code>POST /student</code> — Add new student data.
                </div>
                <div class="endpoint">
                    <code>GET /</code> — API Dashboard (this page).
                </div>
            </div>

            <footer class="mt-5">
                <p>Made with ❤️ using Flask</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)


@app.route('/student/<name>', methods=['GET'])
def get_student(name):
    data = {
        "name": name,
        "grade": 10,
        "section": "Zechariah",
        "message": f"Hello {name}, welcome to our API!"
    }
    return jsonify(data)


@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request"}), 400
    return jsonify({
        "message": "Student added successfully",
        "student": data
    }), 201


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
