import Tkinter
import tkFileDialog
import hashlib
import os
import datetime

def main():
	#call Tkinter for user input on file selection via GUI.
	Tkinter.Tk().withdraw() 
	
	print "Please select two md5 files to compare"
	file1 = tkFileDialog.askopenfilename()
	file2 = tkFileDialog.askopenfilename()
	f1_line = file1.readline()
	f2_line = file2.readline()
		#keep track of lines read in file
	line_counter=1
		#visually show which files are being compared
	print("Now comparing files", file1, "and", file2)
		# Loop if either file1 or file2 has not reached EOF
'''
	while f1_line != '' or f2_line != '':
		if f1_line != f2_line:
			if f2_line == '' and f1_line != '':
				print(">+", "Line-%d" % line_no, f1_line)
		else f1_line != '':
				print(">", "Line-%d" % line_no, f1_line)
					
		f1_line = file1.readline()
		f2_line = file2.readline()
			
		line_counter += 1
'''
		
if __name__ == "__main__":
    main()