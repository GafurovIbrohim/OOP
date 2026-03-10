#Avto class

class Avtosalon:
    def __init__(self,salonnomi,manzili):
        self.salonname=salonnomi
        self.manzili=manzili
        self.boravtomabillar=[]
    def addavto(self,avtonomi):
        self.boravtomabillar.append(avtonomi)
    def avtoroyxat(self):
        return self.boravtomabillar

class Avto:
    def __init__(self,model,nomi,rangi,karobka,narx):
        self.model=model
        self.nomi=nomi
        self.rangi=rangi
        self.karobka=karobka
        self.narxi=narx
        self.kilometr=0
    def getinfo(self):
        return f"Avtomabil modeli {self.model} . Nomi {self.nomi} . Narxi {self.narxi} $ . {self.karobka} karobka . Rangi {self.rangi} . {self.kilometr} km yurgan "
    def addkilometr(self,masofa):
        self.kilometr+=masofa
        return self.kilometr
    def avtoname(self):
        return self.nomi

avto1=Avto("BYD","BYD Champion","black","avtomat",20000)
avto2=Avto("Chevrolet","Malibu","white","mexanik",10000)
avto1.addkilometr(1000)
avto2.addkilometr(2200)
print(avto1.getinfo())
print(avto2.getinfo())

avtosalon=Avtosalon("BYD","Toshkent shaxar")
avtosalon.addavto(avto1.avtoname())
avtosalon.addavto(avto2.avtoname())
print(f"Salondagi mavjud avtomabillar {avtosalon.avtoroyxat()}")

print(dir(avto1))
print(Avto.__dict__)