from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

jedi = "of the jedi"

@app.route('/aa')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/aa')

    return "of the jedi"




@app.route('/update/<int:id>')
def updateRoute(id):
    entry = Entry.query.get(id)
    if not id or id != 0:
        return render_template('update.html', entry=entry)
    else:
        db.session.delete(entry)
        db.session.commit()
        return redirect('/aa')
    return "of the jedi"
        


############################################################

# @app.route('/update/<int:id>')
# def updateRoute(id):
#     if not id or id != 0:
#         entry = Entry.query.get(id)
#         if entry:
#             return render_template('update.html', entry=entry)

#     # return "of the jedi"

# @app.route('/update', methods=['GET', 'POST'])
# def update():
#     if not id or id != 0:
#         entry = Entry.query.get(id)
#         if entry:
#             db.session.delete(entry)
#             db.session.commit()
#             return redirect('/aa')

#     return "of the jedi"

############################################################

@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/aa')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/aa')

    return "of the jedi"

@app.route('/')                          # app 을 bp로 바꿔줌
def index1():
    return render_template('index c.html')

@app.route('/user/')                    # main_route로 옮겨 줌
def create1():
    # User.query
    return render_template('user.html')

@app.route('/compare')
def update1():
    return render_template('compare_user.html')

@app.route('/content')
def update12():
    return render_template('content.html')


# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"