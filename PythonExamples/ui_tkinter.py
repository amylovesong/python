#!/usr/bin/env python
# -*- coding: utf-8 -*-

'User Interface exercise use the third mudule：Tkinter'

__author__ = 'sunxiaoling'

from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()

class ApplicationInput(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)

#app = Application()
app = ApplicationInput()
#窗口标题
app.master.title('Hello World')
#主消息循环
app.mainloop()


