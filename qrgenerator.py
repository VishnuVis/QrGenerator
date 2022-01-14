import qrcode
import image
qr = qrcode.QRCode(
    version =15,
    box_size = 10,
    border = 5
)

data ="https://www.instagram.com/invites/contact/?i=qs9c2u8f0uqe&utm_content=jrc0nob"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill ="black",back_color = "white")
img.save("qr.png")

# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('love')
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")