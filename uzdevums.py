class Rekins:

  def __init__ (self,klients,veltijums,izmers,materials):
  
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials
    
    self.teksta_gar = len(self.veltijums)
  #print(Rekins)

    self.lad_iz = self.izmeri.split(",")
    self.platums = self.lad_iz[1]
    self.garums = self.lad_iz[0]
    self.augstums = self.lad_iz[2]

def izdruka (self):
  pass
  
def aprekins (self):
 # darba_samaksa = 15
 # PVN = 21
  # produkta_cena = (veltījuma teksta garums simbolos)*1.2 +
  # (platums/100 * garums/100 * augstums/100)/ 3 * materiala_cena
  # PVN_summa = (produkta_cena + darba_samaksa)*PVN/100
  # rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
  pass

veltijums = input("Uzraksti veltijumu:")
izmeri = input("Ievadi lādītes izmērus\n Garums,platums,augstums (raksti veselus skaitļus, atdalot tos ar komatiem\n")

print(izmeri)
print(type(izmeri))
print(izmeri.split(","))
sadal = izmeri.split(",")
print(sadal[0])
print(sadal[1])
print(sadal[2])