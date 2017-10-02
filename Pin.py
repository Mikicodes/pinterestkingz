class Pin:
<<<<<<< HEAD
	#Construct a Pin for use
	def __init__(self):
=======
	#Construct a pin
	def __init__(self):
# 		self.name = name
# 		self.picture = picture
		self.description
		self.posting_date
>>>>>>> eced91dbde459f139206221edbb8319ae7a4a5b7
		self.comments = []

	#Reassign Name of Pin
	def set_name(self,name):
		self.name =name

	#Get Name of the Pin
	def get_name(self):
		return self.name

	#Reassign Description of the pin
	def set_description(self, descriptione):
		self.description =description

	#Get the description of the pin
	def get_decription(self):
		return self.description

	#Get the picture of the pin
	def get_picture(self):
		return picture

	#Set date and time of posting of the the pin
	def set_posting_date(self, posting_date):
		self.posting_date = posting_date

	#Return date and time of posting of the pin
	def get_posting_date(selfs):
		return posting_date

	#Add a comment to a pin
	def set_comments(self, comment):
		self.comments.append(comment)

	#Return comments of the pin
	def get_comments(self):
		return self.comments