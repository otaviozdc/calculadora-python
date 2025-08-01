import tkinter as tk
import math

# Constantes
pi = 3.14159
historico_operacoes = []
calculo_concluido = False

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.config(bg="#222") # Cor de fundo
janela.geometry("360x500") # Tamanho

# Campo de entrada
entrada = tk.Entry(janela, font=(
    "Arial", 24), bg="#111", fg="white", bd=0, justify="right")
entrada.pack(fill="both", padx=10, pady=10, ipady=10)

def ignorar_digitacao(event):
    return "break"

entrada.bind("<Key>", ignorar_digitacao)

# Histórico
historico = tk.Label(janela, text="", font=("Arial", 12), bg="#222", fg="#ccc", justify="left", anchor="w")
historico.pack(fill="both", padx=10, pady=(0,10))

# Funções
def atualizar_historico(nova_operacao):
    historico_operacoes.append(nova_operacao)
    if len(historico_operacoes) > 3:
        historico_operacoes.pop(0)
    historico.config(text="\n".join(historico_operacoes))

def adicionar_caractere(caractere):
    global calculo_concluido
    conteudo_atual = entrada.get()
    if calculo_concluido and (caractere.isdigit() or caractere == "."):
        reiniciar_entrada()
        calculo_concluido = False
    elif calculo_concluido and not (caractere.isdigit() or caractere == "." or caractere == "Erro "):
        calculo_concluido = False
    if conteudo_atual == "Erro ":
        reiniciar_entrada()
        calculo_concluido = False
    entrada.insert(tk.INSERT, caractere)

def apagar_digito():
    conteudo_atual = entrada.get()
    if conteudo_atual: # Verifica se a caixa de entrada não está vazia
        entrada.delete(len(conteudo_atual) - 1, tk.END)

def reiniciar_entrada():
    global calculo_concluido
    entrada.delete(0, tk.END)
    calculo_concluido = False

def adicionar_ponto():
    conteudo = entrada.get()
    if "." in conteudo: # Checa se já tem ponto na entrada
        return
    if not conteudo:
        adicionar_caractere("0.")
    else:
        adicionar_caractere(".")

def calcular():
    try:
        expressao = entrada.get()
        if not expressao:
            return
        expressao = expressao.replace("%", "/100") # Modifica a string se houver porcentagem
        expressao = expressao.replace("÷", "/") # Tornar o sinal da divisão funcional
        expressao = expressao.replace("x", "*") # Tornar o sinal da multiplicação funcional
        expressao = expressao.replace("sqrt", "math.sqrt") # Tornar o botão da raiz quadrada funcional
        expressao = expressao.replace("^", "**")
        resultado = eval(expressao)
        reiniciar_entrada()
        entrada.insert(tk.END, str(resultado))
        atualizar_historico(f"{expressao} = {resultado}")
        global calculo_concluido
        calculo_concluido = True
    except (SyntaxError, ZeroDivisionError, NameError):
        reiniciar_entrada()
        entrada.insert(tk.END, "Erro ")
        calculo_concluido = True

def inserir_raiz():
    global calculo_concluido
    conteudo_atual = entrada.get()
    if calculo_concluido:
        reiniciar_entrada()
        calculo_concluido = False
    entrada.insert(tk.INSERT, "sqrt()")
    entrada.icursor(entrada.index(tk.INSERT) - 1)
    entrada.focus_set()

def inserir_expoente():
    conteudo = entrada.get()
    if conteudo:
        entrada.insert(tk.END, "^")

# Frame dos botões
botoes_frame = tk.Frame(janela, bg="#222")
botoes_frame.pack(fill="both", expand=True)

for i in range(5):
    botoes_frame.grid_rowconfigure(i, weight=1)
for i in range(5):
    botoes_frame.grid_columnconfigure(i, weight=1, minsize=70)

# Botões de números
botao_0 = tk.Button(botoes_frame, text="0", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("0"))
botao_0.grid(row=4, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_1 = tk.Button(botoes_frame, text="1", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("1"))
botao_1.grid(row=3, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_2 = tk.Button(botoes_frame, text="2", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("2"))
botao_2.grid(row=3, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_3 = tk.Button(botoes_frame, text="3", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("3"))
botao_3.grid(row=3, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_4 = tk.Button(botoes_frame, text="4", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("4"))
botao_4.grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_5 = tk.Button(botoes_frame, text="5", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("5"))
botao_5.grid(row=2, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_6 = tk.Button(botoes_frame, text="6", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("6"))
botao_6.grid(row=2, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_7 = tk.Button(botoes_frame, text="7", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("7"))
botao_7.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_8 = tk.Button(botoes_frame, text="8", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("8"))
botao_8.grid(row=1, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_9 = tk.Button(botoes_frame, text="9", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("9"))
botao_9.grid(row=1, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Botões de operações
botao_soma = tk.Button(botoes_frame, text="+", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("+"))
botao_soma.grid(row=4, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_subtracao = tk.Button(botoes_frame, text="-", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("-"))
botao_subtracao.grid(row=3, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_multiplicacao = tk.Button(botoes_frame, text="x", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("x"))
botao_multiplicacao.grid(row=2, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_divisao = tk.Button(botoes_frame, text="÷", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("÷"))
botao_divisao.grid(row=1, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_expoente = tk.Button(botoes_frame, text="^", font=("Arial", 18), bg="#333", fg="white", command=inserir_expoente)
botao_expoente.grid(row=2, column=4, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_raiz_quadrada = tk.Button(botoes_frame, text="√", font=("Arial", 18), bg="#333", fg="white", command=inserir_raiz)
botao_raiz_quadrada.grid(row=1, column=4, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_porcentagem = tk.Button(botoes_frame, text="%", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("%"))
botao_porcentagem.grid(row=4, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

# Botões de controle
botao_apagar = tk.Button(botoes_frame, text="⌫", font=("Arial", 18), bg="#a5a5a5", fg="black", command=apagar_digito)
botao_apagar.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_AC = tk.Button(botoes_frame, text="AC", font=("Arial", 18), bg="#c71515", fg="black", command=reiniciar_entrada)
botao_AC.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_ponto = tk.Button(botoes_frame, text=".", font=("Arial", 18), bg="#333", fg="white", command=adicionar_ponto)
botao_ponto.grid(row=4, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_abre_parenteses = tk.Button(botoes_frame, text="(", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere("("))
botao_abre_parenteses.grid(row=0, column=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_fecha_parenteses = tk.Button(botoes_frame, text=")", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere(")"))
botao_fecha_parenteses.grid(row=0, column=3, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_pi = tk.Button(botoes_frame, text="π", font=("Arial", 18), bg="#333", fg="white", command=lambda: adicionar_caractere(str(pi)))
botao_pi.grid(row=0, column=4, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

botao_igual = tk.Button(botoes_frame, text="=", font=("Arial", 18), bg="#228B22", fg ="white", command=calcular)
botao_igual.grid(row=3, column=4, rowspan=2, padx=5, pady=5, ipadx=10, ipady=10, sticky="nsew")

janela.mainloop()