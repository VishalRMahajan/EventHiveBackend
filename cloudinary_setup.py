import io
import cloudinary
import cloudinary.uploader
import qrcode

config = cloudinary.config(secure=True)


def generate_url(url : str):
    data = url
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the PIL image to a BytesIO object
    image_io = io.BytesIO()
    qr_image.save(image_io, format='PNG')
    image_io.seek(0)

    # Upload QR code image to Cloudinary
    result = cloudinary.uploader.upload(image_io, folder="qr_codes", format='png')

    # Get the URL of the uploaded image
    qr_code_url = result["secure_url"]
    print("QR Code URL:", qr_code_url)
    return qr_code_url