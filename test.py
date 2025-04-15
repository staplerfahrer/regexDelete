import os, shutil, regexDelete, time

# shutil.rmtree('testTemp')
# shutil.copytree('testSource', 'testTemp')
# os.chdir('testTemp')

start = time.time()

regexDelete.main(testMode=True, workingDir='c:\\temp', arguments=['ROOT'])

# out = list()
# errors = list()
# regexDelete.scandirRec('c:\\', out, errors)
# print(len(out))
# print(len(errors))

elapsed = time.time() - start
print(f'took: {elapsed:.3f} s')
