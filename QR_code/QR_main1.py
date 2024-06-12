import qrcode as qr
img = qr.make("https://www.linkedin.com/in/kanchan-naval/")
img.save("kanchan_linkedin.png")