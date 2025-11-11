import tkinter as tk
from tkinter import messagebox

def adicionar_despesa():
    nome = entrada_nome.get()
    valor = entrada_valor.get()

    if not nome or not valor:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido!")
        return

    despesas.append((nome, valor))
    atualizar_lista()
    entrada_nome.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)

def atualizar_lista():
    lista_despesas.delete(0, tk.END)
    total = 0
    for nome, valor in despesas:
        lista_despesas.insert(tk.END, f"{nome}: R$ {valor:.2f}")
        total += valor
    label_total.config(text=f"Total de despesas: R$ {total:.2f}")

def limpar_despesas():
    despesas.clear()
    lista_despesas.delete(0, tk.END)
    label_total.config(text="Total de despesas: R$ 0.00")

# --- Interface Tkinter ---
janela = tk.Tk()
janela.title("Calculadora de Despesas Mensais")
janela.geometry("350x400")
janela.resizable(False, False)

despesas = []

tk.Label(janela, text="Nome da despesa:").pack(pady=(10, 0))
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack()

tk.Label(janela, text="Valor (R$):").pack(pady=(10, 0))
entrada_valor = tk.Entry(janela, width=30)
entrada_valor.pack()

tk.Button(janela, text="Adicionar Despesa", command=adicionar_despesa).pack(pady=5)
tk.Button(janela, text="Limpar Tudo", command=limpar_despesas).pack(pady=5)

lista_despesas = tk.Listbox(janela, width=40, height=10)
lista_despesas.pack(pady=10)

label_total = tk.Label(janela, text="Total de despesas: R$ 0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

janela.mainloop()
