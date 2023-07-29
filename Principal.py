import win32console
import win32gui

from dateutil import parser # convertir string a formato de hora
import os
import pyautogui  # Controlar el raton, tomar ss
import webbrowser  # Para abrir paginas web
import time
import AdministracionBD as bd
from time import sleep  # Detener la ejecicion
from datetime import date  # Fecha
from datetime import datetime  # Hora
from plyer import notification  # Para mostrar notificaciones
import pytesseract
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'



# zoom de la pantalla en 110 y full screen

# variables fijas
url_bot_liderboard = "https://www.duolingo.com/leaderboard"
url_bot_perfil = "https://www.duolingo.com/profile/V1PRIME"
# cuento optimo 
url_cuento = "https://www.duolingo.com/stories/en-es-something-to-drink?mode=read&practiceHubStory=featured"

tiempoInicio = ""
tiempoFinal = ""
tiempoInicioF = ""
tiempoFinalF = ""
mensaje_finalizacion_cuento = ""

cuento_tiempo_inicio = time.time()
cuento_tiempo_final = time.time()

iniciar = False
pares_una_vez = True
haciendo_cuento = True
continuar_activado = True
pares_terminados = False
cuento_empezar=True

ultimaSesion = 0
cantidad_de_cuentos_a_resolver = 1
hora_iniciar = ""


def notificacionGenerica(mensaje):
    notification.notify(
        title='DUO BOT',
        message=mensaje,)

def obtenerPosicionRaton():
    if str(input()) == "p":
        print(pyautogui.position())

def menu_princial():
    opcion = 0
    print("DUO BOT TRY HARD 1.0")
    print("Ver Seciones")
    
def validar_hora_inicio():
    fecha_actual = "" 
    # obtengo la fecha actual y la formateo 
    # obtengo la fecha actual y la formateo
    hoy = date.today()
    fecha_actual_sistema = ""
    fecha_actual_sistema = str(hoy.day)+"/"+str(hoy.month)+"/"+str(hoy.year)
    fecha_actual_sistema_formateada = datetime.strptime(fecha_actual_sistema, "%d/%m/%Y")
    # pido la fecha formato "20/07/2023"
    fecha_actual = str(input("ingrese la fecha de hoy "))
    fecha_formateada = datetime.strptime(fecha_actual,"%d/%m/%Y")


# devuelve verdadero o falso
def detectar_cuanto_tiempo_falta(_hora_iniciar):
    una_vez = False
    # 
    #hora2 = "22:45:00"
    hora_actual = datetime.now().time()
    hora_inicio_formateada = parser.parse(_hora_iniciar).time()
    #hora1_formateada = parser.parse(hora1).time()
    #hora2_formateada = parser.parse(hora2).time()
    #print(hora_actual > hora_inicio_formateada)
    if hora_actual > hora_inicio_formateada and una_vez==False:
        una_vez = True
        #iniciar = True
        return True
    else:
        return False
