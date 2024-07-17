import requests
URL="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
class Course:
    def get(self):
        r=requests.get(URL)
        data= r.json()
        usd = float(data[0]['Rate']) 
        return usd
class UzsToUsd(Course):
    def __init__(self,amount):
        self.amount=amount

    def convert(self):
        usd=self.get()
        return self.amount / usd
    
    
class UsdToUzs(Course):
    def __init__(self,amount):
        self.amount=amount
    def convert(self):
        usd=self.get()
        return self.amount*usd
    
    
Ask=input("""So'm dan Do'llarga o'tkazmoqchi bo'lsangiz 'S' deb yozing 
Agar Teskarisi bo'lsa 'D' deb yozing: """)
if Ask.lower()=='s':
    s=float(input("Uzb so'mida pul kiriting:"))
    Uzs=UzsToUsd(amount=s)
    print(f"{Uzs.amount}={Uzs.convert()}$")

elif Ask.lower()=='d':
    d=float(input("Do'llarda pul kiriting: "))
    Usd=UsdToUzs(amount=d)
    print(f"{Usd.amount}={Usd.convert()}UZS")
else:
    print("Xato!!!")