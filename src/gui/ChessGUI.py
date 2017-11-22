#
# Nahtan Timmerman
# November 20, 2017
#
# GUI for chess game 
#

import Tkinter as tk

class ChessGUI(tk.Frame):
    
    def __init__(self, controller):
        tk.Frame.__init__(self, controller )
        self.controller = controller
        #mystuff









if __name__ == "__main__":
    root = tk.Tk()
    #ChessGUI(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


