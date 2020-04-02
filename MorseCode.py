import time
import RPi.GPIO as GPIO
from Tkinter import *

window = Tk()
window.geometry("300x250")
window.title("Morse Code Converter")

textInput = StringVar()

LED = 21 # define led pin 21

# setup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

# dot
def dot():
	GPIO.output(LED, 1)
	time.sleep(0.5)
	GPIO.output(LED, 0)
	time.sleep(0.5)

# dash
def dash():
	GPIO.output(LED, 1)
	time.sleep(2)
	GPIO.output(LED, 0)
	time.sleep(0.5)

# delay
def delay():
	time.sleep(1)

# individual letters for conversion
def a():
	dot()
	dash()

def b():
	dash()
	dot()
	dot()
	dot()
	
def c():
	dash()
	dot()
	dash()
	dot()

def d():
	dash()
	dot()
	dot()
	
def e():
	dot()

def f():
	dot()
	dot()
	dash()
	dot()

def g():
	dash()
	dash()
	dot()
	
def h():
	dot()
	dot()
	dot()
	dot()
	
def i():
	dot()
	dot()
	
def j():
	dot()
	dash()
	dash()
	dash()
	
def k():
	dash()
	dot()
	dash()
	
def l():
	dot()
	dash()
	dot()
	dot()
	
def m():
	dash()
	dash()
	
def n():
	dash()
	dot()
	
def o():
	dash()
	dash()
	dash()
	
def p():
	dot()
	dash()
	dash()
	dot()
	
def q():
	dash()
	dash()
	dot()
	dash()
	
def r():
	dot()
	dash()
	dot()
	
def s():
	dot()
	dot()
	dot()

def t():
	dash()
	
def u():
	dot()
	dot()
	dash()
	
def v():
	dot()
	dot()
	dot()
	dash()
	
def w():
	dot()
	dash()
	dash()
	
def x():
	dash()
	dot()
	dot()
	dash()

def y():
	dash()
	dot()
	dash()
	dash()
	
def z():
	dash()
	dash()
	dot()
	dot()

#converts words with greater than 12 characters
def Morse_Code_Conversion():
	MorseCode = textInput.get()
	if len(MorseCode) > 12:
		return
	for i in MorseCode:
		if i.lower() == "a":
			a()
		elif i.lower() == "b":
			b()
		elif i.lower() == "c":
			c()
		elif i.lower() == "d":
			d()
		elif i.lower() == "e":
			e()	
		elif i.lower() == "f":
			f()
		elif i.lower() == "g":
			g()
		elif i.lower() == "h":
			h()
		elif i.lower() == "i":
			i()
		elif i.lower() == "j":
			j()
		elif i.lower() == "k":
			k()
		elif i.lower() == "l":
			l()
		elif i.lower() == "m":
			m()
		elif i.lower() == "n":
			n()
		elif i.lower() == "o":
			o()
		elif i.lower() == "p":
			p()
		elif i.lower() == "q":
			q()
		elif i.lower() == "r":
			r()
		elif i.lower() == "s":
			s()
		elif i.lower() == "t":
			t()
		elif i.lower() == "u":
			u()
		elif i.lower() == "v":
			v()
		elif i.lower() == "w":
			w()
		elif i.lower() == "x":
			x()
		elif i.lower() == "y":
			y()
		elif i.lower() == "z":
			z()
		delay()
		


textEntry = Entry(window, width=12, textvariable=textInput)#.grid(column=2, row=1)
Convert_Button = Button(window, text="Convert to Morse Code", command=Morse_Code_Conversion)#.grid(column=2, row=13)

textEntry.pack(side=LEFT)
Convert_Button.pack(side=RIGHT)


window.mainloop()
