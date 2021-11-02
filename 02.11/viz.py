import tkinter as tk

window = tk.Tk()

label = tk.Label(
  text = "Sveiki! Sveiki! Sveiki! Sveiki! hello Sveiki!",
  foreground = "red" ,
  background = "#34A2FE"
  )

label1 = tk.Label(
  text = "Čau!",
  fg = "red",
  bg = "#34A2FE",
  width = 20,
  height = 15
  )

label.pack()
label1.pack

window.mainloop()