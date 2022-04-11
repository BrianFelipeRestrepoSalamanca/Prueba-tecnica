class cuenta():
    titular = ""
    cantidad = 0
    #no recuerdo muy bien los getters y setters 
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    def mostrar(self):
        print("El nombre del titular es: "+ self.titular)
        print("La cantidad que hay es: "+ str(self.cantidad))
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print("----------------------------------")
            print("El usuario " + self.titular + " ingreso " + str(cantidad)+ "\n Nuevo saldo es de: " + str(self.cantidad))
        else: 
            print("-------------------------------------")
            print("No ingresaste un valor adecuado")
    def retirar(self,cantidad):
        self.cantidad = self.cantidad - cantidad
        print("-------------------------------------")
        print("El usuario " + self.titular + " retiro " + str(cantidad)+ "\n Nuevo saldo es de: " + str(self.cantidad))
        if self.cantidad <0:
            print("Debes " + str(self.cantidad) +" a la cuenta")

objeto1= cuenta("Brian",300000)
objeto1.mostrar()
objeto1.ingresar(200000)
objeto1.retirar(1000000)