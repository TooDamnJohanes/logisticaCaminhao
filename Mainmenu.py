import tkinter as tk
from tkinter import ttk
import subprocess

def open_cadastro_caminhoes():
    subprocess.call(["python", "cadastrar_caminhão.py"])

def open_despacho_janela():
    subprocess.call(["python", "DespachoJanela.py"])

def open_frentes_janela():
    subprocess.call(["python", "Logistica.py"])

# Criação da janela principal
janela_principal = tk.Tk()
janela_principal.title("Menu Principal")

# Criação do menu
menu_principal = tk.Menu(janela_principal)
janela_principal.config(menu=menu_principal)

# Criação do menu "Janelas"
menu_janelas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Janelas", menu=menu_janelas)
menu_janelas.add_command(label="Cadastro de Caminhões", command=open_cadastro_caminhoes)
menu_janelas.add_command(label="Despacho", command=open_despacho_janela)
menu_janelas.add_command(label="Frentes de Colheita", command=open_frentes_janela)

# Execução da janela principal
janela_principal.mainloop()