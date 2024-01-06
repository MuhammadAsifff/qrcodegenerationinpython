# We import qrcode from python library.
import qrcode

# here saved the data in the url variable 
url = 'https://www.linkedin.com/in/muhammadasifai/'

# here change the functionality of qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# here add the data in the qr variable 
qr.add_data(url)

# here make the qrcode
qr.make(fit=True)

# here change the color of qrcode
img = qr.make_image(fill_color="green", back_color="black")

# here save the qrcode 
img.save('linkedin.png')
