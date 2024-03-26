class Personel:
    def __init__(self, ad, departman, cyil, maas):
        self.ad = ad
        self.departman = departman
        self.cyil = cyil
        self.maas = maas
   
class Firma:
    def __init__(self, personel_list=[]):
        self.personel_list = personel_list
        
    def pers_ekle(self, personel):
        self.personel_list.append(personel)
        
    def personel_listele(self):
        print("Firmanın Personel Listesi:")
        for personel in self.personel_list:
            print("Adı:", personel.ad)
            print("Departmanı:", personel.departman)
            print("Çalışma Yılı:", personel.cyil)
            print("Maaşı:", personel.maas)
            print("")
            
    def maas_zammi(self, personel, zam_oran):
        personel.maas *= (1 + zam_oran / 100)

    def personel_çıkart(self, personel):
        self.personel_list.remove(personel)


personel1 = Personel("Sude", "Satış", 5, 5000)
personel2 = Personel("Ayşe", "Pazarlama", 3, 4500)
personel3=Personel("Ali","Satış",7,6000)

firma = Firma()

firma.pers_ekle(personel1)
firma.pers_ekle(personel2)
firma.pers_ekle(personel3)

firma.personel_listele()
firma.maas_zammi(personel1, 10)
print("-----ZAM UYGULANDI.-----\n\n")
firma.personel_listele()
print("-----BAZI ÇALIŞANLAR ÇIKARTILDI.-----\n\n")
firma.personel_çıkart(personel2)
firma.personel_listele()
