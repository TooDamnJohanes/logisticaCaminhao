import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Importe o módulo messagebox separadamente

from cadastrar_caminhão import CadastroEquipamentos

FROTA = "Frota:"
TIPO = "Tipo:"
MODELO = "Modelo:"
GRUPO = "Grupo:"
CADASTRAR = "Cadastrar"
JANELA_CADASTRO_EQUIPAMENTO_TITLE = "Cadastro de Equipamentos"

root = tk.Tk()
novo_equipamento = CadastroEquipamentos()


def construcao_janela_equipamento():
    root.title(JANELA_CADASTRO_EQUIPAMENTO_TITLE)
    frota_entry_component()
    tipo_entry_component()
    tipo_entry_component()
    grupo_entry_component()
    botao_cadastrar_equipamento()


def frota_entry_component():
    ttk.Label(root, text=FROTA).grid(row=0, column=0, padx=10, pady=5)
    novo_equipamento.frota_entry = ttk.Entry(root)
    novo_equipamento.frota_entry.grid(row=0, column=1, padx=10, pady=5)


def tipo_entry_component():
    ttk.Label(root, text=TIPO).grid(row=1, column=0, padx=10, pady=5)
    novo_equipamento.tipo_entry = ttk.Entry(root)
    novo_equipamento.tipo_entry.grid(row=1, column=1, padx=10, pady=5)


def modelo_entry_component():
    ttk.Label(root, text=MODELO).grid(row=2, column=0, padx=10, pady=5)
    novo_equipamento.modelo_entry = ttk.Entry(root)
    novo_equipamento.modelo_entry.grid(row=2, column=1, padx=10, pady=5)


def grupo_entry_component():
    ttk.Label(root, text=GRUPO).grid(row=3, column=0, padx=10, pady=5)
    novo_equipamento.grupo_entry = ttk.Entry(root)
    novo_equipamento.grupo_entry.grid(row=3, column=1, padx=10, pady=5)


def botao_cadastrar_equipamento():
    novo_equipamento.cadastrar_button = ttk.Button(root, text=CADASTRAR, command=novo_equipamento.cadastrar_equipamento)
    novo_equipamento.cadastrar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


construcao_janela_equipamento()
root.mainloop()
