import re
import tkinter as tk
from tkinter import messagebox

# ----------------------------------------
# FUNÇÕES DE VALIDAÇÃO (REGEX)
# ----------------------------------------

def validar_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)


def validar_telefone(telefone):
    # Formato: +244 9XXXXXXXX (9 dígitos começando com 9)
    return re.match(r'^\+244\s9\d{8}$', telefone)


def validar_data(data):
    return re.match(r'^\d{2}-\d{2}-\d{4}$', data)


def validar_nif(nif):
    return re.match(r'^\d{9}$', nif)


# ----------------------------------------
# DECORADOR
# ----------------------------------------

def validar_formulario(validacoes):
    def decorador(func):
        def wrapper(**kwargs):
            erros = {}

            for campo, func_validacao in validacoes.items():
                valor = kwargs.get(campo)

                if not valor:
                    erros[campo] = "Campo obrigatório"
                elif not func_validacao(valor):
                    erros[campo] = f"Formato inválido"

            if erros:
                return {"status": "erro", "erros": erros}

            return func(**kwargs)
        return wrapper
    return decorador


# ----------------------------------------
# FUNÇÃO PROCESSAMENTO
# ----------------------------------------

@validar_formulario({
    "email": validar_email,
    "telefone": validar_telefone,
    "data": validar_data,
    "nif": validar_nif
})
def processar(email, telefone, data, nif):
    return {"status": "sucesso"}


# ----------------------------------------
# INTERFACE TKINTER
# ----------------------------------------

def submeter():
    dados = {
        "email": entry_email.get(),
        "telefone": entry_telefone.get(),
        "data": entry_data.get(),
        "nif": entry_nif.get()
    }

    resultado = processar(**dados)

    if resultado["status"] == "erro":
        msg = "\n".join([f"{k}: {v}" for k, v in resultado["erros"].items()])
        messagebox.showerror("Erro de Validação", msg)
    else:
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")


# Criar janela
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("350x300")

# Labels e campos
tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela, width=30)
entry_email.pack()

tk.Label(janela, text="Telefone (ex: (92) 12345-6789)").pack()
entry_telefone = tk.Entry(janela, width=30)
entry_telefone.pack()

tk.Label(janela, text="Data (DD-MM-AAAA)").pack()
entry_data = tk.Entry(janela, width=30)
entry_data.pack()

tk.Label(janela, text="NIF (9 dígitos)").pack()
entry_nif = tk.Entry(janela, width=30)
entry_nif.pack()

# Botão
tk.Button(janela, text="Submeter", command=submeter).pack(pady=10)

# Rodar aplicação
janela.mainloop()