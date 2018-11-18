from src.arena import Arena
from time import sleep
from threading import Thread
from random import randint
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

def stop_test(app):
    sleep(2)
    x1, y1=randint(0,29), randint(0,29)
    app.draw_tile(x1, y1, 'black')
    app.update()
    sleep(2)
    x2, y2=randint(0,29), randint(0,29)
    app.draw_tile(x2, y2, 'red')
    app.update()
    sleep(2)
    x3, y3=randint(0,29), randint(0,29)
    app.draw_tile(x3, y3, 'green')
    app.update()
    sleep(2)
    app.draw_tile(x3, y3)
    app.update()
    sleep(2)
    app.draw_tile(x2, y2)
    app.update()
    sleep(2)
    app.draw_tile(x1, y1)
    app.update()
    sleep(3)
    app.exit()

def main():
    root=tk.Tk()
    app=Arena(master=root,title='Snake Attack')
    app.after(500,stop_test,app)
    # app_thread=Thread(target=stop_test,args=(app,))
    # app_thread.start()
    app.mainloop()


if __name__ == '__main__':
    main()
