import Tkinter
import tkFileDialog
import hashlib
import os
import datetime
import difflib

def main():
	#call Tkinter for user input on file selection via GUI.
	Tkinter.Tk().withdraw() 
	
	print "Please select two md5 files to compare"
	file1 = tkFileDialog.askopenfilename()
	file2 = tkFileDialog.askopenfilename()
	with open(file1) as f1:
			f1_data = f1.read()
	with open(file2) as f2:
			f2_data = f2.read()
	print "Any differences in MD5s between files will be displayed below. A blank output means no changes"
# Find and print the diff:
	for line in difflib.unified_diff(f1_data, f2_data, fromfile = 'file1', tofile='file2', lineterm=''):
		print line
		
		
if __name__ == "__main__":
    main()