import pyautogui 


pyautogui.PAUSE = 2
#abrir o programa
pyautogui.press("win")
pyautogui.write("login.xlsx") 
pyautogui.press("backspace")
pyautogui.press("enter")

#preencher login
pyautogui.click(x = 523, y = 312)
pyautogui.write("Fabricio")

#preencher senha
pyautogui.click(x = 499, y = 346)
pyautogui.write("abc123")

#clicar em Fazer Login
pyautogui.click(x = 485, y = 432)





