import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Importe o módulo messagebox separadamente
import openpyxl

class CadastroEquipamentos:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Equipamentos")

        # Campos de entrada
        ttk.Label(self.root, text="Frota:").grid(row=0, column=0, padx=10, pady=5)
        self.frota_entry = ttk.Entry(self.root)
        self.frota_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Tipo:").grid(row=1, column=0, padx=10, pady=5)
        self.tipo_entry = ttk.Entry(self.root)
        self.tipo_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Modelo:").grid(row=2, column=0, padx=10, pady=5)
        self.modelo_entry = ttk.Entry(self.root)
        self.modelo_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Grupo:").grid(row=3, column=0, padx=10, pady=5)
        self.grupo_entry = ttk.Entry(self.root)
        self.grupo_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botão cadastrar
        cadastrar_button = ttk.Button(self.root, text="Cadastrar", command=self.cadastrar_equipamento)
        cadastrar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Caminho do arquivo Excel
        self.db_path = 'equipamentos.xlsx'

    def cadastrar_equipamento(self):
        frota = self.frota_entry.get()
        tipo = self.tipo_entry.get()
        modelo = self.modelo_entry.get()
        grupo = self.grupo_entry.get()

        # Cria ou abre o arquivo Excel
        try:
            workbook = openpyxl.load_workbook(self.db_path)
        except FileNotFoundError:
            workbook = openpyxl.Workbook()

        # Seleciona a planilha "equipamentos" ou cria uma nova
        sheet = workbook.get_sheet_by_name('equipamentos') if 'equipamentos' in workbook.sheetnames \
            else workbook.create_sheet('equipamentos')

        # Verifica se a planilha está vazia
        if sheet.max_row == 1:
            # Insere os cabeçalhos das colunas
            sheet.cell(row=1, column=1, value="Frota")
            sheet.cell(row=1, column=2, value="Tipo")
            sheet.cell(row=1, column=3, value="Modelo")
            sheet.cell(row=1, column=4, value="Grupo")

        # Obtém a última linha preenchida na planilha
        last_row = sheet.max_row

        # Insere os dados na próxima linha vazia
        sheet.cell(row=last_row + 1, column=1, value=frota)
        sheet.cell(row=last_row + 1, column=2, value=tipo)
        sheet.cell(row=last_row + 1, column=3, value=modelo)
        sheet.cell(row=last_row + 1, column=4, value=grupo)

        # Salva as alterações no arquivo Excel
        workbook.save(self.db_path)

        # Limpa os campos de entrada após o cadastro
        self.frota_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)
        self.modelo_entry.delete(0, tk.END)
        self.grupo_entry.delete(0, tk.END)

        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Cadastro de Equipamentos", "Equipamento cadastrado com sucesso!")


# Criação da janela principal
root = tk.Tk()
CadastroEquipamentos(root)
root.mainloop()
