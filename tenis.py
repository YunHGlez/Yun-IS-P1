# Qué necesitamos?
"""
- tenemos puntos por juego
    15 30 40 gana juego
    si ambos llegan a 40 gana el q gane dos juegos seguidos

- 6 juegos hacen un set

"""
class Marcador:
    j1 = ""
    j2 = ""
    pj1 = 0
    pj2 = 0
    setj1 = 0
    setj2 = 0
    juegosj1 = 0
    juegosj2 = 0
    cambioCancha = 0
    arrPuntos = ["0", "15", "30", "40", "ad","gana juego"]
    arr = [1,3,5,7]
    """
    
    """
    def __str__(self):
        buff1 = self.pj1
        buff2 = self.pj2
        st = f"MARCADOR \n{self.j1} puntos: {self.arrPuntos[buff1]} | juegos ganados {self.juegosj1} | sets ganados {self.setj1}\n"
        st += f"{self.j2} puntos: {self.arrPuntos[buff2]}  | juegos ganados {self.juegosj2} | sets ganados {self.setj2}\n"
        return st
    """
    {self.arrPuntos[buff2]}
    :param j1: nombre del jugador 1.
    :param j2: nombre del jugador 2.
    """
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2

    def ganaJuego(self, a, b):
        
        if a == 4 and (b == 2 or b == 1 or b == 0) :
            self.juegosj1 += 1
            self.reiniciaPuntos()
        elif (a == 2 or a == 1 or a == 0) and b == 4:
            self.juegosj2 += 1
            self.reiniciaPuntos()
        elif a == 4 and b == 6:
            self.juegosj1 += 1
            self.reiniciaPuntos()
        elif a == 6 and b == 4:
            self.juegosj2 += 1
            self.reiniciaPuntos()
        # D E U C E
        elif a == 4 and b == 4:
            self.pj1 -= 1
            self.pj2 -= 1
        elif a == 3 and b == 5:
            self.juegosj2 += 1
            self.reiniciaPuntos()
        elif a == 5 and b == 3:
            self.juegosj1 += 1
            self.reiniciaPuntos()

    def ganaSet(self, a, b):

        if a == 6 and (b ==4 or b == 3 or b == 2 or b == 1 or b == 0) :
            self.setj1 += 1
            self.reiniciaPuntosSet()
        elif b == 6 and (b ==4 or a == 3 or a == 2 or a == 1 or a == 0):
            self.setj2 += 1
            self.reiniciaPuntosSet()
        elif a == 5 and b == 7:
            self.setj1 += 1
            self.reiniciaPuntosSet()
        elif a == 7 and b == 5:
            self.setj1 += 1
            self.reiniciaPuntosSet()
        # P U N T O DE V E N T A J A
        elif a == 6 and b == 6:
            self.juegosj1 -= 1
            self.juegosj2 -= 1
            print("punto de ventaja")
        elif a == 4 and b == 6:
            self.setj2 += 1
            self.reiniciaPuntosSet()
        elif a == 6 and b == 4:
            self.setj1 += 1
            self.reiniciaPuntosSet()

        #Caso para comprobar si alguno gano el juego
        if self.setj1 == 2:
            print(f"***********{self.j1} ha ganado el partido!***********")
            exit()

        elif self.setj2 == 2:
            print(f"***********{self.j2} ha ganado el partido!***********")
            exit()
    
    def cambioDeCancha(self):
        if self.cambioCancha in self.arr:
            print("\n----Cambio de cancha----\n")

    def reiniciaPuntos(self):
        self.pj1 = 0
        self.pj2 = 0
        self.cambioCancha += 1
        self.cambioDeCancha()
        self.ganaSet(self.juegosj1, self.juegosj2)
    
    def reiniciaPuntosSet(self):
        self.juegosj1 = 0
        self.juegosj2 = 0
        self.cambioCancha = 0

    def aPuntoj1(self):
        self.pj1 += 1
        self.ganaJuego(self.pj1, self.pj2)

    def aPuntoj2(self):
        self.pj2 += 1
        self.ganaJuego(self.pj1, self.pj2)

    def menu(self):
        print(f"[1] {self.j1} anota punto.")
        print(f"[2] {self.j2} anota punto ")
        

def pideNombres():
    print("Iniciando marcador:")
    a = str(input("Ingresa el nombre del primer jugador: "))
    b = str(input("Ingresa el nombre del segundo jugador: "))
    nameLs = [a, b]
    return nameLs

def iniciaMarcador():
    arr = pideNombres()
    j1 = arr[0]
    j2 = arr[1]
    marca = Marcador(j1, j2)
    print("Iniciando juego...")
    while True:
        marca.menu()
        print(str(marca))
        try:
            a = int(input("Ingresa una opción:"))
        except:
            print("Ingresa una opción válida.")
        if a == 1:
            marca.aPuntoj1()
        elif a == 2:
            marca.aPuntoj2()
        elif a == 3:
            print("saliendo")
            break
        else: 
            print("Esa no es una opción válida")
        
    

iniciaMarcador()



    
        





