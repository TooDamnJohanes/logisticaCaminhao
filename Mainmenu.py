import tkinter as tk
import subprocess

from Constants import MENU_PRINCIPAL, PYTHON, CADASTRAR_CAMINHAO_JANELA, DESPACHO_JANELA, LOGISTICA_JANELA, JANELAS, \
    CADASTRO_CAMINHOES, DESPACHO, FRENTE_COLHEITA


def open_cadastro_caminhoes():
    subprocess.call([PYTHON, CADASTRAR_CAMINHAO_JANELA])


def open_despacho_janela():
    subprocess.call([PYTHON, DESPACHO_JANELA])


def open_frentes_janela():
    subprocess.call([PYTHON, LOGISTICA_JANELA])


# Criação da janela principal
janela_principal = tk.Tk()
janela_principal.title(MENU_PRINCIPAL)

# Criação do menu
menu_principal = tk.Menu(janela_principal)
janela_principal.config(menu=menu_principal)

# Criação do menu "Janelas"
menu_janelas = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label=JANELAS, menu=menu_janelas)
menu_janelas.add_command(label=CADASTRO_CAMINHOES, command=open_cadastro_caminhoes)
menu_janelas.add_command(label=DESPACHO, command=open_despacho_janela)
menu_janelas.add_command(label=FRENTE_COLHEITA, command=open_frentes_janela)

# Execução da janela principal
janela_principal.mainloop()
