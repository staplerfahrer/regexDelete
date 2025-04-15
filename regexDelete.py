import re, shutil, sys, os, os.path, stat

from typing import List

def main(testMode, workingDir, arguments):
	print(f'Working directory: {workingDir}')

	if not testMode:
		print('Delete mode.')
	else:
		print('Test mode.')

	print('Regexes:')
	for a in arguments:
		print(a)

	patterns = [
		re.compile(argument, flags=re.IGNORECASE) 
	    for argument 
		in arguments]

	allObjects        = list()
	enumerationErrors = list()
	scandirRec(workingDir, allObjects, enumerationErrors)

	print(f'{workingDir} contains {len(allObjects)} file system objects.')

	matchingObjects = [
		fsObj for fsObj in allObjects 
		if any([pattern.search(fsObj.path) for pattern in patterns])]

	deleteCount = 0
	deletionErrors = list()
	# todo: count errors and exceptions
	# todo: os.scandir provides DirEntry objects with is_dir() and is_file() functions
	for fsObj in matchingObjects:
		try:
			print(fsObj.path, end=' ')
		except Exception as e:
			print('unprintable path', end=' ')
			deletionErrors.append(e)

		if testMode:
			print('matched.')
			continue #################################################

		try:
			if fsObj.is_dir():
				shutil.rmtree(fsObj.path, onerror=remove_readonly)
				print('deleted.')
				deleteCount += 1
			elif fsObj.is_file():
				os.chmod(fsObj.path, stat.S_IWRITE)
				os.remove(fsObj.path)
				print('deleted.')
				deleteCount += 1
			else:
				raise Exception(f'Not a directory or a file: {fsObj.path}')
				
		except FileNotFoundError as fe:
			deletionErrors.append(fe)
			print('not found.')
			print(fe)

		except Exception as e:
			deletionErrors.append(e)
			print('NOT deleted. Error:')
			print(e)
	
	print(f'Done. {deleteCount} objects deleted.')
	print(f'Errors while enumerating file system objects: {len(enumerationErrors)}')
	print(enumerationErrors)

def scandirRec(targetPath: str, output: List[os.DirEntry], errors: list):
	# add trailing slash
	if targetPath[-1:] != '\\':
		targetPath += '\\'

	try:
		entries = list(os.scandir(targetPath))
	except Exception as e:
		errors.append(e)
		entries = list()

	subDirs = [e.name for e in entries if e.is_dir()]

	#recursively scan directories
	[scandirRec(targetPath+d, output, errors) for d in subDirs]

	output += entries

def remove_readonly(func, path, excinfo):
	# from https://stackoverflow.com/questions
	# 	/1889597/deleting-read-only-directory-in-python
    os.chmod(path, stat.S_IWRITE)
    func(path)

if __name__ == '__main__':
	print('Regex Delete by Jacob Bruinsma, 2022-2025, v1.3\n'
			'Delete files and directories matching a Python regular expression.')

	if len(sys.argv) < 4:
		print('Command line arguments:\n'
				'-t or -d    -t = test mode, -d = delete mode\n'
				'"c:\\temp"   working directory\n'
				'"\\\\.*tmp$"  as many regex patterns as you like\n'
				'            regexes are case-insensitive\n'
				'            escape backslashes like below\n'
				'Examples:\n'
				'    regexDelete -t "c:\\temp" "test1.*\.jpg$" "\\\\temp" "\\\\cache\\\\\\\\"\n'
				'    regexDelete -d "c:\\temp" "pattern1.*\.jpg$" "pattern2.*\.bmp$"')
		sys.exit()

	testMode   = not (sys.argv[1] == '-d')
	workingDir = sys.argv[2]
	arguments  = sys.argv[3:]

	main(testMode, workingDir, arguments)
