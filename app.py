from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USE_SSL'] = False 
app.config['MAIL_USERNAME'] = 'unidosporeldeportemtb@gmail.com' 
app.config['MAIL_PASSWORD'] = 'pfvttqtdqeclwmsr'
app.config['MAIL_DEFAULT_SENDER'] = 'unidosporeldeportemtb@gmail.com' 
 
mail = Mail(app)
app.secret_key = "clavesecreta"

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
        "auspiciantes": ["google", "youtube", "linkedin", "shopify", "rebel"],
        "telefono": "(011) 555-5555",
        "email": "info@clubdeportivo.com.ar",
        "sociales": {
            "facebook": "https://www.facebook.com/unidosporeldeporte",
            "instagram": "https://www.instagram.com/unidosporeldeporte",
            "twitter": "https://www.twitter.com/unidosporedeporte"
        }
    },
    2: {
        "kit_carrera": ["Número de corredor (dorsal) con chip de cronometraje.",
				"Remera técnica o jersey oficial del evento.",
				"Botella de agua o bebida isotónica.",
				"Barra energética o gel de nutrición.",
				"Mapa del circuito y reglamento impreso. ",
				"Deslinde de responsabilidad (si no fue firmado online).",
				"Bolsa o mochila oficial del evento.",
				"Souvenirs y material promocional de los sponsors.",
				"Pulsera o credencial de identificación del corredor.",
				"Ticket para hidratación o lunch post-carrera."]
    }
}
    
@app.route('/')
def home():
    return render_template('index.html', evento=info_evento[1], kit=info_evento[2]["kit_carrera"])

@app.route('/formulario', methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        categoria = request.form.get("categoria")
        nombre = request.form.get("name")
        apellido = request.form.get("last_name")
        dni = request.form.get("documento")
        correo = request.form.get("correo")

        body = f"""
        Nuevo competidor inscripto:

        Nombre: {nombre} {apellido}
        DNI: {dni}
        Correo: {correo}
        Categoría: {categoria}
        """

        try:
            msg = Message("Nueva inscripción a la carrera",
                          recipients=["unidosporeldeportemtb@gmail.com"])
            msg.body = body
            mail.send(msg)
            flash("Inscripción enviada con éxito", "success")
        except Exception as e:
            flash(f"Error enviando correo: {str(e)}", "danger")

        return redirect("formulario")

    return render_template("registration.html", evento=info_evento[1])

@app.errorhandler(404)
def error(e):
    return render_template('error.html', evento=info_evento[1]),404

if __name__ == '__main__':
    app.run('localhost', port=5002, debug=True)

