import qrcode

img = qrcode.make('脑壳高头的包')
img.save('qrcode.png')