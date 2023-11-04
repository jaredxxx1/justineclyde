
#coding/utf/
#created/by/Dani Malik 
import os
import random
def clear():
    os.system('clear')
    print(logo)
logo=("""\033[1;37m
    \033[97;░
░░░░██╗░█████╗░██████╗░███████╗██████╗░
░░░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
░░░░░██║███████║██████╔╝█████╗░░██║░░██║
██╗░░██║██╔══██║██╔══██╗██╔══╝░░██║░░██║
╚█████╔╝██║░░██║██║░░██║███████╗██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░
\033[91;1m--------------------------------------------------
\033[97;1mOWNER    : \033[0;92mJared \033[0;97m& \033[0;92mJustine
\033[97;1mTOOL     : Hugmal
\033[97;1mCity      : Manila
\033[97;1mTOOL TYPE   : \x1b[96;1mAUTO UA MAKER
\033[91;1m--------------------------------------------------""")
clear()
print('\033[0;97m[+] \033[0;96mYOUR UA \033[97;1m[\033[93;1mUSERAGENT\033[97;1m] \033[96;1mLIST HERE\n\033[1;97m==================================================')
for i in range(100):
        ##################model_,build = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix", "Oppo", "Qmobile",])
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = 'null'
        fban = random.choice(["FB4A"])
        fbpn = random.choice(["com.facebook.katana"])
        fbbd = 'lge'
        user_agent = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/en_US;FBRV/{fbrv};FBCR/{fbcr};FBMF/lge;FBBD/{fbbd};FBPN/{fbpn};FBDV/LGE;FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
print(user_agent)
            