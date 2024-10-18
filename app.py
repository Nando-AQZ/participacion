from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto a una clave secreta real en producción

# Diccionario de ejemplo con usuarios y contraseñas
users = {
    "fernando": "12345","nano": "123"  # En producción, usa hashes de contraseñas en lugar de texto claro
}

@app.route("/", methods=['GET'])
def index():
    if 'user' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get("nombre")
        password = request.form.get("password")
        
        if nombre in users and users[nombre] == password:
            session['user'] = nombre
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', error='Credenciales incorrectas')
    
    return render_template('login.html')

@app.route("/inicio")
def inicio():
    if 'user' in session:
        return render_template('inicio.html', user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/atras")
def atras():
    
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
