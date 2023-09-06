import tkinter as tk
from tkinter import ttk

from FrenteColheita import FrenteColheita

JANELA_DESPACHO_TITLE = "Sistema de Despacho de Caminhões"
FRENTE_COLHEITA_01 = "Frente 1"
FRENTE_COLHEITA_02 = "Frente 2"

frentes_corte = [FRENTE_COLHEITA_01, FRENTE_COLHEITA_02]

# Lista de frotas disponíveis
frota_disponivel = ['Frota 1', 'Frota 2', 'Frota 3']

janela_principal = tk.Tk()


def construcao_janela_despacho():
    janela_principal.title(JANELA_DESPACHO_TITLE)
    abas_frentes = cria_notebook_abas_frente_corte()
    for frente in frentes_corte:
        cria_aba_frente_corte(nome_frente=frente, abas_frentes=abas_frentes)
    # Posicionamento das abas
    abas_frentes.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


# Criação das abas para as frentes de colheita
def cria_notebook_abas_frente_corte():
    return ttk.Notebook(janela_principal)


def cria_aba_frente_corte(nome_frente, abas_frentes):
    frente_frame = ttk.Frame(abas_frentes)
    abas_frentes.add(frente_frame, text=nome_frente)
    FrenteColheita(frente_frame, frota_disponivel)


construcao_janela_despacho()
# Execução da janela principal
janela_principal.mainloop()
