from tkinter import *
import time

juego = Tk()

#juego.resizable(0,0) # Evita que la ventana se pueda cambiar de tamaño

juego.title('PsicoPinball')#titulo de la ventana

v = Canvas(juego, width=1000, height=800,) #medidas de la ventana
v.pack()

    ################ FONDO ###############

imfondo = PhotoImage(file = 'Fondo.gif')
v.create_image(0,0, image = imfondo, anchor = NW)

fondogris = PhotoImage(file = 'fondo gris.gif')
v.create_image(635,0, image = fondogris, anchor = NW)

logo = PhotoImage(file = 'Logo.gif')
v.create_image(730,40, image = logo, anchor = NW)

tomate = PhotoImage(file = 'Tomate.gif')
v.create_image(670,300, image = tomate, anchor = NW)


    ############# ELEMENTOS ################

linea1 = v.create_line(590, 150, 590, 800)
linea2 = v.create_line(635, 0, 635, 800)

bola = v.create_oval(600, 700, 625, 725, fill = "gray") # bola

triangulo1 = v.create_polygon((50, 750, 100, 650, 150, 750), fill="green")
triangulo2 = v.create_polygon((470, 750, 520, 650, 570, 750), fill="green")

pinza1 = v.create_rectangle(120, 710, 200, 700, outline='black', fill='gray') #pinza lado izquierdo
pinza2 = v.create_rectangle(420, 710, 500, 700, outline='black', fill='gray') #pinza lado derecho

obstaculo1 = v.create_oval(50, 100, 150, 200, fill = "brown") # obstaculo
obstaculo2 = v.create_oval(70, 125, 125, 175, fill = "orange") # obstaculo

triangulo3 = v.create_polygon((0, 0, 0, 50, 100, 0), outline='black', fill="red")
triangulo4 = v.create_polygon((635, 0, 635, 50, 585, 0), outline='black', fill="red")

obstaculo4 = v.create_oval(450, 275, 550, 385, fill = "gray") # obstaculo
obstaculo5 = v.create_oval(470, 300, 525, 360, fill = "red") # obstaculo

obstaculo6 = v.create_oval(50, 500, 150, 600, fill = "gray") # obstaculo
obstaculo7 = v.create_oval(70, 525, 125, 575, fill = "yellow") # obstaculo

obstaculo8 = v.create_rectangle(45, 275, 145, 385, outline='black', fill='blue') #cuadrado izquierdo sombra
obstaculo9 = v.create_rectangle(50, 280, 150, 390, outline='black', fill='gray') #cuadrado izquierdo 

obstaculo8 = v.create_rectangle(455, 95, 555, 195, outline='black', fill='gray') #cuadrado derecho1 sombra
obstaculo9 = v.create_rectangle(450, 100, 550, 200, outline='black', fill='red') #cuadrado derecho1

obstaculo10 = v.create_rectangle(455, 505, 555, 605, outline='black', fill='gray') #cuadrado derecho2 sombra
obstaculo11 = v.create_rectangle(450, 500, 550, 600, outline='black', fill='blue') #cuadrado derecho2

    ############ BOTONES ###############

guardar = Button(v,text="Guardar Partida", bg = "gray", font = ("Arial Rounded MT Bold", 15)). place(x = 750, y = 600)

    ############# MOVER #####################

for x in range (50):
    
    y = 1
    x = 0

    while (y > 0):

        time.sleep(0.05)
        v.move(bola, x, -y)
        v.update()
        y = y + 1

   

juego.mainloop()
