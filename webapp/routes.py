from werkzeug.utils import redirect

from webapp import app
from flask import render_template, url_for, request
from .mydb import *

initdb()
# add_emp("firstA", "last", "depA", "2")
# add_emp("firstB", "last", "depA", "3")
# add_emp("firstC", "last", "depA", "4")
# add_emp("firstD", "last", "depA", "5")
#
# print("UPDATE: " + update_emp('108', 'S', 'F', 'A', '77').__str__())
# users = get_emps_all()
# for user in users:
#     print(user)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', users=get_emps_all())

@app.route('/<int:id>/delete')
def delete(id):
    del_emp(id)
    return redirect(url_for('index'))



@app.route('/edit/<int:id>')
def edit(id):
    return render_template('edit.html', emp=get_emp(id)[0])

@app.route('/editpost', methods=['GET', 'POST'])
def editpost():
    # print("UPDATE: " + update_emp('108', 'S', 'F', 'A', '77').__str__())
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    emp_no = request.form.get('emp_no')
    department = request.form.get('department')
    id = request.form.get('id')
    print("Edit : " + first_name + last_name + id)
    update_emp(id, first_name, last_name, department, emp_no)
    return render_template('index.html', users=get_emps_all())

@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    emp_no = request.form.get('emp_no')
    department = request.form.get('department')
    print("Adding : " + first_name + last_name)
    add_emp(first_name, last_name, department, emp_no)
    return render_template('index.html', users=get_emps_all())
