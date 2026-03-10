# #Dender metodlar
# class Avtosalon:
#     def __init__(self,salonname):
#         self.salonnomi=salonname
#         self.avtolar=[]
#     def addavto(self,avto):
#         if isinstance(avto,Avto):
#             self.avtolar.append(avto)
#         else:
#             print("Avto clasiga tegishli obyekt jo'nating .")
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self,index):
#         return self.avtolar[index]
    
#     def __setitem__(self,index,newavto):
#         if isinstance(newavto,Avto):
#             self.avtolar[index]=newavto
#         else:
#             print("Avto clasiga tegishli obyekt kiriting .")
#     def __call__(self):
#         return [avto for avto in self.avtolar]

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
#     # def __str__(self):
#     #     return f"{self.model} {self.make} . Rangi {self.rang} . Narxi {self.narh}"
#     def __repr__(self):
#         return f"{self.model} {self.make} . Rangi {self.rang} . Narxi {self.narh}"

#     def __lt__(self,y):
#         return self.narh<y.narh
#     def __eq__(self,y):
#         return self.rang==y.rang
#     def __le__(self,y):
#         return self.narh<=y.narh
    
# salon1=Avtosalon("Bankrot")
# avto1=Avto("BMW","M 5","qora",2026,30000)
# avto2=Avto("GM","Lacetti","qora",2024,12000)
# avto3=Avto("Mercedes","Mers","oq",2007,20000)
# avto4=Avto("Mercedes","Mers","oq",2007,20000)
# for avto in [avto1,avto2,avto3,avto4]:
#     salon1.addavto(avto)
# salon1[0]=avto4
# print(salon1())





class Universitet:
    def __init__(self,nomi,manzili):
        self.nomi=nomi
        self.manzili=manzili
    def getname(self):
        return self.nomi
    def getmanzil(self):
        return self.manzili
    #Dunder metodlari
    def __repr__(self):
        return f"{self.nomi} {self.manzili}da joylashgan"

class Fakultet:
    def __init__(self,faknomi,talabalar_soni):
        self.faknomi=faknomi
        self.talabalar_soni=talabalar_soni
    def getname(self):
        return self.faknomi
    def gettalabalar_soni(self):
        return self.talabalar_soni

class Fan:
    def __init__(self,fannomi,fankrediti,fansoati):
        self.fannomi=fannomi
        self.fankrediti=fankrediti
        self.fansoati=fansoati
        self.talabalar=[]

    def __repr__(self):
        return self.fannomi
    def addstudent(self,student):
        if isinstance(student,Talabalar):
            self.talabalar.append(student)
        else:
            print("Talabalar klasiga tegishli obyekt kiriting ")
    def __getitem__(self,index):
        return self.talabalar[index]
    def __setitem__(self,index,value):
        self.talabalar[index]=value
    def __len__(self):
        return len(self.talabalar)
    def gettalabalar(self):
        return self.talabalar
    def __call__(self):
        return [talaba for talaba in self.talabalar]
    




class Talabalar:
    def __init__(self,name,lastname,guruh,yosh):
        self.name=name
        self.lastname=lastname
        self.guruh=guruh
        self.yosh=yosh
        self.bosqich=1
    def getname(self):
        return self.name
    def getlastname(self):
        return self.lastname
    def getage(self):
        return self.yosh
    def getguruh(self):
        return self.guruh
    #Dunder 
    def __repr__(self):
        return f"Talaba ismi {self.name} {self.lastname} . Guruhi {self.guruh} . {self.bosqich}-bosqich talabasi . "
    def __eq__(self,y):
        return self.yosh==y.yosh
    def __lt__(self,y):
        return self.yosh<y.yosh
    
universitet1=Universitet("Samarqand davlat universiteti","Boulvar")
universitet2=Universitet("Toshkent axborot texnalogiyalari universiteti","Toshkent shaxar")
# print(universitet1)
# print(universitet2)

talaba1=Talabalar("Ibrohim","G'afurov","405-gurux",23)
talaba2=Talabalar("Rustamjon","Alijonov","405-gurux",22)
talaba3=Talabalar("Jasur","Islomov","405-gurux",23)
talaba4=Talabalar("Ollayor","Bazarboyev","404-gurux",24)
# if talaba1==talaba2:
#     print(f"{talaba1.getname()} va {talaba2.getname()}ning yoshi teng ")
# elif talaba1>talaba2:
#     print(f"{talaba1.getname()}ning yoshi katta {talaba2.getname()}ning yoshidan")
# else:
#     print(f"{talaba1.getname()}ning yoshi {talaba2.getname()}ning yoshidan kichik")


fan1=Fan("Tarix",4,120)
fan2=Fan("Ingiliz tili",2,90)
fan3=Fan("Falsafa",6,180)
fan4=Fan("Matematika",6,180)


for talaba in [talaba1,talaba2,talaba4]:
    fan1.addstudent(talaba)
for talaba in [talaba1,talaba3,talaba4,talaba2]:
    fan2.addstudent(talaba)
for talaba in [talaba2,talaba3,talaba4]:
    fan3.addstudent(talaba)
for talaba in [talaba1,talaba3,talaba4]:
    fan4.addstudent(talaba)
print(fan1[0])
fan1[0]=talaba2
print(fan1[0])

print(fan1())