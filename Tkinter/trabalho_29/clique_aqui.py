import tkinter as tk

janela = tk.Tk()
janela.title("Contador")
janela.geometry("200x150")

contador = 0

label = tk.Label(janela, text="0", font=("Arial", 20))
label.pack(pady=20)

def contar():
    global contador
    contador = contador + 1
    label.config(text=str(contador))

botao = tk.Button(janela, text="Clique aqui", command=contar)
botao.pack()

janela.mainloop()