#Import Python Module
import qrcode


data = "Type your message here"

img = qrcode.make(data=data)

#save qrcode
img.save("Secret Message.png")
