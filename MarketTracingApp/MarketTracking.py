import requests
from time import sleep
from bs4 import BeautifulSoup
import playsound as ps
import time

def Dollar():
    request = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    a = 0
    while True:
        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        Dollar = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_Dollar = float(Dollar.replace(",","."))
        output1 = f"Dollar = {float_Dollar}"
        value1 = float_Dollar
        
        if(a == 0):
            print(output1+'\n')
        a = 1
        sleep(10)

        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        Dollar = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_Dollar = float(Dollar.replace(",","."))
        output2 = f"Dollar = {float_Dollar}"
        value2 = float_Dollar
        current_time = time.strftime("%H:%M:%S")
        
        if(value2 > value1):
            ps.playsound(r"alkissesi.wav")
            print(current_time)
            print(output2 +' ↑'+'\n')
            
        elif(value2 == value1):        
            print(current_time)
            print("(not changed)")
            print(output2+'\n')

        else:
            ps.playsound(r"kecibagirmasesi.wav")        
            print(current_time)
            print(output2 +' ↓'+'\n')
    

def XRP():
    request = "https://www.google.com/finance/quote/XRP-TRY?hl=tr"
    a = 0
    while True:
        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        XRP = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_XRP = float(XRP.replace(",","."))
        output1 = f"XRP = {float_XRP}"
        value1 = float_XRP
        
        if(a == 0):
            print(output1+'\n')
        a = 1
        sleep(10)

        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        XRP = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_XRP = float(XRP.replace(",","."))
        output2 = f"XRP = {float_XRP}"
        value2 = float_XRP
        current_time = time.strftime("%H:%M:%S")
        
        if(value2 > value1):
            ps.playsound(r"alkissesi.wav")
            print(current_time)
            print(output2 +' ↑'+'\n')
            
        elif(value2 == value1):        
            print(current_time)
            print("(not changed)")
            print(output2+'\n')

        else:
            ps.playsound(r"kecibagirmasesi.wav")        
            print(current_time)
            print(output2 +' ↓'+'\n')

def Euro():
    request = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    a = 0
    while True:
        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        Euro = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_Euro = float(Euro.replace(",","."))
        output1 = f"Euro = {float_Euro}"
        value1 = float_Euro
        
        if(a == 0):
            print(output1+'\n')
        a = 1
        sleep(10)

        respond = requests.get(request)
        page_content = BeautifulSoup(respond.content,"html.parser")
        Euro = page_content.find("div",class_="YMlKec fxKbKc").get_text()
        float_Euro = float(Euro.replace(",","."))
        output2 = f"Euro = {float_Euro}"
        value2 = float_Euro
        current_time = time.strftime("%H:%M:%S")
        
        if(value2 > value1):
            ps.playsound(r"alkissesi.wav")
            print(current_time)
            print(output2 +' ↑'+'\n')
            
        elif(value2 == value1):        
            print(current_time)
            print("(not changed)")
            print(output2+'\n')

        else:
            ps.playsound(r"kecibagirmasesi.wav")        
            print(current_time)
            print(output2 +' ↓'+'\n')


secim = str(input(print('TAKİP ETMEK İSTEDİĞİNİZ BİRİMİ SEÇİNİZ :\n DOLAR İÇİN (1) TUŞLAYINIZ\n EURO  İÇİN (2) TUŞLAYINIZ\n XRP   İÇİN (3) TUŞLAYINIZ')))
if(secim == '1'):
    Dollar()
elif(secim == '2'):
    Euro()
elif(secim == '3'):
    XRP()
else:
    quit()

