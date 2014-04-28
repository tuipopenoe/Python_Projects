def listDirectory(directory, fileExtList):
	"""Get a list of file info objects for files of particular extensions"""
	fileList = [os.path.normcase(f) for f in os.listdir(directory)]
	# Gets a list of the full pathnames of alll the files in a drietory
	fileList = [os.path.join(directory, f) for f in fileList \
	 if os.path.splitext(f)[1] in fileExtList]

	 def getFileInfoClass(filename, \
	 	module=sys.modules[FileInfo.__module__]):
	 	"""Get file info class from filename extension"""
	 	# Gets the extension of the file and constructs class name
	 	subclass = "%sFileInfo" % \
	 		os.path.splitext(filename)[1].upper()[1:]
	 		# Check if handler class exists in this module
	 	return hasattr(module, subclass) and \
	 		getattr(module, subclass) or FileInfo
	 return[getFileInfoClass(f)(f) for f in fileList]