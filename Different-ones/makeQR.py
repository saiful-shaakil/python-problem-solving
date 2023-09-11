# Importing QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# String which would be represented by QR Code
enter_your_link = input("Enter your link to make QRCode: ")

# Generate QR Code
url = pyqrcode.create(enter_your_link)

# Create and save the svg & png file naming "myQRCode"
url.svg("myQRCode.svg", scale=8)
url.png("myQRCode.png", scale=6)
