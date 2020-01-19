from webapp import app
from flask import render_template

@app.route('/')
@app.route('/index')



def index():
    users = [
    {'id': 1, 'first_name': "Tom",'last_name': "Bom", 'pid': 1, 'department': "A"},
    {'id': 2, 'first_name': "Maya",'last_name': "Yala", 'pid': 2, 'department': "A"},
    {'id': 3, 'first_name': "Omri",'last_name': "Aviv`", 'pid': 5, 'department': "C"},
    {'id': 4, 'first_name': "Dani",'last_name': "Yosh", 'pid': 14, 'department': "B"}
    ]

#    users = [User.load(db, uid) for uid in db]
    return render_template('index.html', users=users)
