#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'This is a module used to communicate with IFTTT platform.'

__author__ = 'Andy Liu'

import requests

class Notification(object):
    
	mykey = 'dVNxHrwtqldbtVk8OjbsDs'
	def __init__(self, event, **values):
		self.__url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, self.mykey)
		self.__values = values
	
	def sent(self):
		requests.post(self.__url, data=self.__values)

	@property
	def url(self):
		return self.__url

	@property
	def values(self):
		return self.__values

if __name__ == '__main__':
	n = Notification('op-answers', value1 = 'answer1', value2 = 'answer2', value3 = 'answer3')
#	n.sent()
	print(n.url)
	print(n.values)
