from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = False 
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' 
app.config['MAIL_PASSWORD'] = 'your-email-password' security 
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com' 
 
mail = Mail(app)

info_evento = {
    1: {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...",
        "fecha": "24 de Octubre de 2025",
        "horario": "8am",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {
            1: {"nombre": "Corta", "valor": "100"},
            2: {"nombre": "Larga", "valor": "200"}
        },
        "Auspiciantes": ["ausp1", "ausp2"]
    }
}
    
@app.route('/')
def home():
    return render_template('index.html', evento=info_evento[1])

@app.route('/formulario', methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        categoria = request.form.get("categoria")
        nombre = request.form.get("name")
        apellido = request.form.get("last_name")
        dni = request.form.get("documento")
        correo = request.form.get("correo")
    return render_template("index.html")

if __name__ == '__main__':
    app.run('localhost', port=5002, debug=True)

