# # # Super va Voris classlar
# # #Super class
# class Shaxs:
#     __num_ber=
#     def __init__(self,name,lastname,birthyear):
#         self.name=name
#         self.lastname=lastname
#         self.birthyear=birthyear
#         self.__id=
#     def getinfo(self):
#         return f"Talaba ismi {self.name} {self.lastname} . {self.birthyear}-yilda tug'ilgan . Pasport seriyasi : {self.pasport}"
#     def getage(self):
#         return 2026-self.birthyear        
# # #Voris class
# class Talaba(Shaxs):
#     def __init__(self,name,lastname,birthyear,pasport,idnumber):
#         super().__init__(name,lastname,birthyear,pasport)
#         self.idnumber=idnumber
#         self.bosqich=1
#         self.fanlar=[]
#     def getid(self):
#         return self.idnumber
#     def getfan(self):
#         return self.fan
#     #Poliformizm
#     def getinfo(self):
#         info=f"Talaba {self.name} {self.lastname} . {self.getage()} yoshda . Pasport malumoti : {self.pasport} ."
#         info+=f" Id raqami : {self.idnumber} .{self.bosqich}- bosqich talabasi"
#         return info
    
#     def fangayozil(self,newfan):
#         self.fanlar.append(newfan)
    
#     def fanlist(self):
#         return self.fanlar

    
#     def remove_fan(self,fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             print("Talaba bunday fanga yozilmagan .")


# # class Fanlar:
# #     def __init__(self,fannomi,fansoati,fankrediti):
# #         self.fannomi=fannomi
# #         self.fansoati=fansoati
# #         self.fankrediti=fankrediti

# #     def getfan(self):
# #         return self.fannomi
    
# #     def getfankredit(self):
# #         return self.fankrediti
    
# #     def getfansoati(self):
# #         return self.fansoati
    
# #     def getfanlar(self):
# #         infofan=f"{self.fannomi} . {self.fansoati} soat . Fan {self.fankrediti} kredit"
# #         return infofan

# # fan1=Fanlar("Oliy matematka",180,"6 kredit")
# # fan2=Fanlar("Informatika",120,"4 kredit")
# # fan3=Fanlar("Ingiliz tili",90,"2 kredit")

# # talaba1=Talaba("Ibrohim","G'afurov",2003,"AD0277495","N000286")
# # talaba2=Talaba("Javohir","G'afurov",1994,"AD782895","N2763323")
# # talaba1.fangayozil(fan1.fannomi)
# # talaba1.fangayozil(fan2.fannomi)
# # talaba2.fangayozil(fan1.fannomi)
# # talaba2.fangayozil(fan3.fannomi)

# # print(talaba1.name ," quyidagi fanlarga yozilgan ", talaba1.fanlist())
# # print(talaba2.name ," quyidagi fanlarga yozilgan ", talaba2.fanlist())

# # talaba1.remove_fan("Rus tili")
# # talaba2.remove_fan("Ingiliz tili")

# # print(talaba1.name ," quyidagi fanlarga yozilgan ", talaba1.fanlist())
# # print(talaba2.name ," quyidagi fanlarga yozilgan ", talaba2.fanlist())
# # print(talaba2.getinfo())
# # print(talaba2.getage())
# # print(fan1.fannomi)


# # # Foydalanuvchi class
# # class User(Shaxs):
# #     def __init__(self,name,lastname,birthyear,email,password):
# #         super().__init__(name,lastname,birthyear)
# #         self.email=email
# #         self.password=password
# #     def getinfo(self):
# #         info=f"Foydalanuvchi {self.name} {self.lastname} . {self.birthyear}-yilda tug'ilgan . Email mazili : {self.email}"
# #         info+=f"Foydalanuvchi paroli : {self.password}"
# #         return info

# # #Admin class
# # class Admin(User):
# #     def __init__(self,birthyear,email,password):
# #         super().__init__(birthyear,email,password)

# #     def banuser(self,checpassword):
# #         if checpassword==self.password:
# #             print("Muvaffaqiyatli")
# #         else:
# #             print("Foydalanuvchi bloklandi ! ")

# # foydalanuvchi1=User("Ibrohim","G'afurov",2003,"gafurovibrohim2003@gmail.com","123456")
# # print(foydalanuvchi1.getinfo())

# # admin1=Admin(2003,"gafurovibrohim2003@gmail.com","123456")
# # chek=input("Kirish uchun parol kiriting : ")
# # admin1.banuser(chek)


