import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Alessandro18',  # Cambia esto a tu contraseña real de MySQL
        db='escuela',
        cursorclass=pymysql.cursors.DictCursor
    )
