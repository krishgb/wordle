from pyautogui import press, write, hotkey, position, moveTo, click
import pyautogui
from time import sleep

url = 'https://www.nytimes.com/games/wordle/index.html'
console_code = 'let m;for(let i of $r.hooks) if(!i.name.length) {m = i.subHooks[1].subHooks[4].value.api.solution.data.solution;break;}'

# press win key
press('super')
sleep(0.5)

# search for browser and open it
write('browser')
press('enter')
sleep(1)

# type the url in search bar
write(url)
press('enter')
sleep(1)

# open Developer tools in browser
# press('f12')
hotkey('ctrl', 'shift', 'j')
sleep(2)

# clear the console
hotkey('ctrl', 'l')
sleep(2)

# press react components tab
# print(position())
com_pos = [1161, 554]
moveTo(com_pos[0], com_pos[1])
click()
sleep(2)

# press Ki component
# print(position())
a_pos = [153, 805]
moveTo(a_pos[0], a_pos[1])
click()
sleep(2)

# # move back to console tab
hotkey('ctrl', 'shift', 'j')
sleep(1)
hotkey('ctrl', 'shift', 'j')
sleep(1.5)

# # write script in console
hotkey('ctrl', 'l')
write(console_code)
press('enter')
sleep(2)
# print(position())

# # print(position)
# print(position())
pos = [53, 653]
moveTo(pos[0], pos[1])
click()
click()
click()

hotkey('ctrl', 'c')
hotkey('ctrl', 't')
write('https://web.whatsapp.com')
press('enter')
sleep(12)

# whatsapp
wordle_pos = [179, 266]
moveTo(wordle_pos[0], wordle_pos[1])
click()
sleep(1)

hotkey('ctrl', 'v')
pyautogui.press('enter')