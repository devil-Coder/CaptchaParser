from os import walk
import random
import timeit,os,time
from PIL import Image
def removeNoise(img):
	#clearing image	noise
	pix=img.load()
	for y in range(1,44):
		for x in range(1,179):
			if pix[x,y-1]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x,y+1]==(255,255,255):
				pix[x,y]=(255,255,255)
			if pix[x-1,y]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x+1,y]==(255,255,255):
				pix[x,y]=(255,255,255)
			if pix[x,y]!=(255,255,255) and pix[x,y]!=(0,0,0):
				pix[x,y]=(255,255,255)
	print("\t\tSaving the Noise free image in results folder...")
	im.save("results\\testcase.png")
	print("\t\tShowing the Noise free image in 2 seconds")
	time.sleep(2)
	im.show("results\\testcase.png") 
def CaptchaParse(img):
	print("\t\tThe image selected will be available in 1 seconds.")
	time.sleep(1)
	img.show()
	captcha=""
	dirs=os.listdir("Chars")
	removeNoise(img) ##calling removeNoise() to clear noise
	for j in range(30,181,30):
		#croping each character
		ch=img.crop((j-30,12,j,44))
		pix1=ch.load() ##Holds the pixel of original image
		ch.show()
		matches={}
		for i in dirs:
			match=0
			black=0
			pixx=0
			## matching with each character in Chars folder
			im2=Image.open("Chars\\"+i)
			pix2=im2.load() ##Holds the pixels of the actual characters
			for y in range(0,32):
				for x in range(0,30):
					if pix1[x,y]==pix2[x,y] and pix2[x,y]==(0,0,0):
						match+=1
					if pix2[x,y]==(0,0,0):
						black+=1
					if pix1[x,y]==(0,0,0):
						pixx+=1
			#if float(match)/float(black)>=0.85:
			perc=float(match)/float(black)
			matches.update({perc:i[0].upper()})
		try:
			captcha+=matches[max(matches.keys())]
		except ValueError:
			captcha+="0"
	return captcha
print("\t\t\t\t\tWelcome to Captcha Parser\n\t\t\t***---------------------------------------------------**\n\n")
randomNumber = str(random.randint(0,100))
im=Image.open("download\\"+randomNumber
+".png")
starttime = timeit.default_timer()
captcha=CaptchaParse(im)
print("\t\tThe Final Captcha is :\t "+captcha)
