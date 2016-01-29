class main (object):
	def __init__(self, images, phrases):
		self.listeImage = images
		self.phrases = phrases
		self.ImgPhr = []

	def getImages (self):
		return self.listeImage

	def getCommentaire (self):
		return self.phrases

	def AssocieImgPhr (self):
		for i in range(len(getImages())):
			self.ImgPhr.append({img:getImages() [i], getCommentaire() [i]})

	def getImgPhr (self):
		return self.ImgPhr
