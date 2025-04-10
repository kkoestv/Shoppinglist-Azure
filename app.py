from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Handleliste lagret i minnet som dict: {"Melk": False}
handleliste = {
    "Melk": False,
    "Brød": False,
    "Egg": False
}

# HTML + CSS template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Handleliste</title>
    <style>
        body {
            background-color: #f5f5dc; /* beige */
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            margin: 0;
            padding-top: 50px;
        }
        .notatblokk {
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
        .ferdig {
            text-decoration: line-through;
            color: #777;
        }
        form.ny-vare {
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
    <div class="notatblokk">
        <h1>Handleliste</h1>
        <form method="POST" action="/toggle">
            <ul>
                {% for vare, ferdig in liste.items() %}
                    <li>
                        <input type="checkbox" name="kryss_av" value="{{ vare }}" onchange="this.form.submit()" {% if ferdig %}checked{% endif %}>
                        <span class="{{ 'ferdig' if ferdig }}">{{ vare }}</span>
                    </li>
                {% endfor %}
            </ul>
        </form>

        <form method="POST" action="/" class="ny-vare">
            <input type="text" name="vare" placeholder="Ny vare" required>
            <button type="submit">Legg til</button>
        </form>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ny_vare = request.form.get("vare")
        if ny_vare and ny_vare not in handleliste:
            handleliste[ny_vare] = False
        return redirect(url_for("index"))
    
    return render_template_string(HTML_TEMPLATE, liste=handleliste)

@app.route("/toggle", methods=["POST"])
def toggle():
    kryssa_av = request.form.get("kryss_av")
    if kryssa_av in handleliste:
        handleliste[kryssa_av] = not handleliste[kryssa_av]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
