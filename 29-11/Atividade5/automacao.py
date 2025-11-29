import pyautogui as p
import time as t

p.press("win")
t.sleep(1)

p.write("google chrome")
t.sleep(1)

p.press("enter")
t.sleep(3)

p.write("https://www.sp.senai.br/noticia/senai-sp-consolida-lideranca-na-educacao-profissional-com-vitoria-na-worldskills-americas")
t.sleep(1)

p.press("enter")
t.sleep(2)

p.rightClick(920, 620)
t.sleep(1)

p.leftClick(1042, 700)
t.sleep(1)

p.hotkey("win", "d")
t.sleep(1)

p.rightClick(869, 144)
t.sleep(1)

p.leftClick(998, 442)
t.sleep(1)

p.press("down")
t.sleep(1)

p.press("enter", 3)
t.sleep(2)

p.press("f11")
t.sleep(2)

p.rightClick(964, 164)
t.sleep(1)

p.click(1088, 543)
t.sleep(1)

p.press("down", 5)
t.sleep(1)

p.press("enter", 3)
t.sleep(2)

p.hotkey("ctrl", "v")
t.sleep(2)

p.hotkey("ctrl", "b")
t.sleep(1)

p.hotkey("win", "d")
t.sleep(1)