import glob, re, shutil, sys, os, os.path, stat

def main(testing, arguments):
	print(arguments)

	if not testing:
		print('Delete mode.\n')
	else:
		print('Test mode.\n')

	patterns = [re.compile(argument, flags=re.IGNORECASE) for argument in arguments]

	allFiles = glob.glob("**/*", recursive=True)
	currentWorkDir = os.getcwd()
	print(f'{currentWorkDir} contains {len(allFiles)} files and/or directories.')
	matchingPaths = [file for file in allFiles if any([pattern.search(file) for pattern in patterns])]

	for path in matchingPaths:
		path = f'\\\\?\\{currentWorkDir}\\{path}'
		print(path+' ', end='')
		if not testing:
			if os.path.isfile(path):
				try:
					os.chmod(path, stat.S_IWRITE)
					os.remove(path)
					print('deleted.')
				except FileNotFoundError as fe:
					print('"not found"!?')
				except Exception as e:
					print('NOT deleted. Error:')
					print(e)
			else:
				try:
					shutil.rmtree(path, onerror=remove_readonly)
					print('deleted.')
				except FileNotFoundError as fe:
					print('"not found"!?')
				except Exception as e:
					print('NOT deleted. Error:')
					print(e)
		else:
			print('matched.')

def remove_readonly(func, path, excinfo):
	# from https://stackoverflow.com/questions/1889597/deleting-read-only-directory-in-python
    os.chmod(path, stat.S_IWRITE)
    func(path)

if __name__ == '__main__':
	print('Regex Delete by Jacob Bruinsma, 2022\n'
			'Delete files and directories matching a Python regular expression.\n')
	if len(sys.argv) < 3:
		print('Usage:\n'
				'regexDelete -t "test1.*\.jpg$"\n'
				'regexDelete -d "pattern1.*\.jpg$" "pattern2.*\.bmp$"')
		sys.exit()

	testing = not (sys.argv[1] == '-d')
	arguments = sys.argv[2:]

	main(testing, arguments)
