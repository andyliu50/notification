#!/usr/bin/env python3

'This is a module used to push notification.'

__author__ = 'Andy Liu'

import requests

class Notification:

	def __init__(self, title, message):
		self.title = title
		self.message = message

class IFTTT(Notification):
    
	def __init__(self, title, message):
		super().__init__(title, message)
		self.mykey = 'dVNxHrwtqldbtVk8OjbsDs'
		self.event = 'general'
		self.url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (self.event, self.mykey)
		self.values = {"value1":self.title, "value2":self.message}
	
	def send(self):
		requests.post(self.url, data=self.values)

if __name__ == '__main__':
	n = IFTTT('This is Title', 'This is message!')
	n.send()
	print(n.url)
	print(n.title)
	print(n.message)
	print(n.values)
