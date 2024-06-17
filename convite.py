from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode

# Dados do convite
link = "Coloque aqui o link que deseja   que o Qrcode abra"

# Gerar QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(link)
qr.make(fit=True)
img_qr = qr.make_image(fill_color="black", back_color="white")

# Salvar QR Code como imagem
qr_code_filename = "qrcode.png"
img_qr.save(qr_code_filename)

# Criar o arquivo PDF
c = canvas.Canvas("convite.pdf", pagesize=letter)
width, height = letter

# Adicionar a imagem de fundo
c.drawImage("tema.png", 0, 0, width=width, height=height)

# Centralizar o QR Code na página
qr_code_size = 100  # Tamanho do QR Code
qr_x_position = (width - qr_code_size) / 2  # Centralizar horizontalmente
qr_y_position = (height - qr_code_size) / 2 -250  # Centralizar verticalmente
c.drawImage(qr_code_filename, qr_x_position, qr_y_position, width=qr_code_size, height=qr_code_size)

# Salvar o PDF
c.save()
