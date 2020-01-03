import win32gui
import win32con
import json
import time
import requests
import urllib
from threading import Thread
from re import search, sub, I, escape

def jsonize (string):
	jsonData = json.loads(string)
	return jsonData

def unjsonize (json_data):
	string = json.dumps(json_data, indent = 4)
	return string
	
def loadJson (path):
	with open(path, "r") as file:
		data = json.load(file)

		return data

def saveJson (path, data):
	with open(path, "w") as file:
		json.dump(data, file, indent = 4)

def putContentIn (filePath, data):
	with open(filePath, "w") as file:
		file.write(data)

def getContentOf (filePath):
	with open(filePath, "r") as file:
		return file.read()

def getContentOfBinary (filePath):
	with open(filePath, "rb") as file:
		return file.read()

def setImmediate (method, args = {}):

	def _method (method, arguments):
		operation = method(**arguments)

	immediateObj = Thread(target = _method, args = (method, args))
	immediateObj.start()
	return immediateObj

def setTimeout (method, secs = 5, args = {}):

	def _method (method, arguments, secs):
		time.sleep(secs)
		operation = method(**arguments)

	timeoutObj = Thread(target = _method, args = (method, args, secs))
	timeoutObj.start()
	return timeoutObj

def setInterval (method, secs = 10, args = {}):
	def _method (method, arguments, secs):
		while True:
			time.sleep(secs)
			operation = method(**arguments)

			if operation == "end" or operation == "break":
				break

	intervalObj = Thread(target = _method, args = (method, args, secs))
	intervalObj.start()
	return intervalObj

def clearTimeout (timeoutObject):
	pass

def clearInterval (intervalObject):
	clearTimeout(intervalObject)

def httpPost (url, postData = {}):
	req = requests.post(url, data = postData)

	return req.text

def httpGet (url, getData = {}):
	req = requests.get(url, data = postData)

	return req.text

def exp (num1, num2):
	return num1 ** num2

def swapQuotes (txt):
	matchObj = search(r"'", txt, I)
	if matchObj:
		ntxt = sub(r"'", '"', txt)
		return ntxt
	else:
		return txt

def downloadFile (url, filename):
	return urllib.urlretrieve(url, filename)

def searchString (string, regex, ignoreCase = False):
	if ignoreCase:
		match = search(r"%s" % regex, string, I)
	else:
		match = search(r"%s" % regex, string)
		
	return match

def wait (secs):
	time.sleep(secs)

def hideWindow ():
	program = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(program, win32con.SW_HIDE)

def showWindow ():
	program = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(program, win32con.SW_SHOW)