import pyautogui
import cv2
import numpy as np
import time
import keyboard  # pip install keyboard

# Lista dos 8 botões que precisa clicar antes do farm
botoes_iniciais = [
    "imagens/botao1.png",
    "imagens/botao2.png",
    "imagens/botao3.png",
    "imagens/botao4.png",
    "imagens/botao5.png",
    "imagens/botao6.png",
    "imagens/botao7.png",
    "imagens/botao8.png"
]

# Função para encontrar e clicar
def encontrar_e_clicar(template_path, precisao=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    w, h = template.shape[1], template.shape[0]

    resultado = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= precisao:
        x, y = max_loc[0] + w // 2, max_loc[1] + h // 2
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()
        print(f"Cliquei em {template_path} ({x}, {y})!")
        return True
    else:
        print(f"{template_path} não encontrado.")
        return False

# --- Loop inicial: clicar nos 8 botões ---
print("Você tem 5 segundos para colocar o jogo em foco...")
time.sleep(5)
print("Clicando nos 8 botões iniciais...")

for botao in botoes_iniciais:
    encontrado = False
    while not encontrado:  # Repete até encontrar e clicar
        if keyboard.is_pressed('q'):
            print("Bot parado pelo usuário.")
            exit()
        encontrado = encontrar_e_clicar(botao)
        time.sleep(0.5)

print("Botões iniciais clicados! Começando farm automático...")

# --- Loop do farm ---
botoes_farm = ["imagens/botao_coletar.png"]

while True:
    if keyboard.is_pressed('q'):
        print("Bot parado pelo usuário.")
        break

    for botao in botoes_farm:
        encontrar_e_clicar(botao)

    time.sleep(1)
