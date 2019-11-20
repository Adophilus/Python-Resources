import sys
from PIL import ImageGrab
from time import sleep

class ScreenshotTaker():
	def __init__ (self, delay, path = "./"):
		this.delay = delay
		this.path = path

	def takeScreenshot (self):
		image = ImageGrab.grab()

	def saveScreenshot (self, image):
		with open(self.path, "w") as screenshotFile:
			screenshotFile.write(image)

if __name__ == "__main__":
	try:
		camera = ScreenshotTaker(sys.argv[1], sys.argv[2])
	except Exception as e:
		camera = ScreenshotTaker(sys.argv[1])