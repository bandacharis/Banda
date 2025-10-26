@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'students' not in session:
        session['students'] = []

    students = session['students']

    # Handle deletion
    if request.method == 'POST' and 'delete_index' in request.form:
        delete_index = int(request.form.get('delete_index'))
        students.pop(delete_index)
        session['students'] = students
        return redirect(url_for('dashboard'))

    student_rows = ""
    for index, s in enumerate(students):
        student_rows += f"""
        <tr>
            <td>{s['name']}</td>
            <td>{s['year']}</td>
            <td>{s['section']}</td>
            <td>
                <form method="POST" action="/edit/{index}" style="display:inline;">
                    <button type="submit" style="background:#ffa500;">Edit</button>
                </form>
                <form method="POST" style="display:inline;margin-left:5px;">
                    <input type="hidden" name="delete_index" value="{index}">
                    <button type="submit" style="background:#ff4b5c;">Delete</button>
                </form>
            </td>
        </tr>"""

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
            input {{
                padding: 10px;
                border-radius: 8px;
                border: none;
                margin-bottom: 15px;
                width: 300px;
                text-align: center;
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
                cursor: pointer;
            }}
            th {{
                background: rgba(255,255,255,0.25);
            }}
            tr:nth-child(even) {{
                background: rgba(255,255,255,0.1);
            }}
            tr:hover {{
                background: rgba(255,255,255,0.25);
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
            form button {{
                width: auto;
                padding: 5px 10px;
            }}
        </style>
    </head>
    <body>
        <h1>📋 Student Dashboard</h1>
        <input type="text" id="searchInput" onkeyup="searchTable()" placeholder="🔍 Search by name, year or section">
        <table id="studentTable">
            <tr>
                <th onclick="sortTable(0)">Name ⬍</th>
                <th onclick="sortTable(1)">Year ⬍</th>
                <th onclick="sortTable(2)">Section ⬍</th>
                <th>Action</th>
            </tr>
            {student_rows if student_rows else '<tr><td colspan="4">No students added yet</td></tr>'}
        </table>
        <form action="/" >
            <button type="submit">⬅️ Back to Form</button>
        </form>

        <script>
            // Search function
            function searchTable() {{
                let input = document.getElementById("searchInput");
                let filter = input.value.toLowerCase();
                let table = document.getElementById("studentTable");
                let tr = table.getElementsByTagName("tr");
                for (let i = 1; i < tr.length; i++) {{
                    let tdArr = tr[i].getElementsByTagName("td");
                    let found = false;
                    for (let j = 0; j < tdArr.length - 1; j++) {{
                        if (tdArr[j].textContent.toLowerCase().indexOf(filter) > -1) {{
                            found = true;
                        }}
                    }}
                    tr[i].style.display = found ? "" : "none";
                }}
            }}

            // Sort function
            function sortTable(n) {{
                let table = document.getElementById("studentTable");
                let rows = Array.from(table.rows).slice(1);
                let asc = table.getAttribute("data-sort-dir") === "asc";
                rows.sort((a, b) => {{
                    let x = a.cells[n].textContent.toLowerCase();
                    let y = b.cells[n].textContent.toLowerCase();
                    if (x < y) return asc ? -1 : 1;
                    if (x > y) return asc ? 1 : -1;
                    return 0;
                }});
                for (let row of rows) table.appendChild(row);
                table.setAttribute("data-sort-dir", asc ? "desc" : "asc");
            }}
        </script>
    </body>
    </html>
    """)
