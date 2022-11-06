class Producto():       #Creamos la clase Producto
    def __init__(self,codigo,nombre,precio,tipo):   
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("El producto ha sido creado con éxito")   
    
    def __str__(self):      
        return "Código: {}\nNombre: {}\nPrecio: {}\nTipo: {}".format(self.codigo,self.nombre,self.precio,self.tipo)


prod1=Producto("29","Bate de beisbol","35€","Bate")  
print(prod1)
prod2=Producto("7","Bomber","89€","Abrigo")
print(prod2)
prod3=Producto("31","Vapormax","15€","Zapatillas")
print(prod3)
