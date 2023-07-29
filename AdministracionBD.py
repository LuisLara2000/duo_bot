import os
import sqlite3

ruta_base_datos = "C:/DuoBotTryHard_Info/DuoBd"
#os.mkdir('C:/DuoBotTryHard_Info')

def crear_tablas():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS seciones(idsecion int(255), fecha char(12), horainicio char(10),numerocuentos int(255), PRIMARY KEY(idsecion))")
    cursor.execute("create table if not exists inicio_sesiones(idinicio int(255),sesiondia char(30),inicio char(30),experiencia char(5),posicion char(5),primary key(idinicio))")
    cursor.execute("create table if not exists resgitro_cuentos(idcuento int(255),horainicio char(30),horafin char(30),finalizacion char(15))")
    cursor.execute("create table if not exists mensajes_consola(idmensaje int(255),mensaje char(100))")

def ver_todas_seciones():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select * from seciones order by idsecion limit 3"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    #print(resultado)

def ingresar_secion(id_secion,fecha,hora_inicio,numero_cuentos):
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "insert into seciones(idsecion,fecha,horainicio,numerocuentos) values (?,?,?,?)"
    valores = (id_secion,fecha,hora_inicio,numero_cuentos)
    cursor.execute(sentencia,valores)
    #resultado = cursor.fetchall()
    bd.commit()


# el inicio de sesion esta en funcion a las seciones registradas
# por lo tanto se tiene que obtener el numero desecion del dia 
# tambien el ultmino jsjs
def buscar_sesion_por_fecha(fecha_actual):
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select horainicio,numerocuentos from seciones where fecha='"+str(fecha_actual)+"'"
    print(sentencia)   
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    return resultado


def obtener_ultimo_INICIO_sesion_mas_uno():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select idinicio from inicio_sesiones order by idinicio desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0

def obtener_numero_ultima_sesion_mas_uno():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select idsecion from seciones order by idsecion desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0

def obtener_ultimo_mensaje():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select idmensaje from mensajes_consola order by idmensaje desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0
    

def obtener_ultimo_cuento():
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "select idcuento from resgitro_cuentos order by idcuento desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0


def ingresar_inicio(_idinicio, _sesiondia, _inicio, _experiencia, _posicion):
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "insert into inicio_sesiones(idinicio,sesiondia,inicio,experiencia,posicion) values (?,?,?,?,?)"
    valores = (_idinicio, _sesiondia, _inicio, _experiencia, _posicion)
    cursor.execute(sentencia, valores)
    bd.commit()

def generar_mensaje(_idmensaje,_mensaje):
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "insert into mensajes_consola(idmensaje,mensaje) values (?,?)"
    valores = (_idmensaje, _mensaje)
    cursor.execute(sentencia, valores)
    bd.commit()

def generar_cuento(_idcuento,_horainicio,_horafin,_finalizacion):
    bd = sqlite3.connect(ruta_base_datos)
    cursor = bd.cursor()
    sentencia = "insert into resgitro_cuentos(idcuento,horainicio,horafin,finalizacion) values (?,?,?,?)"
    valores = (_idcuento, _horainicio, _horafin, _finalizacion)
    cursor.execute(sentencia, valores)
    bd.commit()




crear_tablas()
#ver_todas_seciones()