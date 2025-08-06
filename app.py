import tkinter as tk
import requests
from tkinter import messagebox
from tkinter import font as tkfont


def buscar_pais():
    nome_pais = entrada.get().strip()
    if not nome_pais:
        messagebox.showwarning("Aviso", "Digite o nome de um país.")
        return

    url = f"https://restcountries.com/v3.1/name/{nome_pais}"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        pais = dados[0]

        nome = pais.get("name", {}).get("common", "Desconhecido")
        capital = pais.get("capital", ["Desconhecida"])
        capital = capital[0] if capital else "Desconhecida"
        regiao = pais.get("region", "Desconhecida")
        populacao = pais.get("population", 0)
        area = pais.get("area", 0)

        resultado["text"] = (
            f"🌍 País: {nome}\n"
            f"🏛️ Capital: {capital}\n"
            f"🌎 Região: {regiao}\n"
            f"👥 População: {populacao:,}\n"
            f"📏 Área: {area:,} km²"
        )
    except Exception as e:
        resultado["text"] = "Não foi possível encontrar o país."



# --- Estilização ---
BG_COLOR = "#22223b"
FG_COLOR = "#f2e9e4"
BTN_COLOR = "#4a4e69"
BTN_HOVER = "#9a8c98"
ENTRY_BG = "#f2e9e4"
ENTRY_FG = "#22223b"
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_RESULT = ("Segoe UI", 11)

def on_enter(e):
    botao_buscar["background"] = BTN_HOVER
def on_leave(e):
    botao_buscar["background"] = BTN_COLOR

janela = tk.Tk()
janela.title("Explorador de Países - REST Countries")
janela.geometry("420x350")
janela.configure(bg=BG_COLOR)

titulo = tk.Label(janela, text="Explorador de Países", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR)
titulo.pack(pady=(18, 5))

label = tk.Label(janela, text="Digite o nome de um país:", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR)
label.pack(pady=(5, 8))

entrada = tk.Entry(janela, width=28, font=FONT_LABEL, bg=ENTRY_BG, fg=ENTRY_FG, relief="flat", justify="center")
entrada.pack(ipady=5)

botao_buscar = tk.Button(janela, text="Buscar", font=FONT_LABEL, bg=BTN_COLOR, fg=FG_COLOR, activebackground=BTN_HOVER, activeforeground=FG_COLOR, command=buscar_pais, relief="flat", cursor="hand2")
botao_buscar.pack(pady=14, ipadx=10, ipady=3)
botao_buscar.bind("<Enter>", on_enter)
botao_buscar.bind("<Leave>", on_leave)

resultado = tk.Label(janela, text="", font=FONT_RESULT, bg=BG_COLOR, fg=FG_COLOR, justify="left", anchor="w")
resultado.pack(pady=12, fill="both", expand=True, padx=18)

janela.mainloop()
