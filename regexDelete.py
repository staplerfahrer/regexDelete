import glob, re, shutil, sys, os, os.path

def main(testing, arguments):
	print(arguments)

	if not testing:
		print('Delete mode.\n')
	else:
		print('Test mode.\n')

	patterns = [re.compile(argument, flags=re.IGNORECASE) for argument in arguments]

	allFiles = glob.glob("**/*", recursive=True)
	print(f'{os.getcwd()} contains {len(allFiles)} files and/or directories.')
	matchingPaths = [file for file in allFiles if any([pattern.search(file) for pattern in patterns])]

	for path in matchingPaths:
		print(path+' ', end='')
		if not testing:
			if os.path.isfile(path):
				try:
					os.remove(path)
					print('deleted.')
				except FileNotFoundError as fe:
					pass
				except Exception as e:
					print('NOT deleted. Error:')
					print(e)
			else:
				try:
					shutil.rmtree(path)
					print('deleted.')
				except FileNotFoundError as fe:
					pass
				except Exception as e:
					print('NOT deleted. Error:')
					print(e)
		else:
			print('matched.')

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage:\n'
				'regexDelete -t "test1.*\.jpg$"\n'
				'regexDelete -d "pattern1.*\.jpg$" "pattern2.*\.bmp$"')
		sys.exit()

	testing = not (sys.argv[1] == '-d')
	arguments = sys.argv[2:]

	main(testing, arguments)
