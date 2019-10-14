"""
NNSTU IRIT 16-V-2
Student: Shunin Kirill
14 10 2019
"""
from PIL import Image, ImageDraw 
from random import randint
from re import findall
#шифруемое сообщение
message = 'Hello, my name is Kirill'
#функция кодирования сообщения в картинку
def stega_encode():
	img = Image.open('original.jpg')
	draw = ImageDraw.Draw(img)
	width = img.size[0]
	height = img.size[1]
	pix = img.load()
	f = open('keys.txt','w')

	for elem in ([ord(elem) for elem in message]):
		key = (randint(1,width-10),randint(1,height-10))
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	img.save('encoded.png', 'PNG')
	f.close()
#функция дешифрации из картинки по ключу
def stega_decode():
	
	a = []						    
	keys = []
	img = Image.open('encoded.png')				
	pix = img.load()
	f = open('keys.txt','r')
	y = str([line.strip() for line in f])				
															
	for i in range(len(findall(r'\((\d+)\,',y))):
		keys.append((int(findall(r'\((\d+)\,',y)[i]),int(findall(r'\,\s(\d+)\)',y)[i]))) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])

stega_encode()
print(stega_decode())