from flask import Flask, render_template, request
from deta import Deta
app = Flask(__name__)

deta = Deta("c0uJEdiLS8zv_tATyVLnLAD5TL2QTqcNkPhWCXRZQbZwY")

# This how to connect to or create a database.
db = deta.Base("sachin_db")

@app.route("/pib/")
def pib():
    return render_template('pib.html')


@app.route("/")
def hello_world():
    return notes()

@app.route("/delete/<key>")
def delete(key):
    db.delete(key)
    return notes()

@app.route("/notes", methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        if request.form['key']:
            db.put({ 
                "title" : request.form['title'], 
                "msg" : request.form['msg'],
                "date" : request.form['date']
                },request.form['key'])
        else:
            db.put({ 
                "title" : request.form['title'], 
                "msg" : request.form['msg'],
                "date" : request.form['date']
                })
        
    context = {
        "data" : db.fetch().items
    }
    return render_template('notes.html', context = context)

if __name__ == '__main__':
    app.run()
