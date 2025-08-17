#import qrcode from pyqrcode

import pyqrcode
import _png 
from pyqrcode import qrcode

#string which representes the qr code

s = ""


#generate qr code
url = pyqrcode.create(s)


#create and save the svg file
url.svg("myqr.svg",scale=8)


#create and save png file
url.png("mysqr.png",scale=6)