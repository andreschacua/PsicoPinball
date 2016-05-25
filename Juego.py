from tkinter import *
import time

juego = Tk()

#juego.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaño

juego.title('PsicoPinball')#titulo de la ventana

v = Canvas(juego, width=1000, height=800,) #medidas de la ventana
v.pack()

    ################ FONDO ###############

imfondo = PhotoImage(file = 'C:/Users/123456/Documents/Universidad/Programacion/Proyecto/Fondo.gif')
v.create_image(0,0, image = imfondo, anchor = NW)

fondogris = PhotoImage(file = 'C:/Users/123456/Documents/Universidad/Programacion/Proyecto/fondo gris.gif')
v.create_image(635,0, image = fondogris, anchor = NW)

logo = PhotoImage(file = 'C:/Users/123456/Documents/Universidad/Programacion/Proyecto/Logo.gif')
v.create_image(730,40, image = logo, anchor = NW)

tomate = PhotoImage(file = 'C:/Users/123456/Documents/Universidad/Programacion/Proyecto/Tomate.gif')
v.create_image(670,300, image = tomate, anchor = NW)


    ############# ELEMENTOS ################

linea1 = v.create_line(590, 150, 590, 800)
linea2 = v.create_line(635, 0, 635, 800)

bola = v.create_oval(600, 700, 625, 725, fill = "gray") # bola

triangulo1 = v.create_polygon((50, 750, 100, 650, 150, 750), fill="green")
triangulo2 = v.create_polygon((470, 750, 520, 650, 570, 750), fill="green")

pinza1 = v.create_rectangle(120, 710, 200, 700, outline='black', fill='gray') #pinza lado izquierdo
pinza2 = v.create_rectangle(420, 710, 500, 700, outline='black', fill='gray') #pinza lado derecho

obstaculo1 = v.create_oval(50, 100, 150, 200, fill = "brown") # bola
obstaculo2 = v.create_oval(70, 125, 125, 175, fill = "orange") # bola

triangulo3 = v.create_polygon((0, 0, 0, 50, 100, 0), outline='black', fill="red")
triangulo4 = v.create_polygon((600, 0, 600, 50, 700, 10), outline='black', fill="red")


    ############ BOTONES ###############

guardar = Button(v,text="Guradar Partida", bg = "gray", font = ("Arial Rounded MT Bold", 15)). place(x = 750, y = 600)

    ############# MOVER #####################

for x in range (50):

    y = 11
    x = 0

    time.sleep(0.025)
    v.move(bola, x, -y)
    v.update()



juego.mainloop()
