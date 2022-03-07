# --------------------------------
# copyfile() = copies contents of a file
# copy() = + permission mode , destination can be a directory
# copy2() = + copies metadata (file creation time & modification time)
# --------------------------------
import os, shutil
# --------------------------------

original_file = '/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/archive/'
new_file = '/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/lib/'


# --------------------------------
# shutil.copyfile('notes.txt','copy.txt')
# shutil.copy2(original_file,new_file)
shutil.copyfile(original_file,new_file)


# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------
# --------------------------------