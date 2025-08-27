import pyautogui
import cv2
import numpy as np
import time

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
        print(f"Cliquei em ({x}, {y})!")
        return True
    else:
        print("Botão não encontrado.")
        return False

# --- Loop principal ---
print("Você tem 5 segundos para colocar o jogo em foco...")
time.sleep(5)
print("Bot iniciado! Tentando coletar...")

while True:
    encontrado = encontrar_e_clicar("botao_coletar.png")
    time.sleep(2)
