import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 0.5

# Passo a passo do projeto

# 1. Abrir o sistema da empresa
link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write(link_sistema)
pyautogui.press("enter")

# pausa maior para carregamento do site
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=904, y=369)
pyautogui.write("email@example.com")
pyautogui.press("tab")
pyautogui.write("asenhamaisdificildomundo@321")
pyautogui.press("tab")
pyautogui.press("enter")

# 3. Importar base de dados para cadastrar
tabela = pd.read_csv("produtos.csv")


# 4. Cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=943, y=258)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)


# 5. Repetir até acabar a lista de produtos

