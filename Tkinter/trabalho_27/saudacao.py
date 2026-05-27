import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 27 de Python")
janela.geometry("500x500")

texto = tk.Label(
    janela,
    text="Seja bem-vindo ao meu trabalho de Python usando Tkinter",
    font=("Arial", 13)
)

texto.place(x=40, y=20)

nome_usuario = tk.Entry(
    janela,
    font=("Arial", 10)
)

nome_usuario.place(x=120, y=50)

def recebendo_valor():
    mensagem = tk.Label(
        janela,
        text=f"Olá {nome_usuario.get()}",
        font=("Arial", 15)
    )

    mensagem.place(x=120, y=150)
    

exibir_mensagem = tk.Button(
    janela,
    text="Ler mensagem",
    width= 13,
    height= 1,
    command=recebendo_valor
)

exibir_mensagem.place(x=290, y=45)

janela.mainloop()