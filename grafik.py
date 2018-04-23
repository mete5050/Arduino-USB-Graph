#METE EKER
#python 3 ile çalışır
import serial
import os
os.system("dmesg")#eğer windows kullanıyorsanız bu satırı silin veya alternatif bir komut bulun 
print("USB portu yazınız :")#/dev/AMC0 , COM1 gibi arduuinonun bağlı olduğu usb portu yazınız
usbport = input()
print("Band genişliğini yazın ")#serial okuma için arduinoda seçilen serial değerini yazın(Arduino kodunda Serial.begin(); ile gösterilen kısım )
bant = int(input())
os.system("clear")#eğer windows kullanıyorsanız bu satıra os.system("cls") yazın
while True:
    port = serial.Serial(usbport, baudrate=bant)#usb portu ve band genişliğini bidirdik
    data = port.readline()#Serial porttan veri okumaya başladık  
    sonuc = int(data) * 100 / 1023#arduinoda en fazla genellikle 1023 değeri olduğu için onu baz alarak yüz ile oranladık
    print (sonuc * " ","| \n") 
