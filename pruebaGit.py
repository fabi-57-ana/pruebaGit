#******************************************************************************************
#*********************** Aplicaciones de escritorio con ***********************************
#******************************************************************************************
#********************************* Tkinter ************************************************
#******************************************************************************************
#******************************************************************************************
#******************************************************************************************


# Desarrollo de aplicaciones graficas 

# - Desarrollar aplicaciones de escritorio empleando ventanas y controles tales como cajas 
# de texto, etiquetas, botones, listas desplegables, checkbox, menus, etc. en Python
# - Tkinter es un modulo Python que nos facilita el desarrollo de las GUI, esta disponible
# en la instalacion por defecto, soporta diversas plataformas como: Windows, Linux, Mac, 
# y ademas es muy facil de usar 

# PRIMER PROGRAMA
# """"""""
from tkinter import Tk, Label, Button

def mensaje():
    print("Mensaje del boton")

ventana = Tk()
ventana.geometry("400x280")
ventana.title("Primera ventana con Python")

lbl = Label(ventana, text='Este es un [Label] tkinter')
lbl.pack()

btn = Button(ventana, text='Presiona este [Button] para mensaje', command=mensaje)
btn.pack()

ventana.mainloop() 
# """"""""

# EXPLICACION PRIMER PROGRAMA
# - desde la libreria tkinter importamos tres clases, Tk, Label y Button, 
# - tenemos un metodo del mensaje
# - ventana = Tk(), es una clase, creamos el objeto ventana a partir de la clase 
# Tk() y aqui se ejecuta su constructor
# - una vez que tenemos el objeto ventana con el metodo geometry indicamos que 
# queremos que sea una ventana de 400 x 280 el tamaño
# - ventana.title, con esto indicamos el titulo de la ventana
# ventana = Tk()
# ventana.geometry("400x280")
# ventana.title("Primera ventana con Python")
# - estos tres renglones de arriba es la ventana en si, solo falta el ultimo renglon, # ventana = Tk(),
# en donde se corre el ciclo principal de la ventana
# - en esta ventana estamos agregando dos objetos, un Label y un Button 
# - creamos el objeto lbl a partir de la clase Label y alli ejecutamos el constructor y como primer
# parametro le pasamos el contenedor, este Label va a estar contenido dentro de nuestra ventana y 
# como titulo va a tener "Este es un Label"
# - el metodo pack() lo llamamos para indicar que Label se posicione en la ventana, si no lo llamamos
# no se posicionaria aunque crearamos el Label no aparece 
# - creamos el objeto btn de la clase Button e invocamos a su constructor, (ventana, text='Presiona 
# este [Button] para mensaje', command=mensaje), ventana, el primer parametro es su contenedor
# tambien que es la ventana, este boton va a estar contenido en la ventana y como texto dice
# text='Presiona este [Button] para mensaje' y en la propiedad command le indicamos al boton que 
# cuando se de click en el boton se ejecuta el evento command, entonces se va a ejecutar el metodo 
# o la funcion mensaje, esta funcion mensaje la tenemos arriba en el segundo renglon,
# def mensaje():
#     print("Mensaje del boton")
# esta funcion lo que hace unicamente con un print imprime mensaje del boton, entonces este boton
# ya tiene asociado un evento cuando le demos click va a mandar ese mensaje
# btn.pack() lo que hace es posicionar el boton dentro de la ventana 
#------------------------------------------------------------------------------

# Clase Tk y algunos metodos

# - Tk() clase para crear una ventana principal donde añadir los widgets
# - pack() ubica los widgets en una posicion que podemos cambiar a traves de los correspondientes 
# atributos.
# - mainloop() | main - principal | loop - bucle
# inicia un bucle de mansajes, aqui se monitorea la interaccion del usuario a traves del
# raton o el teclado con la aplicacion, cuando se produzca un evento recibiremos la notificacion 
# correspondiente y podremos responder a dicho evento, por ejemplo: el usuario hace click sobre el 
# boton cerrar, respondemos cerrando la aplicacion.


# Configurar widgets tkinter

# Los widgets tienen configuraciones y una de ellas es el text, la propiedad text es un valor que 
# nosotros le estamos indicando al Label o al Button que es un texto que ellos estan presentando
# esas propiedades son configuraciones y existen tres formas de configurar los widgets en tkinter

# 3 formas 

# - Costructor: 
#    - miBoton = Button(self, fg="red", bg="blue")

# - Metodo config:
#    - miBoton.config(fg="red", bg="blue")

# - Accesando a la propiedad(como un dicccionario clave/valor)
#    - miBoton["fg"]="red"
#    - miBoton["bg"]="blue"


from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("400x280")
lbl = Label(ventana, text="Este es un Label")
lbl.config(bg = "gray")
lbl.pack()
btn = Button(ventana, text="Presionar", command=miFuncion)
# btn = Button(ventana, text="Presionar", bg = "yellow",  fg = "blue" ,command=miFuncion)
# btn.configure( bg = "yellow",  fg = "blue")
btn["fg"]="red"
btn["bg"]="yellow"
btn.pack()

ventana.mainloop()