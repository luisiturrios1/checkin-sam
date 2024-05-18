import qrcode
import qrcode.image.svg
from ids import ids


for id in ids:
    # SVG
    img_svg = qrcode.make(
        f"https://XXXXX.execute-api.us-east-1.amazonaws.com/Prod/checkin/{id}",
        image_factory=qrcode.image.svg.SvgImage,
    )
    with open(f"invitaciones/svg/{id}.svg", "wb") as qr_svg:
        img_svg.save(qr_svg)

    # PNG
    img_png = qrcode.make(
        f"https://XXXXXXXX.execute-api.us-east-1.amazonaws.com/Prod/checkin/{id}"
    )
    with open(f"invitaciones/png/{id}.png", "wb") as qr_png:
        img_png.save(qr_png)

    print(id)
