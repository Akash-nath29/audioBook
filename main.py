#Audio Book made using Python
#---------------------------------------------------
#
#Author: Akash Nath (https://tinyurl.com/akash-nath)
#
#----------------------------------------------------

import pyttsx3
import fitz

doc = fitz.open('books/Rich_Dad_Poor_Dad.pdf')
text = ""
for page in doc:
    text += page.get_text()
print(text)
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
