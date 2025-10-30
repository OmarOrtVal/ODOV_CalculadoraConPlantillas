from flask import Flask, render_template, request

app = Flask(__name__)

FACTORES_ACTIVIDAD = {
    "sedentario": 1.2,
    "ligera": 1.375,
    "moderada": 1.55,
    "alta": 1.725
}

@app.route('/', methods=['GET', 'POST'])
def calculadora_get():
    tmb = None
    get = None
    
    if request.method == 'POST':
            peso = float(request.form['peso']) 
            altura = float(request.form['altura']) 
            edad = int(request.form['edad']) 
            genero = request.form['genero'] 
            actividad = request.form['actividad'] 

            if genero == 'hombre':
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
            elif genero == 'mujer':
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

            factor_actividad = FACTORES_ACTIVIDAD.get(actividad)
            
            if factor_actividad:
                get = tmb * factor_actividad
                
    return render_template('formulario.html', tmb=tmb, get=get)

if __name__ == '__main__':
    app.run(debug=True)