from tkinter import *
import hashlib 
from tkinter.messagebox import *
import datetime

win = Tk()
win.resizable(False, False)
win.title("MD5PyCracker")
win.iconbitmap('favicon.ico')
win.config(bg='#ecf0f1')

title = Label(win, text='MD5 Python cracker\nby Tobi Sama \n-----------------------------------------\n Twitter: @ryurina23 | Github: @ryurina\n')
title.pack()

labelCode = Label(win, text="Enter MD5 :")
code = StringVar()
textLine = Entry(win, textvariable=code, width=30)
labelCode.pack()
textLine.pack()

def crack():
    mdCode = code.get()
    count = 0
    attempt = 0 
    try:
        passwordFile = open("wordlist.txt", "r")
    except:
        showwarning("Warning","File Not Found : wordlist.txt")
        quit()
        
    for word in passwordFile:
        encodedWord = word.encode('utf-8') 
        digest = hashlib.md5(encodedWord.strip()).hexdigest() 
        attempt += 1
        if digest == mdCode:
            dateNow = datetime.datetime.now()
            logText = '\n{} | Password: {} | Attempts: {}'.format(dateNow, word,attempt)
            logFile = open("log.txt", "a")
            logFile.write(logText)
            logFile.close()
            showwarning('Password Found','Password: {} \nAttempts: {}\n'.format(word,attempt))
            count = 1
            break
        
    if count == 0:
        showwarning("Warning", "Password Not Found!")

crackButton = Button(win, text="Crack", command=crack)
crackButton.pack()

exitButton = Button(win, text="Exit", command=win.quit)
exitButton.pack()

win.mainloop()