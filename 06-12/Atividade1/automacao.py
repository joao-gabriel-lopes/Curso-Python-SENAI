import pandas as pa
import pyautogui as p
import time as t

p.press("win")
t.sleep(1)

p.write("google chrome")
t.sleep(1)

p.press("enter")
t.sleep(2)

p.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
t.sleep(1)

p.press("enter")
t.sleep(1)

p.leftClick(950, 374)
t.sleep(1)

p.write("Usuario")
t.sleep(1)

p.press("tab")
t.sleep(1)

p.write("senha1234")
t.sleep(1)

p.press("tab")
t.sleep(1)

p.press("enter")
t.sleep(1)

tabela = pa.read_csv("produtos.csv")

for linha in tabela.index:
    
    p.leftClick(950, 260)
    t.sleep(1)

    p.write(tabela.loc[linha, "codigo"])
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.write(tabela.loc[linha, "marca"])
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.write(tabela.loc[linha, "tipo"])
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.write(str(tabela.loc[linha, "categoria"]))
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.write(str(tabela.loc[linha, "preco_unitario"]))
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.write(str(tabela.loc[linha, "custo"]))
    t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    if(str(tabela.loc[linha, "obs"]) != "nan"):
        p.write(tabela.loc[linha, "obs"])
        t.sleep(0.5)

    p.press("tab")
    t.sleep(0.5)

    p.press("enter")
    t.sleep(1)