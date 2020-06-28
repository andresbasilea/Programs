

from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

class Bot_Dinosuario:
    def __init__(self):
        self.coordenadasReinicio = (410,338) # Coordenadas boton reinicio
        self.coordenadasDinosaurio = (262,358) #Coordenadas de dinosaurio
        # agachado (tomadas en la parte de hasta la derecha de la cabeza
        self.area = (self.coordenadasDinosaurio[0]+120, self.coordenadasDinosaurio[1]+90, self.coordenadasDinosaurio[0] + 150, self.coordenadasDinosaurio[1]+95)
        # Los + n fueron agregados para que tomara el area correcta. Cuando no los
        # agregaba tomaba captura de un area diferente a la deseada... checar
    """def definirCoordenadasDino(self,x,y):
        self.coordenadasDinosaurio = (x,y)

    def definirCoordenadasReinicio(self,x,y):
        self.coordenadasReinicio = (x,y)
    """
    def reiniciar(self):
        pyautogui.click(self.coordenadasReinicio)
        pyautogui.keyDown('down')

    def brincar(self):
        pyautogui.keyUp('down')
        pyautogui.keyDown('space')
        time.sleep(0.075)
        pyautogui.keyUp('space')
        pyautogui.keyDown('down')

    def areaDeteccion(self):
        imagen = ImageGrab.grab(self.area)
        #arregloColor = np.array(imagen)
        imagen_bn = ImageOps.grayscale(imagen)
        arreglo = np.array(imagen_bn.getcolors())
        #imagen.show()
        #print(arregloColor)
        #print(arreglo)
        #print(arreglo.mean())
        return arreglo.mean()

    """def estaMuerto(self):
        estaMuerto = False
        t = self.areaDeteccion()
        time.sleep(5)
        tf = self.areaDeteccion()
        if t == tf:
            estaMuerto = True
        return estaMuerto
    """
    def main(self):
        self.reiniciar()
        while True:
            if(self.areaDeteccion() != 198.5):
                self.brincar()
            """if self.estaMuerto() == True:
                self.main()
            """

bot = Bot_Dinosuario()
bot.main()
