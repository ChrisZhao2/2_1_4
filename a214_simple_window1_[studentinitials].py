#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
tk.Label(frame_login,text="Password:",font="Courier")
root.mainloop()

#test
def test_my_button():
  frame_auth.tkraise()
tk.Button(frame_login, text="LOG IN")
command=test_my_button
