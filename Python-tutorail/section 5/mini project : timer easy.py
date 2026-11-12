import time
from os import system, name

while True:
    
    choice = input("Do you want to start? (y/n): \n")
    
    if "y" in choice.lower():
        
        hour = int(input("enter H:  "))
        mint = int(input("enter M:  "))
        seco = int(input("enter S:  "))
        total = hour * 60 * 60 + mint * 60 + seco
        
        print("Timer is start now...")
        
        time.sleep(1)
        
        while total != 0:
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt":# این اف ها برای پاک کردن صفحه موقع تایم زدن هستن
                system("cls")
            else:
                system("clear")
        
        print("time is end\n")

    elif "n" in choice.lower():
        print("Exiting...")
        break

    else:
        print("Invalid input...")
