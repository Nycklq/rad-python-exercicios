import tkinter as tk

janela = tk.Tk()
janela.title("Cores")
janela.geometry("200x150")

def mudar_cor():
    janela.config(bg=cor_escolhida.get())

cor_escolhida = tk.StringVar()

radio1 = tk.Radiobutton(janela, text="Vermelho", variable=cor_escolhida, value="red", command=mudar_cor)
radio1.pack()

radio2 = tk.Radiobutton(janela, text="Verde", variable=cor_escolhida, value="green", command=mudar_cor)
radio2.pack()

radio3 = tk.Radiobutton(janela, text="Azul", variable=cor_escolhida, value="blue", command=mudar_cor)
radio3.pack()

janela.mainloop()