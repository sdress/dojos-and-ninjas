from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def show_form():
    dojo_list = Dojo.get_all_dojos()
    return render_template('ninja_form.html', dojos=dojo_list)

@app.route('/ninjas/create', methods = ['POST'])
def add_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': int(request.form['age']),
        'dojo_id': int(request.form['dojo'])
    }
    print(data)
    Ninja.save_ninja(data)
    return redirect('/ninjas')