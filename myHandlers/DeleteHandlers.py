from BaseHandler import BaseHandler
import torndb
import tornado.web
import os
from PIL import Image

class DeleteHandler(BaseHandler):
	def get(self, entry_id):
		user_id = self.current_user.id
		user_name = self.db.get("SELECT * FROM users WHERE id = %s", int(user_id)).name
		#print entry_id
		#print user_name
		if user_name == 'admin':
			entry = self.db.get("SELECT * FROM entries WHERE id = %s", int(entry_id))
			exe = 'DELETE FROM entries WHERE id = ' + entry_id
			# print entry.imgPaths
			# print entry.imageCount
			if entry.imageCount != 0:
				picPaths = entry.imgPaths.strip(' ').split(' ')
				i = 0
				while i < len(picPaths):
					filename = "./static/" + picPaths[i]
					#print filename
					if os.path.exists(filename):
						os.remove(filename)
						#print "delete"
					i += 1
			self.db.execute(exe)
			self.redirect("/")

	def  post(self):
		pass
		