from flask import Flask, render_template,request
from conexion import *
app=Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Login():
    if request.method== 'POST':
        ID=int(request.form['ID'])
        Register=Getregistro()
        id_reg=Register[0]
        name=Register[1]
        work=Register[2]
        
        return render_template('base.html',Register=Register,id_reg=id_reg,name=name,work=work)
    return render_template('base.html')

def Getregistro():
    ID=int(request.form['ID'])

    cursor.execute('SELECT database();')
    registro=cursor.fetchone()
    select= "SELECT * FROM registro WHERE id = %(ID)s"
    cursor.execute(select,{'ID':ID})

    resultado=cursor.fetchall()
    for respuesta in resultado:
        id_reg=(respuesta[0])
        name=(respuesta[1])
        work=(respuesta[2])
        result=[id_reg,name,work]
        print(id_reg,name,work)
    print(registro)
    return result

if __name__ == '__main__':
    app.run(debug=True)