# toma captura a las 10 palabras
def resolver_pares():
    global pares_terminados
    pares_español=["","","","",""]
    pares_ingles=["","","","",""]
    
    # algunas palabas las tiene que escribir "mal" porque asi las lee
    # aveces pone mayusculas,
    pares_soluciones = {"leche\n\x0c": "milk\n\x0c",
                        "con\n\x0c": "with\n\x0c",
                        "jugo\n\x0c": "juice\n\x0c",
                        "por favor\n\x0c": "please\n\x0c",
                        "azucar\n\x0c": "sugar\n\x0c",
                        "gracias\n\x0c": "thank you\n\x0c",
                        "té\n\x0c": "tea\n\x0c",
                        "refresco\n\x0c": "soda\n\x0c",
                        "esta bien\n\x0c": "OK\n\x0c",
                        "si\n\x0c": "yes\n\x0c"}
    instrucciones_español = ["", "", "", "", ""]
    instrucciones_ingles = ["", "", "", "", ""]
    todas_instrucciones = ["1", "2", "3", "4","5","6","7","8","9","0"]
    # Tomar ss de las palabra
    pyautogui.screenshot('ss_uno.png',   region=(470, 270, 205, 45))
    pyautogui.screenshot('ss_dos.png',   region=(470, 335, 205, 45))
    pyautogui.screenshot('ss_tres.png',  region=(470, 405, 205, 45))
    pyautogui.screenshot('ss_cuatro.png',region=(470, 470, 205, 45))
    pyautogui.screenshot('ss_cinco.png', region=(470, 535, 205, 45))
    pyautogui.screenshot('ss_seis.png',  region=(780, 270, 205, 45))
    pyautogui.screenshot('ss_siete.png', region=(780, 335, 205, 45))
    pyautogui.screenshot('ss_ocho.png',  region=(780, 405, 205, 45))
    pyautogui.screenshot('ss_nueve.png', region=(780, 470, 205, 45))
    pyautogui.screenshot('ss_cero.png',  region=(780, 535, 205, 45))

    # Convertimos las palabras en texto y los almacenamos en una lista
    pares_español[0] = pytesseract.image_to_string("ss_uno.png")
    pares_español[1] = pytesseract.image_to_string("ss_dos.png")
    pares_español[2] = pytesseract.image_to_string("ss_tres.png")
    pares_español[3] = pytesseract.image_to_string("ss_cuatro.png")
    pares_español[4] = pytesseract.image_to_string("ss_cinco.png")
    pares_ingles[0] = pytesseract.image_to_string("ss_seis.png")
    pares_ingles[1] = pytesseract.image_to_string("ss_siete.png")
    pares_ingles[2] = pytesseract.image_to_string("ss_ocho.png")
    pares_ingles[3] = pytesseract.image_to_string("ss_nueve.png")
    pares_ingles[4] = pytesseract.image_to_string("ss_cero.png")

    # Busca la solucion
    for i in range(5):
        omitir = False
        try:
            index_ingles = pares_ingles.index(pares_soluciones.get(pares_español[i]))+6
        except:
            print("PALABRA NO ENCONTRADA")
            omitir = True
        
        if omitir==False:
            if index_ingles == 10:
                index_ingles = 0      
            instrucciones_español[i] = str(i+1)
            instrucciones_ingles[i] = str(index_ingles)
            todas_instrucciones.remove(str(i+1))
            todas_instrucciones.remove(str(index_ingles))
    
    # Ejecuta la solucion
    pyautogui.click()
    for x in range(5):     
        pyautogui.press(instrucciones_español[x])
        pyautogui.press(instrucciones_ingles[x])

    # intrucciones extra, en caso de no detectar uno o dos palabras
    if len(todas_instrucciones)!=0:
        if len(todas_instrucciones) == 2:
            pyautogui.press(todas_instrucciones[0])
            pyautogui.press(todas_instrucciones[1])
        if len(todas_instrucciones) == 4:
            pyautogui.press(todas_instrucciones[0])
            pyautogui.press(todas_instrucciones[2])
            pyautogui.press(todas_instrucciones[0])
            pyautogui.press(todas_instrucciones[3])
            pyautogui.press(todas_instrucciones[1])
            pyautogui.press(todas_instrucciones[2])
            pyautogui.press(todas_instrucciones[1])
            pyautogui.press(todas_instrucciones[3])
    
    pares_terminados = True
    sleep(1)
    pyautogui.press("Enter")
    #print("")
    #print(pares_español)
    #print(pares_ingles)
    #print(todas_instrucciones)
    #print(instrucciones_español)
    #print(instrucciones_ingles)
    #print("")

#     ______________________________________________________________    
#   /|                                                              |   
#  | |                        PROCEDIMIENTOS                        |   
#  | |______________________________________________________________|   
#  |/______________________________________________________________/    
#                                                                       
def detectar_sesion_hoy():
    global hora_iniciar
    global cantidad_de_cuentos_a_resolver
    hoy = date.today()
    fecha_actual_sistema = ""
    #formatear
    fecha_actual_sistema = str(hoy.day)+"/"+str(hoy.month)+"/"+str(hoy.year)
    #fecha_actual_sistema_formateada = datetime.strptime(fecha_actual_sistema, "%d/%m/%Y")
    #print(fecha_actual_sistema)
    resultado = bd.buscar_sesion_por_fecha(fecha_actual_sistema)
    hora_iniciar = resultado[0][0]
    cantidad_de_cuentos_a_resolver = resultado[0][1]

