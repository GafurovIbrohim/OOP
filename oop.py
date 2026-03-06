#OOP --. OBJECT ORIENTER PROGRAMMING 

# class Telefon:
#     def __init__(self,brend,model,narx):  
#         self.brend=brend
#         self.model=model
#         self.narx=narx
          
#     def info(self):
#         return f"Telefon brendi {self.brend} . Telefon modeli {self.model} . Telefon narxi {self.narx}"
#     def chegirma(self,foiz):
#         chegirmafoiz=self.narx-self.narx/100*foiz
#         return f"Asl telefonimizning narxi {self.narx} ga teng . Biz sizga {foiz} % chegirma qilib berdik . Siz {chegirmafoiz} som to'lashingiz kerak . "

# telefon1=Telefon("Samsung","Samsung A14",240000)
# telefon2=Telefon("Redmi","Redmi 13c",180000)
# telefon3=Telefon("Iphone","Iphone 17 pro max",2000000)

# print(f"{telefon1.info()} . {telefon1.chegirma(10)}")
# print(f"{telefon2.info()} . {telefon2.chegirma(20)}")
# print(f"{telefon3.info()} . {telefon3.chegirma(30)}")


#user 
class User:
    def __init__(self,name,lastname,email):
        self.name=name
        self.lastname=lastname
        self.email=email
    def info(self):
        return f"Foydalanuvchi simi {self.name} . Familiyasi {self.lastname} . Email manzili : {self.email}"
    
user=User("Ibrohim","G'afurov","gafurovibrohim2003@gmail.com")
print(user.info())
        