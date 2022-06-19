from PIL import Image
from PIL import Image, ImageEnhance

img =Image.open("../assets/evening1.jpg")
img = img.convert("RGBA")
img = ImageEnhance.Brightness(img).enhance(0.3)


frontImage = Image.open("../assets/text_white.png")
background = img

width = (background.width - frontImage.width) // 2
height = (background.height - frontImage.height) // 2
background.paste(frontImage, (width-1100, height-800), frontImage)
background.show()
background.save("../output/monji.png", format="png")
