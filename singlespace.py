import clipman as pyperclip

pyperclip.init()

text = pyperclip.paste()

text = text.replace("\r\n\r\n","\n")

print(text)

pyperclip.copy(text)
