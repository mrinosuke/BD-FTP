import requests
import time
import os
from datetime import *
import jx_color
#update chack
R = I.RED
B = I.BLUE
GB = I.B_GREEN
G = I.GREEN
RE = I.RESET
C = I.B_CYAN
ban = '''  sSSs  sdSS_SSSSSSbs   .S_sSSs    
 d%%SP  YSSS~S%SSSSSP  .SS~YS%%b   
d%S'         S%S       S%S   `S%b  
S%S          S%S       S%S    S%S  
S&S          S&S       S%S    d*S  
S&S_Ss       S&S       S&S   .S*S  
S&S~SP       S&S       S&S_sdSSS   
S&S          S&S       S&S~YSSY    
S*b          S*S       S*S         
S*S          S*S       S*S         
S*S          S*S       S*S         
S*S          S*S       S*S         
SP           SP        SP          
Y            Y         Y           
                                   '''


time = datetime.now().strftime("%Y%m%d_%M")
#print(time)
#de = input("enter ")
info = '''Tool        : FTP server scanner (BD)
Version     : 1.0
status      : Khola usso'''
bod = "###########-###########-###########-############\n"

try:
    on_of = requests.get("https://www.google.com", timeout=1)

    if on_of.status_code < 400:
        on_st = "Online"
    else:
        on_st = "Offline"
except requests.exceptions.RequestException:
    on_st = "Offline"
  
bod_D = f"\n{bod}"
os.system("clear")
try:
    print(GB + ban)
    print(B + bod)
    print(C + info)
    print(f"Nework      : {on_st}")
    print(B + bod_D)

    if on_st == "offline":
        exit()

    else:
        pass

    uc = input("start scan ? (y/n) : ")

    if uc == "y":
        pass

    else:
        exit()
    
    
    os.system("clear")
    work_link = []
    with open("url.txt", "r") as ftp:
        all_url = ftp.readlines()
        total_url = len(all_url)
        t_url = int(total_url)
        print(B + f"Total FTP server  : {t_url} " )

        u_num = int(input("Enter scan amount : "))
        os.system("clear")

        print("###################################")
        print("   SACNING......     SACNING......")
        print("##################################\n")
        co = 0
        w_url = 0 
        n_url = 0 
        e_url = 0

        for url in all_url:
            url = url.strip()

            if not url:
                continue

            co += 1

            if co > u_num:
                break

            try:
                r = requests.get(url, timeout=0.2)
                if r.status_code < 400:
                    w_url += 1
                    work_link.append(url)
                    print(G + f"{co}. {url} - Working")
                else:
                    n_url += 1
                    print(R + f"{co}. {url} - Not Working")
            except:
                e_url += 1

                print(R + f"{co}. {url} - Error404")

            

        print(B + f"\nTotal scan     : {co - 1}")
        print(G + f"Total work     : {w_url}")
        print(R + f"Total not work : {n_url}")
        print(R + f"Total error    : {e_url}")
        Cho = input(B + "\nSave Working url ? (y/n) :")
        if Cho == "y":
            with open(f"working_url-{time}.txt", "w") as save:
                for url in work_link:
                    save.write(f"{url}\n")

            print(G + f"\nYour url save on working_url-{time}.txt")
            x = input("\nEnter.....")

        else:
            print("Bye bye")
            exit()
                



except:
    print("hi")
    print("heloo")



