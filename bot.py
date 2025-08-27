import pyautogui
import time

print("Você tem 5 segundos para colocar o jogo em foco...")
time.sleep(5)

print("Bot iniciado! Coletando itens...")

while True:
    pyautogui.press('f')  # Coletar itens
    print("Pressionei F")  # DEBUG: mostra no terminal
    time.sleep(2)          # Intervalo entre coletas
