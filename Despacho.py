import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import ttk

from Constants import ERRO


class Despacho(tk.Toplevel):
    CAMINHAO = "Caminhão:"
    DESPACHAR = "Despachar"
    MESSAGEBOX_ERROR_MESSAGE = "Selecione um caminhão para despachar."

    def __init__(self, frente_nome, frota_disponivel, despacho_callback, caminhao_selecionado):
        super().__init__()

        # Variável para armazenar o caminhão selecionado
        self.configuracoes_iniciais(frente_nome=frente_nome, despacho_callback=despacho_callback)

        # Combo box para selecionar o caminhão
        self.combo_box_selecionar_caminhao(frota_disponivel=frota_disponivel)

        # Botão de despachar
        self.cria_boatao_despachar()

        self.caminhao_selecionado.set(caminhao_selecionado)  # Adicione essa linha para definir o valor selecionado

    def configuracoes_iniciais(self, frente_nome, despacho_callback):
        self.title(f"Frente: {frente_nome}")
        self.caminhao_selecionado = tk.StringVar()
        self.frente_nome = frente_nome  # Adicione essa linha
        self.hpc = 0  # Adicione essa linha
        self.vmc = 0  # Adicione essa linha
        self.tch = 0  # Adicione essa linha
        self.qc = 0  # Adicione essa linha
        self.nc = 0  # Adicione essa linha
        self.proximo_cam_str = ""  # Adicione essa linha
        self.raio = 0
        self.despacho_callback = despacho_callback

    def combo_box_selecionar_caminhao(self, frota_disponivel):
        ttk.Label(self, text=self.CAMINHAO).grid(row=0, column=0, padx=10, pady=5)
        caminhao_combobox = ttk.Combobox(self, textvariable=self.caminhao_selecionado, values=frota_disponivel)
        caminhao_combobox.grid(row=0, column=1, padx=10, pady=5)

    def cria_boatao_despachar(self):
        despachar_button = ttk.Button(self, text=self.DESPACHAR, command=self.despachar)
        despachar_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def despachar(self):
        caminhao = self.caminhao_selecionado.get()

        if caminhao:
            self.despacho_callback(caminhao)
            self.destroy()
        else:
            messagebox.showerror(ERRO, self.MESSAGEBOX_ERROR_MESSAGE)
