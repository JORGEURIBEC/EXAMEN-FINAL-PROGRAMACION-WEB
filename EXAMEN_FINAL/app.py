from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta principal (menú con dos botones)
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        # Calcular descuento según la edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')


# Ruta para el Ejercicio 2 (autenticación)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    mensaje = ''

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f'Bienvenido {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
