'''
Created by Seth Dryer
Version 0.1 ALPHA OCT 23, 2018
'''

import Tkinter
import tkFileDialog
import hashlib
import os
import datetime

def main():
	#call Tkinter for user input on file selection via GUI.
	Tkinter.Tk().withdraw() 
	
	#get current time for file name
	now = datetime.datetime.now().time() 
	current_time = now.strftime("%Y-%m-%d %H%M")
	filename = "md5-multiple-files_%s.txt" % current_time
	with open(filename, 'w') as file :
		file_path = tkFileDialog.askopenfilenames()
		print "	--------------------------------------------------------------------" + '\n'			
		print "All MD5s and files have been written to %s" % filename + '\n'
		for file_path in file_path:
				if os.path.isfile(file_path):
					open_file = open(file_path)
					file_content = open_file.read()
					#show user md5 of file
					md5_enc_data = hashlib.md5(file_content).hexdigest()
					print "File:", file_path
					print "The MD5:", md5_enc_data + '\n'
					file.write(md5_enc_data + ' ')
					file.write(file_path + '\n')
	print "	------------------------------------------------------------------------" + '\n'			
	print "All MD5s and files have been written to %s" % filename
if __name__ == "__main__":
    main()
	
