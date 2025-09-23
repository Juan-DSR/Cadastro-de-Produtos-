import pyautogui
import time
import pandas as pd

#abrir o google, entrar no site e fazer login
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write('google')
pyautogui.press('Enter')
time.sleep(0.8)
pyautogui.click(x=326, y=644)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('Enter')
time.sleep(0.5)
pyautogui.click(x=657, y=371)
pyautogui.write('serginho@gmai.com')
pyautogui.press('Tab')
pyautogui.write('soulindo')
pyautogui.press('Enter')
time.sleep(0.5)

#Cadastrar produtos 
Tabela = pd.read_csv('produtos.csv')

for linha in Tabela.index:
    pyautogui.click(x=610, y=255)
    pyautogui.write(str(Tabela.loc[linha, 'codigo']))
    pyautogui.press('Tab')
    pyautogui.write(str(Tabela.loc[linha, 'marca']))
    pyautogui.press('Tab')
    pyautogui.write(str(Tabela.loc[linha, 'tipo']))
    pyautogui.press('Tab')
    pyautogui.write(str(Tabela.loc[linha, 'categoria']))
    pyautogui.press('Tab')
    pyautogui.write(str(Tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('Tab')
    pyautogui.write(str(Tabela.loc[linha, 'custo']))
    pyautogui.press('Tab')
    if not pd.isna(Tabela.loc[linha, 'obs']):
        pyautogui.write(str(Tabela.loc[linha, 'obs']))
    pyautogui.press('Enter')
    pyautogui.scroll(10000)
    time.sleep(0.3)