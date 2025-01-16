import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5 
)
data = "https://www.instagram.com/ajaijash_94?igsh=MTdwM2plNDRxanc5MQ=="
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fit = "black",black_color = "white")
img.save("test.png")
