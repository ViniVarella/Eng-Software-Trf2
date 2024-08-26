import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programa de Busca e Ordenação")
        self.geometry("400x350")  # Aumentei a altura para acomodar a tela 3

        # Configuração da cor de fundo
        self.config(bg="#2E2E2E")  # Cinza escuro
        
        # Variáveis para armazenar os números e a chave de busca
        self.numeros = []
        self.chave = None
        
        self.tela1()
    
    def tela1(self):
        # Limpa a tela
        for widget in self.winfo_children():
            widget.destroy()
        
        # Configuração do Label com Comic Sans MS e tamanho maior
        tk.Label(self, text="Digite 8 números inteiros:", 
                 bg="#2E2E2E", fg="#FFFFFF", font=("Comic Sans MS", 12)).pack(pady=10)
        
        self.campos = []
        for i in range(8):
            campo = tk.Entry(self, bg="#333333", fg="#FFFFFF", insertbackground='white')  # Cor de fundo do campo
            campo.pack(pady=5)
            self.campos.append(campo)
        
        tk.Button(self, text="Entra", command=self.processar_numeros, bg="#444444", fg="#FFFFFF", width=15).pack(pady=20)
    
    def processar_numeros(self):
        try:
            # Verifica se todos os campos foram preenchidos
            if any(campo.get().strip() == "" for campo in self.campos):
                raise ValueError("Favor inserir todos os oito números inteiros.")
            
            # Converte os valores dos campos para inteiros
            self.numeros = []
            for campo in self.campos:
                valor = campo.get().strip()
                if not valor.isdigit() or '.' in valor:
                    raise ValueError("Insira somente números inteiros.")
                self.numeros.append(int(valor))
            
            if len(self.numeros) != 8:
                raise ValueError("Deve inserir exatamente 8 números.")
            
            self.numeros.sort()
            self.tela2()
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
    
    def tela2(self):
        # Limpa a tela
        for widget in self.winfo_children():
            widget.destroy()
        
        # Configuração do Label com Comic Sans MS e tamanho maior
        tk.Label(self, text="Digite o número a ser buscado:", 
                 bg="#2E2E2E", fg="#FFFFFF", font=("Comic Sans MS", 12)).pack(pady=10)
        
        self.campo_busca = tk.Entry(self, bg="#333333", fg="#FFFFFF", insertbackground='white')  # Cor de fundo do campo
        self.campo_busca.pack(pady=5)
        
        tk.Button(self, text="Entra", command=self.processar_busca, bg="#444444", fg="#FFFFFF").pack(pady=20)
    
    def processar_busca(self):
        try:
            valor = self.campo_busca.get().strip()
            if not valor.isdigit() or '.' in valor:
                raise ValueError("Insira somente números inteiros.")
            self.chave = int(valor)
            self.tela3()
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")
    
    def tela3(self):
        # Limpa a tela
        for widget in self.winfo_children():
            widget.destroy()
        
        # Configuração do Label com Comic Sans MS e tamanho maior
        if self.chave in self.numeros:
            posicao = self.numeros.index(self.chave)
            resultado = f"A chave {self.chave} foi encontrada na posição {posicao}."
        else:
            resultado = f"A chave {self.chave} não foi encontrada."
        
        tk.Label(self, text=resultado, bg="#2E2E2E", fg="#FFFFFF", font=("Comic Sans MS", 12)).pack(pady=20)
        tk.Button(self, text="Voltar", command=self.tela1, bg="#444444", fg="#FFFFFF").pack(pady=20)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
