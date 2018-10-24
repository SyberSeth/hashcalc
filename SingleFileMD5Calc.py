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
	now = datetime.datetime.now()
	current_time = now.strftime("%Y-%m-%d %H%M")
	filename = "md5-single-file_%s.txt" % current_time
	with open(filename, 'w') as file :
		file_path = tkFileDialog.askopenfilename()
		open_file = open(file_path)
		file_content = open_file.read()
		#show user md5 of file
		md5_enc_data = hashlib.md5(file_content).hexdigest()
		print "file:", file_path
		print "The MD5:", md5_enc_data + '\n'
		file.write(md5_enc_data)
		file.write(file_path)
		print "NOTE: the following has been written and saved to the following file %s" % filename
	
if __name__ == "__main__":
    main()
	
