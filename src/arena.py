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
    tile_size=10

    def __init__(self, master=None, title='Arena',tile_size=10):
        super(Arena, self).__init__(master, padding="12 12 12 12")
        self.master.title(title)
        self.tile_size=tile_size
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pane = tk.Canvas(self, bg='white', height=300, width=300)
        self.pane.height=300
        self.pane.width=300
        self.pane.grid(column=1, row=1, rowspan=6, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.vlines = []
        self.hlines = []
        # self.vlines.append(self.pane.create_line(1,0,1,self.pane.height))
        # self.hlines.append(self.pane.create_line(0,1,self.pane.width,1))
        for i in range(31):
            self.vlines.append(self.pane.create_line(i*self.tile_size,0,i*self.tile_size,self.pane.height))
            self.hlines.append(self.pane.create_line(0,i*self.tile_size,self.pane.width,i*self.tile_size))

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.master.bind('<Control-c>', self.exit)
        self.master.bind('<Control-q>', self.exit)
        self.master.bind('<Alt-F4>', self.exit)
        self.master.bind('<Control-Escape>', self.exit)
        self.master.bind('<Escape>', self.exit)

    def draw_tile(self,xloc,yloc,color='white'):
        self.pane.create_rectangle(xloc*self.tile_size, yloc*self.tile_size, (xloc+1)*self.tile_size, (yloc+1)*self.tile_size, fill=color)

    def lose_msg(self, msg='YOU LOSE'):
        self.pane.create_text(150, 150, text=msg, fill='red', font=("Helvetica", 20, "bold"), justify=tk.CENTER)

    def create_score(self,players={}):
        for i, (key, value) in enumerate(players.items()):
            self.score_label[key] = ttk.Label(self, text='Score ' + key + ':')
            self.score_label[key].grid(column=2,row=i+1, sticky=tk.W)
            self.score_value_label[key] = ttk.Label(self, text=value)
            self.score_value_label[key].grid(column=3,row=i+1, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def update_score(self, players={}):
        try:
            for key, value in players.items():
                self.score_value_label[key]['text']=value
        except KeyError:
            self.create_score(self, players)
        finally:
            for key, value in players.items():
                self.score_value_label[key]['text']=value

    def exit(self,*args):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Arena(master=root,title='Snake Attack')
    app.mainloop()

if __name__ == "__main__":
    main()