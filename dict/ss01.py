import Tkinter as tk
import ss03
lis=[]
root=tk.Tk()
root.title("DICTIONARY")
root.geometry("230x50")
tk.Label(root,text="WORD").grid(row=0)
s1=tk.StringVar()
tk.Entry(root,width=30,textvariable=s1).grid(row=0,column=1)
def ss():
	s=str(s1.get())
	ss03.search(s)
	root.destroy()
tk.Button(root, text="SEARCH", command=ss,width=25).grid(row=1,column=1)
root.mainloop()