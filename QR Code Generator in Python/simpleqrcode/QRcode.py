# First of all we install the Python library
# pip install qrcode[pil] 
# pil for qrcode image formating

# I give qrcode a nick name 'qr'
import qrcode as qr

# Make function: Make the qrcode
img = qr.make('https://www.linkedin.com/in/muhammadasifai/')

# Save function: Give us qrcode in the form of image and png is image extension.
img.save('Linkedin.png')