def configuirar_sesion():
    fecha_actual_ingresada = ""
    hora_inicial_ingresada = ""
    segundo = "00"
    cuentos = 0

    sesion = bd.obtener_numero_ultima_sesion_mas_uno()
    print("INGRESA LA FECHA DE LA SIGUIENTE SESION")
    dia = str(input("Ingrese el dia -> "))
    mes = str(input("Ingrese el mes -> "))
    año = str(input("Ingrese el año -> "))
    print("INGRESA LA HORA DE INICIO (FORMATO 24 HORAS)")
    hora_inicio = str(input("Ingrese la hora -> "))
    minuto_inicio = str(input("Ingrese los minutos -> "))
    print("INGRESA EL NUMERO DE CUENTOS A RESOLVER")
    cuentos = int(input("Ingresa la cantidad de cuentos a resolver -> "))
    # formateo la fecha ingresada
    # creo que le faltan los ceros
    fecha_actual_ingresada = str(dia)+"/"+str(mes)+"/"+str(año)
    fecha_actual_ingresada_formateada = datetime.strptime(fecha_actual_ingresada,"%d/%m/%Y")
    # formateo la hora 
    hora_inicial_ingresada = str(hora_inicio)+":"+str(minuto_inicio)+":"+str(segundo)
    hora_inicial_ingresada_formateada = parser.parse(hora_inicial_ingresada).time()
    # la fecha y las horas formateadas no se las pasamos a la base de datos 
    bd.ingresar_secion(sesion,fecha_actual_ingresada,hora_inicial_ingresada,cuentos)

def empezar_cuento():
    # abro la ventana
    webbrowser.open(url_cuento, new=2, autoraise=True) 
    # espero unos segundos (mejorarlos)
    sleep(4)
    # hago pantalla completa
    pyautogui.click()
    pyautogui.press("F11")    
