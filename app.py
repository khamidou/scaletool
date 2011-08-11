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
		return handler

	def createWidgets(self):
		self.v = IntVar()
		for i, button in enumerate(scales):
			self.button = Radiobutton(self, text=str(button), command=self.closure(str(button)), 
						variable=self.v, value=i)
			self.button.deselect()
			self.button.grid(row=0, column=i)

class ModeFrame(Frame):
	scales = [	{"name": "Major", "formula" : [2, 2, 1, 2, 2, 2, 1], "chords": "I ii iii IV V vidim vii"},
			{"name": "Harmonic Minor", "formula" : [2, 1, 2, 2, 1, 3, 1]},
			{"name": "Natural Minor", "formula" : [2, 1, 2, 2, 1, 2, 2]},
		]

	def __init__(self, master=None, app=None):
		Frame.__init__(self, master)
		self.app = app
		self.grid()
		self.createWidgets(master)
		self.currentSelec = None
		self.poll()
	
	def closure(self, text):
		def handler():
			global current_scale, current_mode
			current_mode = modes[text]
			print "current scale %s, current mode %s" % (current_scale, current_mode)
			s = Scale(scale=current_scale, mode=current_mode)
			self.app.outputLabel.configure(text=str(s))
		return handler


	def createWidgets(self, master):
		self.listbox = Listbox(master)
		for scale in self.scales:
			self.listbox.insert(END, scale["name"])
		self.listbox.grid()
	
	def poll(self):
		# necessary because of a limitation
		# of tkinter

		global current_scale # ok, crappy design.
	        now = self.listbox.curselection()
	        #if now != self.currentSelec and now != ():
		if now != ():
			self.app.updateWidgets(self.scales[int(now[0])], current_scale)
	                self.currentSelec = now
		self.after(250,	self.poll)
	
	def update(self, currentSelection):
		# notify the parent class of the change
		# in the list
		return

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	
	def createWidgets(self):
		self.outputLabel = Label(self, text="Select a scale and a mode")

		self.scalesLabel = LabelFrame(self, text="Root note")
		self.scalesLabel.grid()
		self.scalesFrame = ScalesFrame(master=self.scalesLabel, app=self)

		self.modesLabel = LabelFrame(self, text="Scale")
		self.modesLabel.grid()
		self.modesFrame = ModeFrame(master=self.modesLabel, app=self)

		self.derivedChordsFrame = LabelFrame(self, text="Derived Chords")
		self.derivedChordsFrame.grid()
		self.derivedChordsLabel = Label(master=self.derivedChordsFrame,	text="ho")
		self.derivedChordsLabel.pack()

		self.outputLabel.grid()

		self.quitButton = Button(self, text="Quit", command=self.quit)
		self.quitButton.grid()
	
	def updateWidgets(self, currentListSelection, currentNote):
		s = Scale(currentNote, currentListSelection["formula"])
		self.outputLabel.configure(text=str(s))
		if "chords" in currentListSelection:
			self.derivedChordsLabel.configure(text=currentListSelection["chords"])

if __name__ == "__main__":
	root = Tk()
	app = Application(master=root)
	app.master.title("Scaletool")
	app.mainloop()
