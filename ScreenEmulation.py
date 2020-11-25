#Test output for 2.9 inch e paper display with dimensions 296x128 

import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=296, width=128)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()