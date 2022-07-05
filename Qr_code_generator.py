import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=12,
    border=6
    )

data='https://www.youtube.com/c/HOMESTUDY247'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="blue",back_color="white")
img.save("img1.png")

