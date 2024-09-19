from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Ejemplo de cómo manejar un formulario y procesar datos
        n1 = float(request.form.get('n1', 0))
        n2 = float(request.form.get('n2', 0))
        n3 = float(request.form.get('n3', 0))
        asistencia = int(request.form.get('asistencia', 0))
        promedio = (n1 + n2 + n3) / 3
        if promedio >= 40 and asistencia >= 75:
            resultado = 'Aprobado'
            # ruta = '/static/img/aprobado.jpg'
        else:
            resultado = 'Reprobado'
            # ruta = '/static/img/reprobado.jpg'
        return render_template('ejercicio1.html', promedio=promedio, resultado=resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nom1 = request.form.get('nom1', '')
        nom2 = request.form.get('nom2', '')
        nom3 = request.form.get('nom3', '')
        if len(nom1) > len(nom2) and len(nom1) > len(nom3):
            mayor = nom1
            cantidad = len(nom1)
        elif len(nom2) > len(nom1) and len(nom2) > len(nom3):
            mayor = nom2
            cantidad = len(nom2)
        else:
            mayor = nom3
            cantidad = len(nom3)
        return render_template('ejercicio2.html', mayor=mayor, cantidad=cantidad)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)