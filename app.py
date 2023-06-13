from multiprocessing import connection
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/updatesalary')
def updatesalary():
   return render_template('updatesalary.html')

@app.route('/remove')
def remove():
   return render_template('remove.html')

@app.route('/find')
def find():
   return render_template('find_person.html')

@app.route('/put_pic')
def put_pic():
   return render_template('show_pics.html')

@app.route('/updatekey')
def updatekey():
   return render_template('updatekey.html')

@app.route('/upload_pic')
def addpic():
   return render_template('upload_pic.html')

@app.route('/all', methods=['POST','GET'])
def full_list():
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    querry="Select * from people "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("list.html",rows = rows)

@app.route('/update_sal',methods=['POST','GET'])
def update_sal():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['sal'])
        querry="UPDATE people SET grade = '"+keyword+"'   WHERE name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/update_key',methods=['POST','GET'])
def updatek():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        querry="UPDATE people SET notes = '"+keyword+"'   WHERE name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/addpic',methods=['POST','GET'])
def addpicture():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        currsor = connection.cursor()
        name= str(request.form['name1'])
        pic= str(request.form['pic1'])
        querry="UPDATE people SET picture = '"+pic+"'   WHERE name ='"+name+"' "
        currsor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        currsor.execute(querry2)
        rows = currsor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/remove_person', methods=['GET', 'POST'])
def deleterecord():
    if (request.method=='POST'):
        connection = sqlite3.connect('people.db')
        cursor = connection.cursor()
        name= str(request.form['name'])
        querry="DELETE FROM people WHERE name ='"+name+"' "
        cursor.execute(querry)
        connection.commit()
        querry2="Select * from people "
        cursor.execute(querry2)
        rows = cursor.fetchall()
        connection.close()
    return render_template("list.html",rows = rows)

@app.route('/find_deets', methods=['POST','GET'])
def list():
    connection = sqlite3.connect('people.db')
    cursor = connection.cursor()
    field=str(request.form['name'])
    querry="Select * from people WHERE name =  '"+field+"' "
    cursor.execute(querry)
    rows = cursor.fetchall()
    connection.close()
    return render_template("show_pics.html",rows = rows)

if __name__ =="__main__":
    app.run(port=8000)
    