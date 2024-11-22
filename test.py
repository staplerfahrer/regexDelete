import os, shutil, regexDelete, time

# shutil.rmtree('testTemp')
# shutil.copytree('testSource', 'testTemp')
# os.chdir('testTemp')
# regexDelete.main(testing=False, arguments=['(temp\\\\|temporary|temp-)', '\\\\dir\\\\', 'cache2?\\\\'])

out = list()
errors = list()

start = time.time()
regexDelete.scandirRec('c:\\', out, errors)
elapsed = time.time() - start
print(f'took: {elapsed} s')
print(len(out))
print(len(errors))
