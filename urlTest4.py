from tkinter import *
import webbrowser

root=Tk()
root.title("Third url try")

root.geometry("400x400")

def openUrl():
    webbrowser.open("https://www.ecosia.org","_self")

wButton=Button(root, text="Open Ecosia", command=openUrl).grid(row=3, column=0)

root.mainloop()
