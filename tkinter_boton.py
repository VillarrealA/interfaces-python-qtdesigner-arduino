import tkinter as tk


def saludar():
    boton.config(text="¡Botón presionado!")


ventana = tk.Tk()
ventana.title("Mi primera interfaz")
ventana.geometry("360x160")
boton = tk.Button(ventana, text="Presionar", command=saludar)
boton.pack(padx=30, pady=45)
ventana.mainloop()
