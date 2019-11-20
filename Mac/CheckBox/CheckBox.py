from tkinter import Frame, Label
from PIL import ImageTk, Image

class CheckBox():
	def __init__(self, window, font = ['verdana', 15], binding = False):
		self.window = window
		self.gfont = font
		self.display = False
		self.checked = False
		self.binding = binding

	def loadimage(self, image = 'uncheck'):
		if image == 'uncheck':
			self.image = ImageTk.PhotoImage(Image.open('src/uncheck.png'))
		else:
			self.image = ImageTk.PhotoImage(Image.open('src/check.png'))
		return self.image

	def create(self, text = 'Check me out'):
		self.checkFrame = Frame(self.window)
		self.checkBox = Label(self.checkFrame, image = self.loadimage())
		self.checkLabel = Label(self.checkFrame, text = text)

		self.bindings()
		self.configs()

	def configs(self):
		self.checkFrame.config(bg = 'white')
		self.checkBox.config(bg = 'white')
		self.checkLabel.config(bg = 'white', font = self.gfont)

	def bindings(self):
		if( self.binding ):
			self.checkFrame.bind('<Button-1>', self.customBinding)
			self.checkBox.bind('<Button-1>', self.customBinding)
			self.checkLabel.bind('<Button-1>', self.customBinding)
		else:
			self.checkFrame.bind('<Button-1>', self.toggle)
			self.checkBox.bind('<Button-1>', self.toggle)
			self.checkLabel.bind('<Button-1>', self.toggle)

	def customBinding(self, event):
		self.toggle(event)
		self.binding(event)

	def packings(self, framePackings):
		self.checkFrame.pack(framePackings)
		self.checkBox.pack(side = 'left')
		self.checkLabel.pack(side = 'left')

	def check(self):
		if self.checked == False:
			self.checkBox['image'] = self.loadimage('check')
			self.checked = True

	def toggle(self, event = None):
		if self.checked == True:
			self.uncheck()
		else:
			self.check()

	def uncheck(self):
		if self.checked == True:
			self.checkBox['image'] = self.loadimage()
			self.checked = False

	def show(self, framePackings = {'fill': 'x'}):
		if self.display == False:
			self.packings(framePackings)
			self.display = True

	def hide(self):
		if self.display == True:
			self.checkFrame.pack_forget()
			self.display = False

# if __name__ == '__main__':
# 	root = Tk()
# 	root.config(bg = 'white')
# 	root.geometry('700x600')

# 	frame = Frame(root)
# 	frame.config(bg = 'white')
	
# 	check = CheckBox(window = frame)
# 	check.create()
# 	check.show()

# 	frame.pack(fill = 'both', expand = True)
# 	root.mainloop()