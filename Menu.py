#FINAL
#Computacion grafica
#2022
'''ELABORADO POR:
        ALICIA VALENCIA ACEVEDO
        RONALD MARIN CARDONA'''
#-----------------------------------------
#LIBRERIAS................................
from Juego import*
from Ventana import VentanaP,Select
import pygame as py
#-----------------------------------------
def MenuJuego():
    '''
    Nombre de la funcion: MenuJuego

    Parametros: Ninguno

    Sirve para: Es el menu del juego.        

    Retorna: No retorna nada

    '''
    #Imagenes del juego
    Principal= py.image.load("Principal.png") #Imagen principal del juego
    Creditos= py.image.load("flatboy\Fondo\Creditos.png")  #Imagen de creditos
    Instrucciones= py.image.load("flatboy\Fondo\Instrucciones.png") #Imagen de instrucciones

    #Llamado a clase VentanaP
    Ventana1=VentanaP((900,506),Principal) 
    Ventana1.Iniciar(0)
    Iniciar=True
    Seleccion="Play"
    ValidadorVentana=False #Valida que imagen abrir.

    # Musica de fondo
    py.mixer.init()
    Sonido= py.mixer.Sound("Musica\Menu.mp3")
    Sonido.set_volume(0.9)
    Sonido.play() 


    while Iniciar:
        for event in py.event.get():
            if event.type==py.QUIT:
                if Seleccion=="Play":
                    exit()
                else: 
                    Iniciar=False
            if event.type==py.MOUSEBUTTONDOWN:
                x,y=event.pos

                if x>561 and x<843 and not ValidadorVentana:
                    Seleccion=Select(y)
                else:
                    Seleccion=''
                if Seleccion=="Play":
                    Sonido.stop()
                    i=Juego()

                    if i!=None:
                        MenuJuego() 
                if Seleccion=="Instrucciones":
                    
                    Ventana1.Poner(Instrucciones,(0,0))
                    py.display.flip()
                    ValidadorVentana=True
                if Seleccion=="Creditos":
                    
                    Ventana1.Poner(Creditos,(0,0))
                    py.display.flip()
                    ValidadorVentana=True
                if Seleccion=="Salir":
                   exit()

    py.display.quit()
    if not Iniciar:
        MenuJuego()
MenuJuego()