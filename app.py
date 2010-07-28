#!/usr/bin/env python

from Tkinter import *
from scales import *

current_scale = "C"
current_mode = "C"

class ScalesFrame(Frame):
	def __init__(self, master=None, app=None):
		Frame.__init__(self, master)
		self.app = app
		self.grid()
		self.createWidgets()
	
	def closure(self, text):
		def handler():
			global current_scale, current_mode
			current_scale = text
			print "current scale %s, current mode %s" % (current_scale, current_mode)
			s = Scale(scale=current_scale, mode=current_mode)
			self.app.outputLabel.configure(text=str(s))
		return handler

	def createWidgets(self):
		for i, button in enumerate(scales):
			self.button = Radiobutton(self, text=str(button), command=self.closure(str(button)))
			self.button.deselect()
			self.button.grid(row=0, column=i)

class ModeFrame(Frame):
	def __init__(self, master=None, app=None):
		Frame.__init__(self, master)
		self.app = app
		self.grid()
		self.createWidgets()
	
	def closure(self, text):
		def handler():
			global current_scale, current_mode
			current_mode = modes[text]
			print "current scale %s, current mode %s" % (current_scale, current_mode)
			s = Scale(scale=current_scale, mode=current_mode)
			self.app.outputLabel.configure(text=str(s))
		return handler


	def createWidgets(self):
		for i, button in enumerate(modes):
			self.button = Radiobutton(self, text=str(button), command=self.closure(str(button)))
			self.button.deselect()
			self.button.grid(row=0, column=i)


class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	
	def createWidgets(self):
		self.outputLabel = Label(self, text="Placeholder")

		self.scalesLabel = LabelFrame(self, text="Scale")
		self.scalesLabel.grid()
		self.scalesFrame = ScalesFrame(master=self.scalesLabel, app=self)

		self.modesLabel = LabelFrame(self, text="Modes")
		self.modesLabel.grid()
		self.modesFrame = ModeFrame(master=self.modesLabel, app=self)


		self.outputLabel.grid()

		self.quitButton = Button(self, text="Quit", command=self.quit)
		self.quitButton.grid()

if __name__ == "__main__":
	root = Tk()
	app = Application(master=root)
	app.master.title("Scaletool")
	app.mainloop()
