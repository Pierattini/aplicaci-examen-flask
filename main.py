from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios predefinidos para Ejercicio 2
usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        # Aplicar descuentos según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_total = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_total

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento_total=descuento_total, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        # Verificación de usuario
        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == 'juan':
                mensaje = f'Bienvenido Administrador {nombre}'
            elif nombre == 'pepe':
                mensaje = f'Bienvenido Usuario {nombre}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
