import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from os import system, name
clear = lambda: system("clear" if name == "posix" else "cls")

clear()
print('[EN]Please put QRCODE image file in same directory with this executable alongside.')
print('[EN]File name must be "qrcode" plus image format must be PNG.')
print()
print('     Made by OKTAY MERCAN / Yapan OKTAY MERCAN       ')
print()
print('[TR]Lütfen QRCODE resminizi bu çalıştırdığınız program ile aynı dizine koyunuz.')
print('[TR]Resim PNG formatında ve isimi "qrcode" olacak şekilde ayarlayınız.')
print()
print('[EN]if qrcode.png file is ready then please press enter key to continue read operation.')
print('[TR]qrcode.png dosyanız hazır ise okumayı başlatmak için enter tuşa basınız.')
input()
clear()

# QR kod okuma fonksiyonu
def read_qr_code(image_path):
    image = cv2.imread(image_path)
    decoded_objects = pyzbar.decode(image)

    for obj in decoded_objects:
        if obj.type == 'QRCODE':
            return obj.data.decode('utf-8')
    input()
    return None

# Resim dosyasının yolu
image_path = 'qrcode.png'

# QR kodu oku
result = read_qr_code(image_path)

if result:
    print(f'QRCODE okuma sonucu / QRCODE read result ==> ', {result})
    print()
    print('[EN]NOTE: You can click and open the link by pressing the Ctrl key. Only open web links you trust!')
    print('[TR]NOT: Ctrl tuşuna basarak bağlantıyı tıklayıp açabilirsiniz. Yalnızca güvendiğiniz web bağlantılarını açın!')
else:
    print('[EN]qrcode.png image file missing.')
    print('[TR]qrcode.png resim dosyası eksik.')
