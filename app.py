from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Enkel handleliste lagret i minnet
handleliste = ["Melk", "Brød", "Egg"]

# HTML-template som string (for enkelhets skyld)
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Handleliste</title>
</head>
<body>
    <h1>Min handleliste</h1>
    <ul>
        {% for item in liste %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>

    <form method="POST" action="/">
        <input type="text" name="vare" placeholder="Ny vare" required>
        <button type="submit">Legg til</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ny_vare = request.form.get("vare")
        if ny_vare:
            handleliste.append(ny_vare)
        return redirect(url_for('index'))
    
    return render_template_string(HTML_TEMPLATE, liste=handleliste)

if __name__ == "__main__":
    app.run(debug=True)
