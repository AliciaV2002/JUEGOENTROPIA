#FINAL
#Computacion grafica
#2022
'''ELABORADO POR:
        ALICIA VALENCIA ACEVEDO
        RONALD MARIN CARDONA'''
#---------------------------------------------------------
#LIBRERIAS................................................
import pygame as py 
import time
#---------------------------------------------------------
'''Nombre de la clase: Sprites
Contiene: En esta clase almacenamos los atributos del sprite
'''
class Sprites():
    '''
     Nombre de la calse:  Sprites

        Parametros: Ventana, prefijo,ancho,alto,xideal, VelX, VelY, CoorX, CoorY
        Ventana: Ventana donde se grafica
        prefijo: Carpeta donde se encuentra la imagen
        ancho: ancho de la imagen
        alto: alto de la imagen
        xideal: ancho de la imagen que se quiere
        VelX: Velocidad inicial del personaje en X
        VelY: Velocidad inicial del personaje en X
        CoorX: Coordenada del personaje en X
        CoorY: Coordenada del personaje en Y

        Sirve para: Contener todos los elementos del personaje
        
    '''
    def __init__(self, Ventana, prefijo,ancho,alto,xideal, VelX, VelY, CoorX, CoorY):

        self.Ventana = Ventana 
        self.prefijo = prefijo 
        self.ancho = ancho 
        self.alto = alto 
        self.xideal = xideal    
        self.VelX = VelX 
        self.VelY = VelY 
        self.CoorX = CoorX 
        self.CoorY = CoorY 
        self.Subio=False
        self.Act=False
        self.Ocolision=py.Rect(1,1,1,1)
        self.Try=False
    

    def cargar_animacion(self, movimiento, ValorRotacion1, ValorRotacion2,Actual):
        '''
       
        Nombre de la funcion: cargar_animacion


        Parametros: movimiento, ValorRotacion1, ValorRotacion2,Actual
            movimiento : Accion que va a realizar el personaje, caminar, saltar 
            ValorRotacion1, ValorRotacion2: valida hacia donde se dirige el personaje y
            se utiliza para ejecucion en el flip (se invierte la imagen)
            Actual: Sirve para saber si el personaje está a la derecha o izquiera
            

        Sirve para:
            Sirve para cargar cada imagen en el pygame y anexarla a una lista de imagenes
        
        Retorna:
            Lista de imagenes.      

        '''
        imagenes = []
        if (ValorRotacion1 and not ValorRotacion2 and Actual==0):
            self.CoorX-=48
        elif (not ValorRotacion1 and not ValorRotacion2 and Actual==1):
            self.CoorX+=48
        for i in range (1, 16):
            name =  self.prefijo + "\png\\" + movimiento + " (" + str(i) + ")" + ".png" 
            yideal = int((self.xideal*self.alto)/self.ancho)
            Img = py.transform.scale(py.image.load(name),(self.xideal,yideal))
            imagenes.append(py.transform.flip(Img.copy(), ValorRotacion1, ValorRotacion2))
            
        
        return imagenes

    def mostrar_animacion(self, imagenes, freq, x, y):
        '''
        Nombre de la funcion: mostrar_animacion

        Parametros: imagenes, freq, x, y
            imagenes: Lista de imagenes
            freq: Frecuencia del sprite
            x: posicion en x donde se graficará el sprite
            y: posicion en y donde se graficará el sprite

        Sirve para:
            Mostrar en pantalla todas las animaciones del personaje.
        
        Retorna: No retora nada.

        '''
        frame = int(time.time() *freq) % len (imagenes)
        self.Ventana.Poner(imagenes [frame], (x,y))
    
    def movimiento(self, tecla, Cambio):
        '''
        Nombre de la funcion: movimiento2()

        Parametros: tecla, cambio.
                tecla: es la tecla que oprime el usuario para especificar la direccion del movimiento del tanque 2.
                cambio: es una palabra vacia que posteriormente se convierte en una orientacion(arriba, abajo, derecha o izquierda).

        Sirve para:
            Su finalidad es cambiar la velocidad del tanque 2 en un eje en especifico con el fin de posteriormente cambiar la orientacion del
            tanque en su movimiento.


        Retorna: Retorna la variable Cambio.

        Ejemplo de llamado de funcion:
            Cambio2 = Tanque2.movimiento2(tecla2, Rotar)
        '''
        
        if tecla[py.K_UP]:
            if not self.Subio:
                self.VelY=-15
            else: 
                pass
            self.Subio=True
            Cambio = "Arriba"

        if tecla[py.K_LEFT]:
            self.VelX = -13
            Cambio = "Izquierda"
           
        if tecla[py.K_RIGHT]:
            self.VelX = 13
            Cambio = "Derecha"   
           
        
        return Cambio
    
    def elementos(self, Objeto, X, Y, VelF):
        '''
        Objeto, X, Y, VelF
        
        Nombre de la funcion:elementos 

        Parametros: Objeto, X, Y, VelF
            Objeto: Objeto a graficar
            X: Posicion en x donde se va a graficar
            Y: Posicion en Y donde se va a graficar
            VelF: Velocidad con la que se mueve la pantalla

        Sirve para:
            Sirve para colocar en pantalla los elementos(imagenes) que sirven como obstaculos y otros.        

        Retorna: Retorna un rectangulo con las mismas dimenciones del objeto inicial y en una posicion en concreto
        Es de gran facilidad para las colisiones.
      
        '''
        Objt = Objeto.get_rect()
        Objt.x, Objt.y = X, Y
        Objt.move_ip(VelF, 0)
        #py.draw.rect(Ventana1, (255,255,255), Objt)

        return Objt
    
    def colicion(self, Objeto, Jugador, ValidadorPos):
        '''
        Nombre de la funcion: colision

        Parametros: Objeto, Jugador, ValidadorPos.
            Objeto: Objeto con el cual va a colicionar
            Jugador: Es la caja que encierra al jugador para validar su colision
            ValidadorPos: Toma en cuenta si el personaje se desplaza a la derecha o izquierda

        Sirve para:
            Detectar las coliciones con los obstaculos.             

        Retorna: No retorna nada
        '''

        Jugador.x, Jugador.y = self.CoorX + ValidadorPos, self.CoorY 
        
        if Jugador.colliderect(Objeto) :
            if self.VelX > 0 and self.CoorY + 85 > Objeto.y:
                self.CoorX -= 35
            if self.VelX <0 and self.CoorY + 85 > Objeto.y:
                self.CoorX += 35
            if self.VelY>=0 and self.CoorY + 75 <= Objeto.y :
                self.VelY=0
                self.Ocolision = Objeto
                self.Act=True
                self.CoorY = Objeto.y - 85

                   
    def colimorir(self, Objeto, Jugador, Coor, ValidadorPos, nv):
        '''
        Nombre de la funcion: colimorir

        Parametros: Objeto, Jugador, Coor, ValidadorPos.  nv
            Objeto: Objeto con el cual va a colicionar
            Jugador: Es la caja que encierra al jugador para validar su colision
            ValidadorPos: Toma en cuenta si el personaje se desplaza a la derecha o izquierda
            Coor: Coordenada donde quiere que caiga el muñeco.
            nv: numero de vidas. 

        Sirve para:
            Detectar las coliciones con los obstaculos que son peligrosos o obstaculos trampa        

        Retorna: retorna el numero de vidas menos uno en caso de colicion 

        ''' 
        Jugador.x, Jugador.y = self.CoorX + ValidadorPos, self.CoorY   
        
        if Jugador.colliderect(Objeto):
            numero=int(nv)
            numero-=1
            Jugador.x=Coor[0]
            Jugador.y=Coor[1]
            self.CoorX=Coor[0] 
            self.CoorY=Coor[1]
            return numero

    def colibala(self, Jugador, Objeto):
        '''
        Nombre de la funcion: colibala

        Parametros: Jugador, Objeto
            Objeto: Se verifica si coliciono con una bala o bola de fuego. 
            Jugador: Es la caja que encierra al jugador para validar su colision

        Sirve para:
            Detectar la colicion con la bola de fuego      

        Retorna: no retorna nada

        '''
        if Jugador.colliderect(Objeto):
            self.Try=True
    
    def colivida(self, Jugador, Objeto):
        '''
        Nombre de la funcion: colivida

        Parametros: Jugador, Objeto
            Objeto: Objeto que contiene una vida.
            Jugador: Es la caja que encierra al jugador para validar su colision

        Sirve para:
            Detectar la colicion del objeto que regala una vida. 

        Retorna: True en caso de colision, False, en el caso contrario.
        Si colisiona con ello el objeto no volverá a aparecer en el juego. 

        '''
        if Jugador.colliderect(Objeto):
            return True

    def ColisionGanar(self,Jugador,Objeto):
        '''
        Nombre de la funcion: ColisionGanar

        Parametros: Jugador, Objeto
            Objeto: Es el personaje femenino que aparece al final del juego.
            Jugador: Es la caja que encierra al jugador para validar su colision

        Sirve para:
            Detectar la colicion del personaje con el personaje femenino, así se valida que el juego a terminado. 

        Retorna: True en caso de colision, False, en el caso contrario.
        

        '''
        if Jugador.colliderect(Objeto):
            return True