#FINAL
#Computacion grafica
#2022
'''ELABORADO POR:
        ALICIA VALENCIA ACEVEDO
        RONALD MARIN CARDONA'''
#---------------------------------
#LIBRERIAS........................
import pygame as py
#---------------------------------
'''Nombre de la clase: VentanaP
Parametros: tam (Tamaño de la ventana)
            img (Imagen de la ventana)
Sirve para: Crea una Ventana de los tamaños establecidos
Retorna: La Ventana creada'''
class VentanaP:
    '''Constructor en el que se establece el tamaño y la imagen de la ventana'''
    def __init__(self,tam,img):
        self.tam=tam
        self.img=img
    '''Nombre del metodo: Iniciar
    Funcion: Sirve para iniciar la ventana con el tamaño e imagen seleccionada'''
    def Iniciar(self,y):
        py.init()
        self.Ventana= py.display.set_mode(self.tam)
        self.Ventana.blit(self.img,(0,y))
        py.display.flip()
        py.display.update()
        return self.Ventana
    '''Nombre del metodo: Actualizar 
    Funcion: Sirve para reiniciar la ventana'''
    def Actualizar(self):
        self.Ventana.blit(self.img,(0,-224))
        py.display.flip()
    '''Nombre del metodo: Rellenar
    Parametros: Color -> Color en RGB
    Funcion: Nos rellena de un color la ventana'''
    def Rellenar(self,color):
        self.Ventana.fill(color)
        py.display.flip()
        py.display.update()
    '''Nombre del metodo: Poner
    Parametros: Imagen -> Imagen
                Pos -> Posicion en la que queremos poner la imagen
    Funcion: Pone una imagen en la posicion indicada'''
    def Poner(self,Imagen,Pos):
        self.Ventana.blit(Imagen,Pos)


#--------------------------------------------------------------------
'''Nombre de la funcion: Select(y)
Parametros: y -> Posicion en y
Retorna: Cadena con el nombre de lo seleccionado
Funcion: Segun la posicion en y retornar la opcion seleccionada'''
def Select(y):
    if y>176 and y<231:
        return "Play"
    if y>257 and y<309:
        return 'Instrucciones'
    if y>341 and y<391:
        return 'Creditos'
    if y>420 and y<469:
        return 'Salir'
