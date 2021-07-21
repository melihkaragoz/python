
#############################

import qrcode
import os

#############################

if os.name=="nt":
    os.system("cls")
elif os.name=="posix":
    os.system("clear")

try:
    os.chdir("QRS")
except:
    pass


##########################################################

imMake = input("KareKod'a donusturulecek metni girin >> ")
if imMake=="url":
	imMakeURL = raw_input("Linki girin >> ")
	imMakeURL = "https://" + imMakeURL
	im = qrcode.make(imMakeURL)
elif imMake=="exit":
	exit()
else:
	im = qrcode.make(imMake)
imName = input("Dosyaya isim veriniz >> ")
imName = imName + ".png"
im.save(imName)
print("\n >>\t QR CODE OLUSTURULDU.\t\n")
print(" >>\t {} OLARAK KAYDEDILDI.\t\n\n\n".format(imName))
