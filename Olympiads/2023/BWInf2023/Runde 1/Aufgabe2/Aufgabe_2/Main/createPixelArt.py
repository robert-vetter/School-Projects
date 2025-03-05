from PIL import Image
import os

directory_path = os.path.dirname(__file__)

myImage = Image.open(directory_path+"\screenshot0.jpg")

smallImage = myImage.resize((32, 32), Image.BILINEAR);

resultImage = smallImage.resize(myImage.size, Image.NEAREST)

resultImage.save(directory_path+"\Main"+"pixelArt.png")

