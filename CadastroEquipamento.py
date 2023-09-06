import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Constants import CAMINHAO_PATH_FOLDER_NAME
from GerenciaArquivosExcel import GerenciaArquivosExcel


class CadastroEquipamentos:
    EQUIPAMENTOS = 'equipamentos'
    FROTA = "Frota"
    TIPO = "Tipo"
    MODELO = "Modelo"
    GRUPO = "Grupo"
    COLUNA_FROTA = 1
    COLUNA_TIPO = 2
    COLUNA_MODELO = 3
    COLUNA_GRUPO = 4
    COLUNAS_PLANILHA_CADASTRO_EQUIPAMENTO = {
        COLUNA_FROTA: FROTA,
        COLUNA_TIPO: TIPO,
        COLUNA_MODELO: MODELO,
        COLUNA_GRUPO: GRUPO,
    }
    MESSAGEBOX_DIALOG_TITLE = "Cadastro de Equipamentos"
    MESSAGEBOX_DIALOG_DESCRIPTION = "Equipamento cadastrado com sucesso!"

    def __init__(self):
        # Campos de entrada
        self.frota_entry = ttk.Entry()
        self.tipo_entry = ttk.Entry()
        self.modelo_entry = ttk.Entry()
        self.grupo_entry = ttk.Entry()
        self.gerenciador_planilha_equipamentos = GerenciaArquivosExcel(
            path_arquivo_ser_criado=CAMINHAO_PATH_FOLDER_NAME,
            nome_planilha=self.EQUIPAMENTOS
        )
        self.dicionario_dados_novo_equipamento = {}

    def cria_dicionario_atributos_cadastro(self):
        return {
            self.COLUNA_FROTA: self.frota_entry.get(),
            self.COLUNA_TIPO: self.tipo_entry.get(),
            self.COLUNA_MODELO: self.modelo_entry.get(),
            self.COLUNA_GRUPO: self.grupo_entry.get()
        }

    def cadastrar_equipamento(self):
        # Cria um dicionário para cada campo do cadastro
        self.dicionario_dados_novo_equipamento = self.cria_dicionario_atributos_cadastro()

        # Verifica se a planilha está vazia
        self.cria_cabecalho_planilha_se_necessario()

        # Insere os dados na próxima linha vazia
        self.insere_dados_proxima_linha()
        # Salva as alterações no arquivo Excel
        self.salva_planilha()

        # Limpa os campos de entrada após o cadastro
        self.limpa_campos_apos_cadastro()

        # Exibe uma mensagem de sucesso
        self.dialog_equipamento_cadastrado()

    def cria_cabecalho_planilha_se_necessario(self):
        for (coluna, value) in self.COLUNAS_PLANILHA_CADASTRO_EQUIPAMENTO.items():
            self.gerenciador_planilha_equipamentos.insere_cabecalho_planilha(
                colum=coluna,
                value=value,
            )

    def insere_dados_proxima_linha(self):
        last_row = self.retorna_valor_proxima_linha_planilha()
        for (coluna, value) in self.dicionario_dados_novo_equipamento.items():
            self.gerenciador_planilha_equipamentos.insere_dados_proxima_linha(row=last_row, column=coluna, value=value)

    def retorna_valor_proxima_linha_planilha(self):
        return self.gerenciador_planilha_equipamentos.retorna_ultima_linha_planilha() + 1

    def salva_planilha(self):
        self.gerenciador_planilha_equipamentos.salva_planilha()

    def limpa_campos_apos_cadastro(self):
        self.frota_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)
        self.modelo_entry.delete(0, tk.END)
        self.grupo_entry.delete(0, tk.END)

    def dialog_equipamento_cadastrado(self):
        messagebox.showinfo(self.MESSAGEBOX_DIALOG_TITLE, self.MESSAGEBOX_DIALOG_DESCRIPTION)
