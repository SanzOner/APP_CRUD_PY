from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'legendary'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Retorna la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Retorna la página de administrador de usuarios
@app.route('/usuarios')
def index_usuarios():
    sql = "SELECT * FROM usuarios"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    conexion.commit()
    return render_template('modules/usuarios/index2.html', usuarios=usuarios)

# Crear un nuevo usuario
@app.route('/usuarios/create/guardar', methods=['POST'])
def guardar_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha = request.form['fecha']
    sql = "INSERT INTO usuarios (nombre, apellido, fecha) VALUES (%s, %s, %s)"
    datos = (nombre, apellido, fecha)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect(url_for('index_usuarios'))

# Actualizar un usuario existente
@app.route('/usuarios/update/<int:id>', methods=['POST'])
def actualizar_usuario(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha = request.form['fecha']
    sql = "UPDATE usuarios SET nombre=%s, apellido=%s, fecha=%s WHERE id=%s"
    datos = (nombre, apellido, fecha, id)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect(url_for('index_usuarios'))

# Eliminar un usuario
@app.route('/usuarios/delete/<int:id>')
def eliminar_usuario(id):
    sql = "DELETE FROM usuarios WHERE id=%s"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, (id,))
    conexion.commit()
    return redirect(url_for('index_usuarios'))

if __name__ == '__main__':
    app.run(debug=True)