# contiene -> "cuento_tiempo_inicio"
def detectar_empezar_cuento():
    global cuento_empezar
    global cuento_tiempo_inicio
    if cuento_empezar:
        if str(pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\DetectarEmpezarCuento.png", grayscale=False, confidence=.7)) != "None":
            pyautogui.press("Enter")
            c_t_i = time.ctime()
            c_t_i_s= c_t_i.split()
            cuento_tiempo_inicio = c_t_i_s[3]
            cuento_empezar = False

def detectar_continuar():
    global detectar_continuar
    if continuar_activado:
        if str(pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\Continuar.png", grayscale=False, confidence=.9)) != "None":
            pyautogui.press("Enter")
def detectar_seleccionar():
    global pares_una_vez
    global continuar_activado
    if pares_una_vez:
        if str(pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\SeleccionaLosPares.png", grayscale=False, confidence=.7)) != "None":
            resolver_pares()
            pares_una_vez = False
            continuar_activado = False
def detectar_si():
    if str(pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\Si.png", grayscale=False, confidence=.7)) != "None":
        pos_si = pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\Si.png", grayscale=False, confidence=.7)
        pyautogui.moveTo(pos_si[0]+20,pos_si[1]+20)
        pyautogui.click()

# contiene -> "cuento_tiempo_final"
# contiene -> "mensaje_finalizacion_cuento"
def detectar_fin_cuento():
    global haciendo_cuento
    global pares_terminados
    global cuento_tiempo_final
    global mensaje_finalizacion_cuento
    una_vez = False
    tiempo_de_espera_superado = False

    if pares_terminados:
        tiempo_inicial = time.time()
        while True:
            if time.time()-tiempo_inicial<=10 and una_vez==False:
                if str(pyautogui.locateOnScreen("Imagenes\DetectarSobrePantalla\Completaste.png", grayscale=False, confidence=.7)) != "None":
                    haciendo_cuento = False
                    break
            elif time.time()-tiempo_inicial>30:
                tiempo_de_espera_superado = True
                break
        c_t_f = time.ctime()
        c_t_f_s = c_t_f.split()
        cuento_tiempo_final = c_t_f_s[3]
        if tiempo_de_espera_superado:
            # leccion perdida
            mensaje_finalizacion_cuento = "ERROR"
            pyautogui.click()
            pyautogui.hotkey("alt", "f4")
            pyautogui.press("ENTER")
        else:
            mensaje_finalizacion_cuento = "COMPLETADO"

def cerrar_pagina():
    pyautogui.hotkey("alt", "f4")
    pyautogui.press("ENTER")
def inicio_sesion():
    # Obtengo la fecha y hora del inicio de sesion
    fecha_actual = time.ctime()
    # Obtengo la cantidad de puntos antes del inicio de sesion
    # Abro la pagina de perfil del bot
    webbrowser.open(url_bot_perfil, new=0, autoraise=True)
    #sleep(2)
    #pyautogui.moveTo(25, 115)
    #pyautogui.click()
    sleep(2)
    pyautogui.moveTo(150, 695)
    sleep(1)
    pyautogui.click()
    pyautogui.press("F11")
    sleep(4)
    ss_experiencia = pyautogui.screenshot(
        'ssExperiencia.png', region=(650, 340, 100, 40))
    # Falta convertir esa imagen en texto
    sleep(1)
    # Abro la pagina del liderboard
    webbrowser.open(url_bot_liderboard, new=0, autoraise=True)
    sleep(4)
    # Obtengo la posicion en el liderboard
    ss_division = pyautogui.screenshot(
        'ssDivision.png', region=(470, 145, 250, 50))
    # Detecto donde esta el nombre del bot
    posicionNombre = pyautogui.locateCenterOnScreen(
        "Imagenes\DetectarSobrePantalla\otBlanco.png")
    print(posicionNombre)
    if posicionNombre == None:
        posicionNombre = pyautogui.locateCenterOnScreen(
            "Imagenes\DetectarSobrePantalla\otRojo.png")
    if posicionNombre == None:
        posicionNombre = pyautogui.locateCenterOnScreen(
            "Imagenes\DetectarSobrePantalla\otNegro.png")
    if posicionNombre == None:
        posicionNombre = pyautogui.locateCenterOnScreen(
            "Imagenes\DetectarSobrePantalla\otVerde.png")
    # FALTA EL VERDE

    print(posicionNombre)
    ss_posicion_lider = pyautogui.screenshot('ssPosicion.png', region=(
        posicionNombre[0]-180, posicionNombre[1]-20, 50, 55))
    # Convierto las imagenes a texto
    texto_division = pytesseract.image_to_string("ssDivision.png")
    texto_experiencia = pytesseract.image_to_string("ssExperiencia.png")
    texto_posicion = pytesseract.image_to_string("ssPosicion.png")
    # formateo la division
    texto_division_split = str(texto_division).split()
    texto_experiencia_split = str(texto_experiencia).split()

    if texto_posicion == None:
        texto_posicion = "-1"

    # print("SALIDA")
    # print("DIVISION ACTUAL -> "+str(texto_division_split[1]))
    # print("EXPERIENCIA -> "+str(texto_experiencia_split[0]))
    # Valido la posicion
    #if texto_posicion_split == []:
        # print("POSICION -> -1")
    #    texto_posicion_split[0] = "-1"
    # Obtengo el ultimo INICIOde secion
    numero_inicio_sesion = bd.obtener_ultimo_INICIO_sesion_mas_uno()
    # obtengo la fecha
    hoy = date.today()
    fecha_actual_sistema = ""
    fecha_actual_sistema = str(hoy.day)+"/"+str(hoy.month)+"/"+str(hoy.year)
    fecha_actual_sistema_formateada = datetime.strptime(
        fecha_actual_sistema, "%d/%m/%Y")
    print(texto_division_split[1])
    print(texto_experiencia_split[0])
    print(texto_posicion)
    # print("ID INICIO SESION -> "+str(numero_inicio_sesion))
    # print("FECHA -> "+str(fecha_actual_sistema_formateada))
    # Ingresamos todos los datos
    bd.ingresar_inicio(numero_inicio_sesion, fecha_actual,
                       texto_division_split[1], texto_experiencia_split[0], texto_posicion)
    pyautogui.click()
    pyautogui.hotkey("alt", "f4")


# para ocultar la ventana del cmd
ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

def principal(): 
    global haciendo_cuento
    global pares_una_vez
    global continuar_activado
    global pares_terminados
    global cuento_empezar
    salir_ciclo = False
    
    
    
    """
    detectar_sesion_hoy()

    while True:
        salir_ciclo = detectar_cuanto_tiempo_falta(hora_iniciar)
        if salir_ciclo:
            break
        sleep(1)
    """
    inicio_sesion()
  
    for c in range(cantidad_de_cuentos_a_resolver):
        haciendo_cuento = True
        pares_una_vez = True
        continuar_activado = True
        pares_terminados = False
        cuento_empezar = True
        empezar_cuento()
        while haciendo_cuento:
            detectar_empezar_cuento()
            detectar_fin_cuento()       
            detectar_si()
            detectar_seleccionar()
            detectar_continuar()
        # GUARDAMOS EL CUENTO EN LA BASE DE DATOS
        _idcuento = bd.obtener_ultimo_cuento()
        bd.generar_cuento(_idcuento,cuento_tiempo_inicio,cuento_tiempo_final,mensaje_finalizacion_cuento)
        cerrar_pagina()
        sleep(2)  
    os.sys.exit()

if __name__ == "__main__":
    principal()