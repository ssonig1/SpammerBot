import pyautogui
import time
f = open("word.txt", 'w')
a = input('Enter Your Spam Line : \n')
b = int(input('Enter How much line You Execute \n'))
for i in range(b):
    f.write(a)
    f.write("\n")
f.close()
print('you have 10 Sec to place your cursor where you want to spam , them BOM:)')
words = open("word.txt", 'r')
time.sleep(20)
for word in words:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
