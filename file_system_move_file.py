import os
 
source = 'main2.txt'
destination = 'newmain.txt'
os.rename(source,destination)
print('source path rename to destination path successfully')