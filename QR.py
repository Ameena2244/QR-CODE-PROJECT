import qrcode

data = "https://github.com/Ameena2244"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  
    border=4, 
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="white")
img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
