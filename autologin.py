#Abrir o mecanismo de pesquisa
#Buscar por valorant
#Clicar no primeiro resultado
#preencher os dados da conta
#Pressionar Enter
#Clicar em jogar
import pyautogui
import time
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Valorant")
pyautogui.press("enter")
time.sleep(10)
pyautogui.write("MyUSERNAME")
pyautogui.press("tab")
pyautogui.write("MyPassoword")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=391, y=401)
