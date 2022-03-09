from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/dojos')
def show_all_dojos():
    all_dojos = Dojo.get_all_dojos()
    print(all_dojos)
    return render_template('index.html', dojos=all_dojos)

@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.make_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<id>')
def show_dojo(id):
    data = {
        'id': id,
        'dojo_id': id
    }
    dojo = Dojo.get_one_dojo(data)
    print(dojo)
    ninjas = Ninja.get_dojo_ninjas(data)
    return render_template('show_dojo.html', dojo=dojo, ninjas=ninjas)

if __name__ == "__main__":
    app.run(debug = True)