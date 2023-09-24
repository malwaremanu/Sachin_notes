import json, os 
from flask import Flask, render_template, request
from deta import Deta
app = Flask(__name__)

deta = Deta("c0uJEdiLS8zv_tATyVLnLAD5TL2QTqcNkPhWCXRZQbZwY")

# This how to connect to or create a database.
db = deta.Base("sachin_db")

@app.route("/pib/")
def pib():
    context = deta.Base("pib_db").fetch().items   

    nc = []
    for c in context[:10]:
        for a in json.loads(c['msg']):
            print(a)
            print("--"*5)

    # for c in context[:10]:
    #     for a in json.loads(c['msg'])[0]['infos']:
    #         nc.append(a)

        print("----"*20)
    return render_template('agri.html', context=nc)


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
        print(request.form['msg'])
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



@app.route("/test", methods=['GET', 'POST'])
def test():            
    return render_template('test.html')


if __name__ == '__main__':
    app.run()
