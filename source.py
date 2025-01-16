import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5 
)
data = "https://www.google.com/search?q=artificial+intelligence&oq=aritf&gs_lcrp=EgZjaHJvbWUqDAgBEAAYChixAxiABDIGCAAQRRg5MgwIARAAGAoYsQMYgAQyDAgCEAAYChixAxiABDIMCAMQABgKGLEDGIAEMgwIBBAAGAoYsQMYgAQyDAgFEAAYChixAxiABDIJCAYQABgKGIAEMgwIBxAAGAoYsQMYgAQyCQgIEAAYChiABDIJCAkQABgKGIAE0gEIODYzM2owajeoAgiwAgE&sourceid=chrome&ie=UTF-8"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fit = "black",black_color = "white")
img.save("test.png")
