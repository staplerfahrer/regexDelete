import glob, re, shutil, sys, os, os.path, stat

def main(testing, arguments):
	print('Arguments:')
	for a in arguments:
		print(a)

	if not testing:
		print('Delete mode.\n')
	else:
		print('Test mode.\n')

	patterns = [
		re.compile(argument, flags=re.IGNORECASE) 
	    for argument 
		in arguments]

	currentWorkDir = os.getcwd()

	allFiles = \
		glob.glob("**/*", recursive=True) \
		+ glob.glob(".**/*", recursive=True) \
		+ glob.glob("**/.*", recursive=True)

	print(f'{currentWorkDir} contains {len(allFiles)} files and/or directories.')

	matchingPaths = [path 
		  for path in allFiles 
		  if any([pattern.search(path) for pattern in patterns])]

	for path in matchingPaths:
		try:
			path = f'\\\\?\\{currentWorkDir}\\{path}'
			print(path.encode('utf-8'), end=' ')
		except Exception as e:
			print(e)
			continue #################################################

		if testing:
			print('matched.')
			continue #################################################

		try:
			if os.path.isdir(path):
				shutil.rmtree(path, onerror=remove_readonly)
			elif os.path.isfile(path):
				os.chmod(path, stat.S_IWRITE)
				os.remove(path)
			print('deleted.')
		except FileNotFoundError as fe:
			print('not found.')
			print(fe)
		except Exception as e:
			print('NOT deleted. Error:')
			print(e)
	
	print('Done.')

def remove_readonly(func, path, excinfo):
	# from https://stackoverflow.com/questions
	# 	/1889597/deleting-read-only-directory-in-python
    os.chmod(path, stat.S_IWRITE)
    func(path)

if __name__ == '__main__':
	print('Regex Delete by Jacob Bruinsma, 2022\n'
			'Delete files and directories matching a Python regular expression.\n')
	if len(sys.argv) < 3:
		print('Usage:\n'
				'regexDelete -t "test1.*\.jpg$" "\\\\TEMP"\n'
				'regexDelete -d "pattern1.*\.jpg$" "pattern2.*\.bmp$"')
		sys.exit()

	testing = not (sys.argv[1] == '-d')
	arguments = sys.argv[2:]

	main(testing, arguments)
