class Ballite:
  def __init__(self,dekoracijas, ciemini, ediens, vel_davanas, tematika_80tie_gadi):
    self.dekoracijas = dekoracijas
    self.vel_davanas = vel_davanas
    self.ciemini= ciemini
    self.ediens = ediens
    self.tematika_80tie_gadi = tematika_80tie_gadi

  def pirkumi_skaits(self):
    return f"Pirkumu skaits {self.dekoracijas} un{self.ediens}."

  def pirkumi(self):
    return f"Pirkumi {self.dekoracijas} un{self.ediens}"

  def davanas(self):
    return f"davanas{self.vel_davanas}"
  
  def Ciemini(self):
    return f"ciemini{self.ciemini}"


a = Ballite(["virtene, uzlime, pleve"], ["dima, emil, sanja"], ["kola, cipsi, alus"], ["bikses, vejaka, torte"],["temats_80tie_gadi"])
print(a.tematika_80tie_gadi)
print(a.pirkumi_skaits())
print(a.Ciemini())
print(a.davanas())
print(a.pirkumi())