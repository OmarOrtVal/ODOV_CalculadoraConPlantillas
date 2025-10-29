from flask import Flask, render_template, url_for, request, redirect, flash, session


app = Flask(__name__)

@app.route('/peso/<altura>/<edad>/<genero>/<nivel_de_actividad>')
def registrar(peso, altura, edad, genero, nivel_de_actividad):
    print("--- Nuevo Registro ---")
    print(f"Peso: {peso}")
    print(f"Altura: {altura}")
    print(f"Edad: {edad}")
    print(f"Género: {genero}")
    print(f"Nivel de Actividad: {nivel_de_actividad}")
    print("----------------------")


    

if __name__ == '__main__':
    app.run(debug=True)