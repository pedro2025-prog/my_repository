from PIL import Image

# Tworzenie nowego obrazka o rozmiarze 1x1 pikseli z przezroczystością
image = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

# Zapisanie obrazka jako plik PNG
image.save('transparent_pixel.png')
