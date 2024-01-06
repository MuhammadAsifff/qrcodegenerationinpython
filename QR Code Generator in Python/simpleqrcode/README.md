## QR Code Generation in Python.
In this video we learn how to generate QR Code using Python. Now the question is, what is qrcode and why we use QR Code ? QR mean Quick Response because they can be read quickly by a camera e.g: cell phone.
QR codes are used to encode and decode the data into a machine-readable form.
For example: 
website_url = "https://www.example.com"
plain_text = "Hello, QR Code!"
product_info = "Product: A123\nPrice: $19.99\nSKU: 987654321"



For qrcode generation there is two processes:
1. Is a normal process in which qr code directly generate 
2. It is a advanced process, in which we change the basic properties of qrcode.

First of all we install the Python library then we import qrcode from it, I give qrcode a nick name 'qr' because I'm not wanna write the lengthy word qrcode. When we import qrcode we see many functions there, from those functions we use some functions,
for example : 
1. Make function make the qrcode
2. Save function give us qrcode in the form of image and png is image extension.

First we make variable i.e is 'asif'. And I equal asif to qr, on the qr I apply make method is a function provided by the qr library to create a QR code. In make function i put 'URL' in it in the form of string, we also use text in it like hello world and when i scan the qrcode i get the text message, After generating the qrcode we save it and for this i used save function and in the bracket i used again strig and in string i write the text in it that will become the name of qrcode and this file I wanna saved in image format so i write dot png in the last of name of text and doing this simple qrcode will generate, that is black and white, Where we create this py file generated qrcode will be there. And finally we open it and also scan it with mobile. 
First of all we install the Python library, pip install qrcode[pil] ,pil for qrcode image formating.