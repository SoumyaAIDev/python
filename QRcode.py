import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, 
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,border=8,)

qr.add_data("file:///C:/Users/Bhargav/Downloads/Soumya%20.photo.pdf")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("qrcode2.png")
img.show()
