""" Aplicativo Para Guardar e Recuperar Documentos"""
import sys
from tkinter import *
import tkinter as tk
from  tkinter import PhotoImage, messagebox
import sqlite3
import os
from PIL import ImageTk, Image

def Elephant():
    """ FUNCÕES """
    def fechar():
        app.destroy()

    def bd01():
        conn = sqlite3.connect("bancodedados.db")
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS dados01 ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'titulo TEXT,'
            'texto Text'
        ')')

    def add_texto(a, b):
        conn = sqlite3.connect("bancodedados.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dados01 (titulo, texto) VALUES (?, ?)', (a, b))
        conn.commit()

    def picture():
        path_image = Image.open(sys.path[0] + '\\img\\' + entrada.get() + '.png')
        get_img = ImageTk.PhotoImage(path_image)
        img_show = Label(app)
        img_show.photo = get_img
        img_show.place(relx=0.55, rely=0.35)
        img_show['image'] = get_img
        img_show.config(text="")

    def buscar():
        bus01 = entrada.get()
        conn = sqlite3.connect("bancodedados.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM dados01")
        c_texto = cursor.fetchall()
        for linha in c_texto:
            identificador, titulo, texto = linha
            if bus01 == titulo:
                labeldes['text'] = texto
                picture()

    def editor():
        root = tk.Tk()
        root.geometry("450x320")
        root["bg"] = "#FF6600"
        def salvar():
            tit_a = ent01.get()
            txt_b = txt01.get('1.0', END)
            add_texto(tit_a, txt_b)
            messagebox.showinfo("Status", "DADOS SALVOS \nCOM SUCESSO!")
            root.destroy()

        ent01 = Entry(root, width=50, font=("Arial 12"))
        ent01.place(relx=0.001, rely=0.001, relheight=0.08)
        txt01 = Text(root, font=("Arial 12"))
        txt01.place(relx=0.001, rely=0.08, relheight=0.8, relwidth=0.998)
        btn2 = Button(root, bg="#1e3743", fg="#FF6600", width=15, text="SALVAR", command=salvar)
        btn2.place(relx=0.37, rely=0.9)

        root.mainloop()

    def nova_tela():
        app.destroy()
        Elephant()

    """ INTERFACE """
    app = tk.Tk()
    app.geometry("700x700+300+5")
    app.title("3LEPHANT - v1.0.0")
    app["bg"] = "#1e3743"
    app.overrideredirect(True)

    # Textos, Entradas e Botões FRAME1
    label02 = Label(app, width=15, text="", bg="#1e3743", fg="#FF6600", font=('Garamond 10'))
    label02.place(relx=0.86, rely=0.05)
    l_titulo = Label(app, width=10, text="3LEPHANT", bg="#1e3743", fg="#FF6600", font=('Garamond 35'))
    l_titulo.place(relx=0.32, rely=0.005)
    label01 = Label(app, width=10, text="Buscar: ", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    label01.place(relx=0.16, rely=0.1)
    entrada = Entry(app, width=40, font=('Arial 15'))
    entrada.place(relx=0.20, rely=0.15, relheight=0.04)

    btnfechar = Button(app, bg="#FF0000", fg="#FFFFFF", width=3, text=" X ", command=fechar)
    btnfechar.place(relx=0.955, rely=0.001)
    btn1 = Button(app, bg="#1e3743", fg="#FF6600", width=15, text="BUSCAR", command=buscar)
    btn1.place(relx=0.20, rely=0.25)
    btn4 = Button(app, bg="#1e3743", fg="#FF6600", width=15, text="EDITAR", command=editor)
    btn4.place(relx=0.40, rely=0.25)
    btn5 = Button(app, bg="#1e3743", fg="#009933", width=15, text="LIMPAR", command=nova_tela)
    btn5.place(relx=0.60, rely=0.25)

    labeldes = Label(app, bg="#1e3743", fg="#FFFFFF", font=('Arial 12'), wraplength=300, text="", anchor=N)
    labeldes.place(relx=0.01, rely=0.35, relwidth=0.49, relheight=0.6)


    app.mainloop()


if __name__ == '__main__':
    Elephant()