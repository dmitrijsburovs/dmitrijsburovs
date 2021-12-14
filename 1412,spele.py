
import tkinter as tk
import random 
def akmens(event):
  lbl_lietizv['text'] = 'Tava izvēle: Akmens'
  data_izveele()

def papirs(event):
  lbl_lietizv['text'] = 'Tava izvēle: Papīrs'
  data_izveele()
def skeres(event):
  lbl_lietizv['text'] = 'Tava izvēle: Šķēres'
  data_izveele()
def data_izveele():
  izveeles = ['Akmens','Šķēres','Papīrs']
  datizv = random.choice(izveeles)
  lbl_datoraizv['text'] = f'Datora izvēle: {datizv}'
  rezultati()

def rezultati():
  dators = lbl_datoraizv['text']
  lietotajs = lbl_lietizv['text']
  dators = dators.split()
  lietotajs = lietotajs.split()

  if dators[2] == lietotajs[2]:
   lbl_rezultats['text'] = 'Rezultāts: Neizšķirts'
  elif dators[2] == 'Akmens' and lietotajs[2] == 'Šķēres':
   lbl_rezultats['text'] = 'Rezultāts: Jūs zaudējāt'
  elif dators[2] == 'Akmens' and lietotajs[2] == 'Papīrs':
   lbl_rezultats['text'] = 'Rezultāts: Jūs vinnējāt'
  elif dators[2] == 'Šķēres' and lietotajs[2] == 'Papīrs':
   lbl_rezultats['text'] = 'Rezultāts: Jūs zaudējāt'
  elif dators[2] == 'Šķēres' and lietotajs[2] == 'Akmens':
   lbl_rezultats['text'] = 'Rezultāts: Jūs vinnējāt'
  elif dators[2] == 'Papīrs' and lietotajs[2] == 'Šķēres':
   lbl_rezultats['text'] = 'Rezultāts: Jūs vinnējāt'
  elif dators[2] == 'Papīrs' and lietotajs[2] == 'Akmens':
   lbl_rezultats['text'] = 'Rezultāts: Jūs zaudējāt'

  else:
    lbl_rezultats['text'] = 'Vēl jāsataisa'
    
 

window = tk.Tk()


lbl_info = tk.Label(text = "Sveicināts/a!\nŠī ir spēle akmens, šķēres, papīrīts!")

lbl_darit = tk.Label(text = "Izvēlies kādu no zemāk piedāvātajiem variantiem: ")

lbl_lietizv = tk.Label()
lbl_datoraizv = tk.Label()
lbl_rezultats = tk.Label()


btn_akmens = tk.Button(text = "Akmens")
btn_skeres = tk.Button(text = "Šķēres")
btn_papirs = tk.Button(text = "Papīrs")

btn_akmens.bind('<Button-1>', akmens)
btn_papirs.bind('<Button-1>', papirs)
btn_skeres.bind('<Button-1>', skeres)


lbl_info.pack(fill = tk.X)
lbl_darit.pack()
btn_akmens.pack()
btn_papirs.pack()
btn_skeres.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()


window.mainloop()