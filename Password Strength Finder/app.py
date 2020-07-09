from tkinter import *
import re

root = Tk()
root.geometry('400x200+400+250')
root.title('Password Strength Finder')
wFont = font = dict(family='Courier New, monospaced',size=20, color='#7f7f7f')
wLabel = Label(root, text='Enter Password : ', font=wFont)
wLabel.grid(row=0,column=0)
wPassword = Entry(root, show='*')
wPassword.grid(row=0,column=1)

def checkStrength():
	strength = ['Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']
	score = 1
	pw = wPassword.get()
	
	if len(pw) == 0:
		psS.set(strength[0])
		return

	if len(pw) < 4:
		psS.set(strength[1])
		return

	if len(pw) >= 8:
		score += 1

	if re.search("[0-9]", pw):
		score += 1	

	if re.search("a-z", pw) and re.search("[A-Z]", pw):
		score += 1

	if re.search(".", pw):
		score += 1

	psS.set(strength[score])
	print(pw, score)

psS = StringVar()
checkBtn = Button(root, text="Check Strength", command=checkStrength)
checkBtn.grid(row=2,column=0)
checkLabel = Label(root, textvariable=psS)
checkLabel.grid(row=2,column=1,sticky=W)

root.mainloop()