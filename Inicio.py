from tkinter import *

ventana = Tk()

ventana.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaño

ventana.title('PsicoPinball')#titulo de la ventana

c = Canvas(ventana, width=1000, height=800, bg='white') #medidas de la ventana
c.pack()

################ FONDO ###############

fondoinicio = PhotoImage(file = 'fondoinicio.gif')
c.create_image(0,0, image = fondoinicio, anchor = NW)

logoinicio = PhotoImage(file = 'Logoinicio.gif')
c.create_image(300,60, image = logoinicio, anchor = NW)

tomateinicio = PhotoImage(file = 'Tomateinicio.gif')
c.create_image(120,500, image = tomateinicio, anchor = NW)



############ BOTONES ###############

nombre = Label(ventana,text="Digite su Nombre de Usuario : ", bg = "gray", font = ("Arial Rounded MT Bold", 15)). place(x = 200, y = 550)
cuadro = StringVar()
Usuario = Entry(ventana,textvariable = cuadro, bg = "gray", font = ("Arial Rounded MT Bold", 15)). place(x = 550, y = 550)

cargar = Button(c,text="Cargar Partida", bg = "gray", font = ("Arial Rounded MT Bold", 15)). place(x = 250, y = 650)

entrar = Button(c,text="Entrar", bg = "gray", font = ("Snap ITC", 25)). place(x = 600, y = 650)


