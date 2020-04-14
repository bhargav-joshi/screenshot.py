import pyautogui
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 150, height = 150)
canvas1.pack()

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screenshot.png')

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='red',fg='white',font= 12)
canvas1.create_window(75, 75, window=myButton)

root.mainloop()
