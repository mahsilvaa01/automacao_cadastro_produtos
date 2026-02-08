import pyautogui as py
import pandas as pd
import time

#importar base dos produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Abrir o sistema
py.PAUSE = 0.5

py.press("win")
time.sleep(3)

py.write("chrome")
py.press("enter")
time.sleep(3)

py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(5)

#esperar carregar
#inserir o login e senha

py.click(x=453, y=408)
py.write("mary.alr2345@gmail.com")
py.press("tab")
time.sleep(2)

py.write("senha1234")
py.press("enter")
time.sleep(5)

#inserir dados do produto

for linha in tabela.index:
    py.click(x=436, y=286)
    codigo = tabela.loc[linha, "codigo"]
    py.write(str(codigo))
    py.press("tab")
    py.write(str(tabela.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str( tabela.loc[linha, "custo"]))
    py.press("tab")   
    if not pd.isna(tabela.loc[linha, "obs"]):
        py.write(str(tabela.loc[linha, "obs"]))
    py.press("tab")
    py.press("enter")
    time.sleep(1)

    # dar scroll de tudo pra cima
    py.scroll(1500)
 #Repetir o cadastro até acabar o cadastro de todos os produtos

    