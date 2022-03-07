# /usr/bin/python3
# -----imports---------------------------
from os import system
# -----say-----------------------------------------------------------
text="Hello World"
def my_text(text):
    system("say {}".format(text))
my_text(text)
# ----------------------------------------------------------------
