import qrcode
import numpy as np
from PIL import Image
 # Define the URL and load the background image
bg_color = (255, 255, 255)  # white background
fg_color = (0, 0, 0)     # black foreground
url = "https://lidengjia1.github.io/"
 # Generate the QR code object
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
 # Make the QR code image
img_qr = qr.make_image(fill_color=fg_color, back_color=bg_color)
img_qr = img_qr.convert('RGBA')
 # Load the heart shape mask
heart_mask = np.array(Image.open("123.jpg").convert('RGBA').resize(img_qr.size))
 # Apply the mask to the QR code image
masked_qr = Image.fromarray(np.uint8(heart_mask * 255))
masked_qr.putalpha(Image.fromarray(np.uint8(heart_mask[:, :, 3] * 255)))
masked_qr = masked_qr.resize(img_qr.size)
 # Combine the QR code and the heart mask
img_qr.paste(masked_qr, (0, 0), masked_qr)
 # Save the final image as a PNG file
img_qr.save("heart_qrcode.png", "PNG")