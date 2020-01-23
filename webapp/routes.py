from werkzeug.utils import redirect

from webapp import app
from flask import render_template, url_for, json, request
from .mydb import *

initdb()
add_emp("firstA", "last", "depA", "2")
add_emp("firstB", "last", "depA", "3")
add_emp("firstC", "last", "depA", "4")
add_emp("firstD", "last", "depA", "5")

print("UPDATE: " + update_emp('108', 'S', 'F', 'A', '77').__str__())
users = get_emps_all()
for user in users:
    print(user)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', users=get_emps_all())

@app.route('/<int:id>/delete')
def delete(id):
    del_emp(id)
    return redirect(url_for('index'))

@app.route('/user/<int:id>')
def edit(id):
    emp = get_emp(id)
    print(emp)
    return render_template('user.html', emp=get_emp(id))

@app.route('/add', methods=['GET', 'POST'])
def signup():
    first_name = request.form['first_name']
    print("The email address is '" + first_name + "'")
    return redirect(url_for('index'))
