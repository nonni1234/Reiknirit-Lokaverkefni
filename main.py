from Keila import Keila
from Kula import Kula
from Sivalningur import Sivalningur
from List import List


listi = List()


kula = Kula(10)
kula2 = Kula(8)

keila = Keila(5,8)
keila2 = Keila(10,10)

sival = Sivalningur(10,6)
sival2 = Sivalningur(10,5)

listi.append(kula)
listi.append(keila)
listi.append(sival)
listi.append(kula2)
listi.append(keila2)
listi.append(sival2)

listi.printList()
print()
print("Stærsta Keilan:", listi.staerstaKeila())
print("Stærsta Kúlan:", listi.staerstaKula())
print("Stærsti Sívalningurinn:", listi.staerstiSivalningur())


