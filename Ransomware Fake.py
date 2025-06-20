import tkinter as tk
import threading
import time
import pyautogui
import socket
import platform
import os
from datetime import datetime
import getpass
import random

# Simula o bloqueio do mouse (opcional)
def bloquear_mouse():
    while True:
        pyautogui.moveTo(960, 540)  # centro da tela
        time.sleep(0.1)

# Função para gerar uma linha de números binários aleatórios
def gerar_linha_binaria(largura=64):
    return ''.join(random.choice('01') for _ in range(largura))

# Função para atualizar a "matrix" animada
def animar_matrix(label, linhas=10, largura=64, intervalo=100):
    def atualizar():
        linhas_binarias = [gerar_linha_binaria(largura) for _ in range(linhas)]
        texto = '\n'.join(linhas_binarias)
        label.config(text=texto)
        label.after(intervalo, atualizar)
    atualizar()

# Coleta informações do sistema
def coletar_informacoes():
    return {
        "usuário": getpass.getuser(),
        "computador": platform.node(),
        "sistema": platform.system() + " " + platform.release(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "diretorio": os.getcwd(),
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Simula uma contagem regressiva (só visual)
def contagem_regressiva(label):
    tempo = 30 # 5 minutos
    while tempo > 0:
        mins, secs = divmod(tempo, 60)
        label.config(text=f"Tempo restante: {mins:02d}:{secs:02d}")
        time.sleep(1)
        tempo -= 1
    label.config(text="SEUS DADOS FORAM PERDIDOS!")

def iniciar_ransomware_fake():
    info = coletar_informacoes()

    root = tk.Tk()
    root.title("ATENÇÃO: SEUS DADOS FORAM CRIPTOGRAFADOS")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    mensagem = tk.Label(root, text="SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!",
                        fg="red", bg="black", font=("Arial", 32, "bold"))
    mensagem.pack(pady=30)

    detalhes = tk.Label(root,
                        text="Para recuperar seus arquivos, envie 1 Bitcoin para o endereço XYZ123...",
                        fg="white", bg="black", font=("Arial", 18))
    detalhes.pack()

    # Label para animação matrix
    matrix_label = tk.Label(root, text="", fg="green", bg="black", font=("Courier", 14), justify="left")
    matrix_label.pack(pady=20)

    timer = tk.Label(root, text="", fg="yellow", bg="black", font=("Arial", 24))
    timer.pack(pady=20)

    # Informações do sistema (para intimidar)
    infos_label = tk.Label(root,
        text=(
            f"Sistema comprometido: {info['sistema']}\n"
            f"Usuário: {info['usuário']}\n"
            f"Nome do computador: {info['computador']}\n"
            f"Endereço IP Local: {info['ip']}\n"
            f"Diretório afetado: {info['diretorio']}\n"
            f"Data e hora do ataque: {info['data']}"
        ),
        fg="orange", bg="black", font=("Courier", 12), justify="left")
    infos_label.pack(pady=10)

    # Ameaças adicionais
    ameaça1 = tk.Label(root, text="TODOS OS SEUS ARQUIVOS SERÃO DESTRUÍDOS APÓS O PRAZO.",
                       fg="red", bg="black", font=("Arial", 16, "bold"))
    ameaça1.pack()

    ameaça2 = tk.Label(root, text="UMA CÓPIA DOS SEUS DADOS FOI ENVIADA PARA NOSSOS SERVIDORES.",
                       fg="red", bg="black", font=("Arial", 16, "bold"))
    ameaça2.pack()

    ameaça3 = tk.Label(root, text="SE NÃO PAGAR, SUAS INFORMAÇÕES PESSOAIS SERÃO VENDIDAS NO MERCADO NEGRO.",
                       fg="red", bg="black", font=("Arial", 16, "bold"))
    ameaça3.pack(pady=20)

    ameaça4 = tk.Label(root, text="NÃO HÁ COMO RECUPERAR SEUS DADOS SEM O PAGAMENTO.",
                       fg="white", bg="black", font=("Arial", 14, "italic"))
    ameaça4.pack()

    threading.Thread(target=contagem_regressiva, args=(timer,), daemon=True).start()
    threading.Thread(target=bloquear_mouse, daemon=True).start()

    # Inicia animação matrix
    animar_matrix(matrix_label)

    root.mainloop()

iniciar_ransomware_fake()