import os, shutil, regexDelete

shutil.rmtree('testTemp')
shutil.copytree('testSource', 'testTemp')
os.chdir('testTemp')
regexDelete.main(testing=False, arguments=['(temp\\\\|temporary|temp-)', '\\\\dir\\\\', 'cache2?\\\\'])