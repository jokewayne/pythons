# encoding = utf8

def WriteToFile(filename, data):
	# filename: Full path to file
	# data: data to be written to the szFile
	f = file(filename, 'a')
	f.write(data)
	f.close()