#FINAL
#Computacion grafica
#2022
'''ELABORADO POR:
        ALICIA VALENCIA ACEVEDO
        RONALD MARIN CARDONA'''
#-----------------------------------------
from Ventana import *
from time import sleep
from Personaje import *
#-----------------------------------------
def Juego():
    '''

    Nombre de la funcion:  Juego

            Parametros: Ninguno

            Sirve para: Contiene el dibujo de imagenes y el while que permite que el juego 
            permanezca en uso         

            Retorna:
            No retorna nada
    '''

    '''IMAGENES'''
    Img=py.image.load("flatboy\Fondo\Fondo2.png") 
    Plt1=py.image.load("flatboy\Obstaculos\Plataforma2.png")
    Plt2=py.image.load("flatboy\Obstaculos\Plataforma.png")
    Portal=py.image.load("flatboy\Obstaculos\Portal.png")
    Ramas=py.image.load("flatboy\Obstaculos\\tree22.png")
    Balas=py.image.load("flatboy\Obstaculos\Balas.png")
    Plt4=py.image.load("flatboy\Obstaculos\Puentesito.png")
    Gameover=py.image.load("flatboy\Obstaculos\GameOver.png")
    Bala=py.image.load("flatboy\Obstaculos\\bala.png")
    LAX=py.image.load("flatboy\Obstaculos\\X.png")
    IRecordar=py.image.load("Recordar.png")
    IVida=py.image.load("flatboy\Obstaculos\\Vida.png")
    ITiempo=py.image.load("flatboy\Fondo\\Tiempo.png")
    IPasto=py.image.load("flatboy\Obstaculos\\Pasto.png")
    Plt5=py.image.load("flatboy\Obstaculos\\P0.png")
    Plt6=py.image.load("flatboy\Obstaculos\\P1.png")
    Plt7=py.image.load("flatboy\Obstaculos\\P2.png")
    Plt8=py.image.load("flatboy\Obstaculos\\P3.png")
    Plt9=py.image.load("flatboy\Obstaculos\\P4.png")
    Portal2=py.image.load("flatboy\Obstaculos\\Portal2.png")
    Muchacha=py.image.load("flatboy\Obstaculos\\Niña.png")
    IGano=py.image.load("flatboy\Fondo\Fin.png")
    #-------------------------------------------------------
    '''Inicio de ventana y valores iniciales'''
    VentanaJ=VentanaP((900,506),Img)
    x,VelF,Actual,nv=0,0,0,3
    W=900
    Yincial=-224
    Reloj=py.time.Clock()
    Ventana1=VentanaJ.Iniciar(-224)
    nuevavida=nv
    BalasenPantalla=[]
    fuente=py.font.SysFont("Consolas",20)

    #Variables del sprite.

    personaje = Sprites(VentanaJ, 'flatboy',614,564,100, 0, 0, 10, 362)  #Se cargan los elementos del sprite
    VentanaJ.Poner(IRecordar,(140,50)) #Se coloca en pantalla el recordatorio del tiempo
    py.display.flip()
    sleep(1.3)
    jugador = py.draw.rect(Ventana1, (255,255,255), (personaje.CoorX, personaje.CoorY,50,95), 1)
    ValorRotacion1 = False #Personaje mirando a la derecha
    ValorRotacion2 = False # Personaje mirando a la derecha.
    Cambio = "Quieto" # Movimiento  que se selecciona: derecha, izquierda, arriba.
    TeclaAnterior = "Quieto" # Movimiento anterior realizado
    ValidadorPos = 0 

    AVida=[]

    #Variable del bucle
    Iniciar=True
    salto = 12 #Valor del salto

    # Musica de fondo
    py.mixer.init()
    Sonido= py.mixer.Sound("Musica\Musica.mp3")
    Sonido.set_volume(0.3)
    Sonido.play() 
    
    while Iniciar:
        #Se inicia el juego
        Tiempo= py.time.get_ticks()/60000

        if nv==-1 or Tiempo>2:
            #Para perder el jugador deberá perder las tres vidas o superar los dos minutos de juego.
            VentanaJ.Poner(Gameover,(325,150))
            py.display.flip()
            sleep(2)
            py.quit()
            Iniciar=False
            return 1
        Vida=py.image.load("flatboy\Vidas"+f"\{nv}"+"vidas.png")
        for event in py.event.get():
            if event.type == py.QUIT:
                Iniciar=False
                Sonido.stop()
                py.quit()
                return 1
            if event.type == py.KEYDOWN:
                #Se espera que el usuario presione una tecla para así realizar los movimientos
                tecla=py.key.get_pressed()
                Cambio = personaje.movimiento(tecla, "")
                if personaje.Subio:
                    #Actua como el movimiento parabolico del salto, y ayuda a que el personaje caiga.
                    if salto>=12:
                        personaje.CoorY -= (salto * abs(salto)) * 0.5
                        salto-=1
                        personaje.VelY=salto
                    else:
                        personaje.Subio=False
                        salto=12
                x -= 12
            else:
                Cambio = "Quieto"   

            if event.type==py.KEYUP:
                if event.key == py.K_LEFT:
                    personaje.VelX = 0
                if event.key == py.K_RIGHT:
                    personaje.VelX = 0  
                
                x= 0

        personaje.Ocolision.x -= personaje.VelX
        
        #Se valida a que direccion se dirige el personaje para cargar las animaciones
        if Cambio == "Quieto":
            Imagenes = personaje.cargar_animacion('Idle', ValorRotacion1, ValorRotacion2,Actual)

        elif Cambio == "Derecha":
            ValorRotacion1 = False
            
            Imagenes = personaje.cargar_animacion('Walk', ValorRotacion1, ValorRotacion2,Actual)
            Actual=0
            ValidadorPos = 0

        elif Cambio == "Izquierda":
            ValorRotacion1 = True
            ValorRotacion2 = False
            ValidadorPos = 50
            
            Imagenes = personaje.cargar_animacion('Walk', ValorRotacion1, ValorRotacion2,Actual)
            Actual=1
      
        elif Cambio == "Arriba":
            Imagenes = personaje.cargar_animacion('Jump', ValorRotacion1, ValorRotacion2,Actual)

        #Se toma en cuenta las teclas anteriormente presionadas para así coniderar el movimiento de la pantalla
        if TeclaAnterior=='Derecha':
            VelF+=x
        elif TeclaAnterior=='Izquierda':
            VelF-=x

        ''' Se validan los bordes para que el personaje no los supere '''
        if personaje.CoorY > 362:
            personaje.CoorY = 362
        if personaje.CoorX < 20:
            personaje.CoorX = 20
        if personaje.CoorX > 506:
            personaje.CoorX = 506

        P1Forma= py.draw.rect(Ventana1,(255,255,255),(personaje.CoorX+8,personaje.CoorY+18,32,63))   #Forma que va encima del personaje

        '''Movimiento de fondo'''

        x_relativo= VelF % Img.get_rect().width
        VentanaJ.Poner(Img,(x_relativo - Img.get_rect().width,Yincial))
        if x_relativo < W:
            VentanaJ.Poner(Img,(x_relativo,Yincial))  
    
        if nuevavida!=None:
            nv=nuevavida

        '''Elementos de pantalla detras del personaje'''

        VentanaJ.Poner(Vida,(10,10))
        if AVida==[]:
            #Condicional para reconocer la vida de regalo.
            VentanaJ.Poner(LAX,(2265+VelF,433))
            elemento=personaje.elementos(LAX,2267,453,VelF)
            SumaVida=personaje.colivida(jugador,elemento)

        #Elementos trampa

        VentanaJ.Poner(IPasto,(2565+VelF,433)) #Se pone en pantalla el objeto
        CPasto=personaje.elementos(IPasto,2565,453,VelF) #Crea los recuadros del elemento
        r=personaje.colimorir(CPasto,jugador,[56,120],ValidadorPos,nv) #Valida su colicion

        VentanaJ.Poner(IPasto,(3295+VelF,433))
        elemento = personaje.elementos(IPasto, 3295,453, VelF) #Crea los recuadros del elemento
        m=personaje.colimorir(elemento,jugador,[56,120],ValidadorPos,nv)#Valida su colicion

        VentanaJ.Poner(IPasto,(3555+VelF,433))
        elemento = personaje.elementos(IPasto, 3555,453, VelF) #Crea los recuadros del elemento
        n=personaje.colimorir(elemento,jugador,[56,120],ValidadorPos,nv)#Valida su colicion

        VentanaJ.Poner(Plt2,(4640+VelF,220))
        elemento = personaje.elementos(Plt2, 4640,223, VelF) #Crea los recuadros del elemento
        personaje.colicion(elemento, jugador, ValidadorPos)#Valida su colicion

        VentanaJ.Poner(Plt2,(4690+VelF,220))
        elemento = personaje.elementos(Plt2, 4690,223, VelF) #Crea los recuadros del elemento
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Portal,(4640+VelF,50))

        #Se valida si las colisiones anteriores han sucedido.
        if r!=None: 
            nv=r
        if m!=None:
            nv=m
        if n!=None:
            nv=n

        '''Mostrar el personaje en pantalla'''
        personaje.mostrar_animacion(Imagenes, 15, personaje.CoorX, personaje.CoorY)
        
        '''Caida de las balas'''
        if personaje.Try:
            if BalasenPantalla==[]:
                for i in range(0,800,100):
                    VentanaJ.Poner(Bala,(100+i,10))
                    Objeto=personaje.elementos(Bala, 100+i, 10,0)
                    BalasenPantalla.append(Objeto)

            for i in BalasenPantalla:
                i.move_ip(1, 20) #Desplaza los elementos en X y Y de forma constante
                VentanaJ.Poner(Bala,(i.x,i.y))
                nuevavida=personaje.colimorir(i,jugador, [56,120], ValidadorPos,nv) #Valida si ha colisionado con el personaje
                
                if i.y>506:
                    personaje.Try=False
                    BalasenPantalla=[]
                if nuevavida!=None:
                    nv=nuevavida  #Le asigna el nuevo valor de la vida. 

        '''Elementos en la pantalla'''
        
        VentanaJ.Poner(Plt2,(300+VelF,430))
        elemento = personaje.elementos(Plt2, 300,432, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
        
        VentanaJ.Poner(Plt2,(430+VelF,400))
        elemento = personaje.elementos(Plt2, 430,402, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(540+VelF,370))
        elemento = personaje.elementos(Plt2, 540,372, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(650+VelF,340))
        elemento = personaje.elementos(Plt2, 650,342, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(760+VelF,310))
        elemento = personaje.elementos(Plt2, 760,312, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
        
        VentanaJ.Poner(Ramas,(820+VelF,400))
        elemento = personaje.elementos(Ramas, 820,402, VelF) #Crea los recuadros
        nuevavida=personaje.colimorir(elemento, jugador, [56,120], ValidadorPos,nv)

        VentanaJ.Poner(Balas,(1030+VelF,210))
        elemento = personaje.elementos(Balas, 1030,210, VelF) #Crea los recuadros
        personaje.colibala(jugador, elemento)

        VentanaJ.Poner(Plt1,(998+VelF,362))
        elemento = personaje.elementos(Plt1, 998,366, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
      
        VentanaJ.Poner(Plt1,(1275+VelF,415))
        elemento = personaje.elementos(Plt1, 1275,420, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
        
        VentanaJ.Poner(Plt1,(1390+VelF,380))
        elemento = personaje.elementos(Plt1, 1390,385, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt1,(1505+VelF,340))
        elemento = personaje.elementos(Plt1, 1505,345, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt1,(1620+VelF,300))
        elemento = personaje.elementos(Plt1, 1620,305, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos )

        VentanaJ.Poner(Plt4,(1755+VelF,270))
        elemento = personaje.elementos(Plt4, 1755,272, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt5,(2795+VelF,407))
        elemento = personaje.elementos(Plt5, 2795,414, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
        
        VentanaJ.Poner(Plt6,(2895+VelF,391))
        elemento = personaje.elementos(Plt6, 2895,395, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt7,(2995+VelF,347))
        elemento = personaje.elementos(Plt7, 2995,351, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt8,(3095+VelF,295))
        elemento = personaje.elementos(Plt8, 3095,299, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt9,(3195+VelF,250))
        elemento = personaje.elementos(Plt9, 3195,254, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt1,(3295+VelF,250))
        elemento = personaje.elementos(Plt1, 3295,255, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Portal2,(3395+VelF,440))
        elemento = personaje.elementos(Portal2, 3395,450, VelF) #Crea los recuadros
        personaje.colimorir(elemento,jugador,[280,15],ValidadorPos,nv)

        VentanaJ.Poner(Plt1,(3555+VelF,250))
        elemento = personaje.elementos(Plt1, 3555,255, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
    
        VentanaJ.Poner(Plt2,(3700+VelF,430))
        elemento = personaje.elementos(Plt2, 3700,432, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)
        
        VentanaJ.Poner(Plt2,(3830+VelF,400))
        elemento = personaje.elementos(Plt2, 3830,402, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(3960+VelF,370))
        elemento = personaje.elementos(Plt2, 3960,372, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(4090+VelF,340))
        elemento = personaje.elementos(Plt2, 4090,344, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(4220+VelF,310))
        elemento = personaje.elementos(Plt2, 4220,313, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(4350+VelF,280))
        elemento = personaje.elementos(Plt2, 4350,283, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Plt2,(4480+VelF,250))
        elemento = personaje.elementos(Plt2, 4480,253, VelF) #Crea los recuadros
        personaje.colicion(elemento, jugador, ValidadorPos)

        VentanaJ.Poner(Muchacha,(4710+VelF,154))
        elemento = personaje.elementos(Muchacha, 4710,154, VelF) #Crea los recuadros
        Gano=personaje.ColisionGanar(jugador,elemento)

        #En caso de que el jugador colisione con la chica quiere decir que ha llegado al final

        if Gano!=None:
            VentanaJ.Poner(IGano,(12,12))
            Sonido.stop() #Se detiene la musica
            py.display.flip()
            sleep(2)
            Iniciar=False
            py.quit()
            return 1
            
        '''Condicional cae vida'''
        if SumaVida != None:
            if AVida==[]:
                VentanaJ.Poner(IVida,(2262+VelF,5))        
                elemento = personaje.elementos(IVida, 2262,5, VelF)
                AVida.append(elemento)
            else:
                AVida[0].move_ip(0,20)
                VentanaJ.Poner(IVida,(AVida[0].x,AVida[0].y))    
                personaje.colibala(AVida[0],jugador)
                if personaje.Try:
                    if nv<3:
                        nv+=1
                    personaje.Try=False
                    AVida[0].move_ip(0,300)
                    VentanaJ.Poner(IVida,(AVida[0].x,AVida[0].y))    
                
        '''Tiempo en pantalla'''       

        VentanaJ.Poner(ITiempo,(680,15))
        texto= fuente.render(str("{:.4f}".format(Tiempo)),1,(255,255,255))
        VentanaJ.Poner(texto,(815,20))

        #Se desplaza el personaje.

        personaje.CoorX += personaje.VelX
        personaje.CoorY += personaje.VelY

        # Ancho y alto del objeto colisionado
        TeclaAnterior = Cambio
        nueva=personaje.Ocolision.x
        ancho=personaje.Ocolision.width


        Elemento=py.Rect(1320+VelF,445,320,5)
        personaje.colimorir(Elemento,jugador,[56,120],ValidadorPos,nv)

        Elemento=py.Rect(2840+VelF,445,570,5)
        personaje.colimorir(Elemento,jugador,[56,120],ValidadorPos,nv)
        
        Elemento=py.Rect(3797+VelF,445,1000,5)
        personaje.colimorir(Elemento,jugador,[56,120],ValidadorPos,nv)

        ''' Se valida las caidas de las escaleras o bloques , asignando así el incremento en Y
            Para un mejor efecto de gravedad'''
        if personaje.Act:
            if jugador.x>=nueva-32 and jugador.x<=nueva+ancho-20:
                pass
            else:
                jugador.y+=15
                personaje.CoorY+=15

        Reloj.tick(80)
        py.display.flip()
    py.quit()
