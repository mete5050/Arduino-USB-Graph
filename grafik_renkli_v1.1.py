
normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pkirmizi= '\033[91m'
pmavi = '\033[96m'
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'
import serial
import os
os.system("dmesg")
print(pmavi)
print("Band genisligini yazin ")
bant = int(input())
print("Hassasligi girin : "+normal)
hsslk = int(input())
os.system("clear")
while True:
    port = serial.Serial("/dev/ttyUSB0", baudrate=bant)
    data = port.readline()  
    sonuc = int(data) * hsslk / 1023
    print pyesil+data+normal+psari+sonuc * "|",pmavi+"[] \n"+normal
