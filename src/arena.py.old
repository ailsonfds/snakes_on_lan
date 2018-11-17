# arena.py
#!/usr/bin/python3

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

# Thanks to https://stackoverflow.com/questions/12332975/installing-python-module-within-code

class Arena(ttk.Frame, object):
    score_label={}
    score_value_label={}

    def __init__(self, master=None, title='Arena'):
        super(Arena, self).__init__(master, padding="12 12 12 12")
        self.master.title(title)
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pane = tk.Canvas(self, bg='white', height=300, width=300)
        self.pane.grid(column=1, row=1, rowspan=6, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.vlines = []
        self.hlines = []
        for i in range(30):
            self.vlines.append(self.pane.create_line(i*10,0,i*10,300))
            self.hlines.append(self.pane.create_line(0,i*10,300,i*10))
        self.quit = ttk.Button(self, text="QUIT", command=self.master.destroy)
        self.quit.grid(column=2, row=6, sticky=(tk.W,tk.S))

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.master.bind('<Control-c>', self.exit)
        self.master.bind('<Escape>', self.exit)

    def add_score_labels(self, players={}):
        for key, value in players.items():
            self.score_label[key] = ttk.Label(self, text='Score ' + key + ':')
            self.score_label[key].grid(column=2,row=1, sticky=tk.W)
            self.score_value_label[key] = ttk.Label(self, text=value.score)
            self.score_value_label[key].grid(column=3,row=1, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def exit(self,*args):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = Arena(master=root,title='Snake Attack')
    app.mainloop()

    # ttk.Entry(mainframe, width=7, textvariable=feet).grid(column=2, row=1, sticky=(W, E)).focus()
    # root.bind('<Return>', calculate) # on enter key pressed

    # root.mainloop()

if __name__ == "__main__":
    main()
