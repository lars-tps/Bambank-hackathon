import qrcode
def make_qr(file_name):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=4,
    )
    qr.add_data('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    qr.make(fit=True)
    img=qr.make_image(fill='black',back_color='white')
    img.save('qrcode/'+file_name+'.png')