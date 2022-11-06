
#EJERCICIO 1 

 

class Alumno:
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
    print("El alumno se ha creado con éxito\n")
    print("Nombre: ", self.nombre)
    print("Nota: ", self.nota)
  
  def calificacion(self):
    if self.nota>=5:
      print(self.nombre, "ha aprobado")
    else:
      print(self.nombre, "ha suspendido")



alumno1=Alumno("Rodrigo", 5)
alumno1.calificacion()

print("\n\n")

#Experimentamos con algunos alumnos
Guillermo = Alumno("Guillermo", 7)
Guillermo.calificacion()

Diego = Alumno("Diego", 5)
Diego.calificacion()

Antonio = Alumno("Antonio", 2)
Antonio.calificacion()

if __name__ == "__main__":
    main()

#EJERCICIO2
class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
    
  def __str__(self):
    return "{} ha sacado un {} en el exámen".format(self.nombre,self.nota)
    
  def calificacion(self):
    if self.nota < 5:
      print(f"{self.nombre} ha suspendido")
    else:
      print(f"{self.nombre} ha aprobado")
      
if __name__ == "__main__":
  Alumno1 = Alumno("Rodrigo",4)
  print(Alumno1)
  Alumno1.calificacion()
  Alumno2 = Alumno("Ivan",8)
  print(Alumno2)
  Alumno2.calificacion()

#EJERCIO3

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


