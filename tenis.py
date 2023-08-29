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
    setCount = 0
    setj1 = 0
    setj2 = 0
    arrPuntos = ["0", "15", "30", "40", "ad","gana juego"]
    arr = [[0, 0, 0],[0, 0, 0]]
    """
    
    """
    def __str__(self):
        buff1 = self.pj1
        buff2 = self.pj2
        st = f"MARCADOR \n{self.j1} puntos: {self.arrPuntos[buff1]} r: {self.pj1}\n"
        st += f"{self.j2} puntos: {self.arrPuntos[buff2]} r: {self.pj2}\n"
        st += f"set j1 {self.setj1} | set j2 {self.setj2}"
        #st += f"J1 Set 1:  {self.set1j1} Set 2:  {self.set2j1} Set 3:  {self.set3j1} \n"
        #st += f"J2 Set 1:  {self.set1j2} Set 2:  {self.set2j2} Set 3:  {self.set3j2} \n"
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
            self.setj1 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()
        elif (a == 2 or a == 1 or a == 0) and b == 4:
            self.setj2 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()
        elif a == 4 and b == 6:
            self.setj1 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()
        elif a == 6 and b == 4:
            self.setj2 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()
        # D E U C E
        elif a == 4 and b == 4:
            self.pj1 -= 1
            self.pj2 -= 1
        elif a == 3 and b == 5:
            self.setj2 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()
        elif a == 5 and b == 3:
            self.setj1 =+ 1
            self.ganaJuego(self.setj1, self.setj2)
            self.reiniciaPuntos()

    def ganaSet(self, a, b):
        if a == 5 and (b == 3 or b == 2 or b == 1 or b == 0) :
            self.set1j1 =+ 1
        elif b == 5 and (a == 3 or a == 2 or a == 1 or a == 0):
            self.set1j2 =+ 1
            self.reiniciaPuntosSet()
        elif a == 5 and b == 7:
            self.set1j1 =+ 1
            self.reiniciaPuntosSet()
        elif a == 7 and b == 5:
            self.set1j2 =+ 1
            self.reiniciaPuntosSet()
        # P U N T O DE V E N T A J A
        elif a == 6 and b == 6:
            self.pj1 -= 1
            self.pj2 -= 1
        elif a == 4 and b == 6:
            self.set1j2 =+ 1
            self.reiniciaPuntosSet()
        elif a == 6 and b == 4:
            self.set1j1 =+ 1
            self.reiniciaPuntosSet()
        if self.setj1 == 2:
            print(f"{self.j1} ha ganado el partido!")
        if self.setj2 == 2:
            print(f"{self.j2} ha ganado el partido!")
    
    def impGanaJuego(self, a):
        print(f'{a} gana el juego!')

    def reiniciaPuntos(self):
        self.pj1 = 0
        self.pj2 = 0


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



    
        





