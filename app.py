from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

shopping_list = {
    "Melk": False,
    "Brød": False,
    "Egg": False
}

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Shopping List</title>
    <style>
        body {
            background-color: #f5f5dc;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            margin: 0;
            padding-top: 50px;
        }
        .note {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            padding: 30px;
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            margin-top: 0;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 8px 0;
            display: flex;
            align-items: center;
        }
        input[type="checkbox"] {
            margin-right: 10px;
        }
        .done {
            text-decoration: line-through;
            color: #777;
        }
        form.add-item {
            margin-top: 20px;
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 8px;
        }
        button {
            padding: 8px 12px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="note">
        <h1>Shopping List</h1>
        <ul>
            {% for item, done in shopping_list.items() %}
                <li>
                    <form method="POST" action="/toggle" style="margin: 0;">
                        <input type="hidden" name="item" value="{{ item }}">
                        <input type="checkbox" onchange="this.form.submit()" {% if done %}checked{% endif %}>
                        <span class="{{ 'done' if done }}">{{ item }}</span>
                    </form>
                </li>
            {% endfor %}
        </ul>

        <form method="POST" action="/" class="add-item">
            <input type="text" name="item" placeholder="New item" required>
            <button type="submit">Add</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        if item and item not in shopping_list:
            shopping_list[item] = False
        return redirect(url_for("index"))
    
    return render_template_string(HTML_TEMPLATE, shopping_list=shopping_list)

@app.route("/toggle", methods=["POST"])
def toggle():
    item = request.form.get("item")
    if item in shopping_list:
        shopping_list[item] = not shopping_list[item]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
