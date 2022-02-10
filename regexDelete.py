import glob, re, shutil, sys, os, os.path

if len(sys.argv) < 3:
	print('Usage:\nregexDelete -t "test1.*\.jpg$"\nregexDelete -d "pattern1.*\.jpg$" "pattern2.*\.bmp$"')
	sys.exit()

testing = not (sys.argv[1] == '-d')
arguments = sys.argv[2:]

print(arguments)

if not testing:
	print('Delete mode.\n')
else:
	print('Test mode.\n')

patterns = [re.compile(argument, flags=re.IGNORECASE) for argument in arguments]

allFiles = glob.glob("**/*", recursive=True)

matchingPaths = [file for file in allFiles if any([pattern.search(file) for pattern in patterns])]

for path in matchingPaths:
	print(path)
	if not testing:
		if os.path.isfile(path):
			os.remove(path)
		else:
			try:
				shutil.rmtree(path)
			except FileNotFoundError as fe:
				pass
			except Exception as e:
				print(e)
