# --------------------------------
# copyfile() = copies contents of a file
# copy() = + permission mode , destination can be a directory
# copy2() = + copies metadata (file creation time & modification time)
# --------------------------------
import shutil
# --------------------------------
original_file = '/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/testfile1.txt'
new_file = '/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/lib/testfile1.txt'
# --------------------------------
# shutil.copyfile('notes.txt','copy.txt')
shutil.copy2(original_file,new_file)
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------