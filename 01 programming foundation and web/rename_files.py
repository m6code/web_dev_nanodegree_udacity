import os


def rename_files():
	# 1 get file names from folder
	file_list = os.listdir(
		r"C:\Users\Benjamin_PC\web_dev\webdev Nanodegree_Udacity\01 programming foundation and web\prank")
	print file_list  # Print the list of files in the directory
	saved_path = os.getcwd()  # save the current working directory
	# change the current working directory
	os.chdir(r"C:\Users\Benjamin_PC\web_dev\webdev Nanodegree_Udacity\01 programming foundation and web\prank")

	# 2 rename files in directory
	for fname in file_list:
		os.rename(fname, fname.translate(None,"0123456789"))
	os.chdir(saved_path)  # Change back to current work directory

rename_files()
