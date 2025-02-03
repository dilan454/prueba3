from flask import Flask, render_template_string

app = Flask(__name__)

# El contenido HTML que quieres mostrar
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hola mundo</h1>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_CONTENT)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Railway usa una variable de entorno para el puerto
    app.run(host="0.0.0.0", port=port)
