# usage: python3 make_qr.py https://your-domain.com/calc/  ->  qr.png
import sys, qrcode
qrcode.make(sys.argv[1]).save("qr.png"); print("saved qr.png")
