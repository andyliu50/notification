#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This is a module used to communicate with IFTTT platform.'

__author__ = 'Andy Liu'

import requests

class Notification(object):
    
	mykey = 'dVNxHrwtqldbtVk8OjbsDs'
	def __init__(self, event, **values):
		self.url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, self.mykey)
		self.report = values
	
	def sent(self):
		requests.post(self.url, data=self.report)

if __name__ == '__main__':
	n = Notification('op-answers', value1 = 'answer1', value2 = 'answer2', value3 = 'answer3')
	n.sent()
