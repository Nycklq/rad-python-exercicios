import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x250")

label1 = tk.Label(janela, text="Primeiro número:")
label1.pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

label2 = tk.Label(janela, text="Segundo número:")
label2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

def somar():
    resultado = float(entrada1.get()) + float(entrada2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def subtrair():
    resultado = float(entrada1.get()) - float(entrada2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def multiplicar():
    resultado = float(entrada1.get()) * float(entrada2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

def dividir():
    resultado = float(entrada1.get()) / float(entrada2.get())
    label_resultado.config(text="Resultado: " + str(resultado))

botao_soma = tk.Button(janela, text="+", command=somar)
botao_soma.pack()

botao_sub = tk.Button(janela, text="-", command=subtrair)
botao_sub.pack()

botao_mult = tk.Button(janela, text="*", command=multiplicar)
botao_mult.pack()

botao_div = tk.Button(janela, text="/", command=dividir)
botao_div.pack()

janela.mainloop()