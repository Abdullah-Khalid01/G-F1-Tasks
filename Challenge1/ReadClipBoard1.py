import pyperclip
from pynput import keyboard

# Craete List as a buffer to store copied texts
txt_lst = []

# Open file and write message to idicate the start
with open('/home/abdullah/Documents/notes3.txt','a') as file: 
    file.write("start: \n")

#Call back function stores the text in the file
def append():

    #Define the txt_lst as global to retieve it's data
    global txt_lst
    print(txt_lst)

    #Write the txt_lst data into the file
    with open('/home/abdullah/Documents/notes3.txt','a') as file:
        for txt in txt_lst:
            file.write(txt+'\n')

    #Clear the buffer for the upcoming operation 
    txt_lst=[]

def copy():
    print('copied')
    global txt_lst
    txt_lst.append(pyperclip.paste())


#Define The hotkeys, related to the required operation and callback functions
#ctr + c --> call the (copy) function which stores the data into the buffer (txt_lst)
#ctrl + shift + d call the (append) function which writes the data stored in the buffer to the file
with keyboard.GlobalHotKeys({
    '<ctrl>+<shift>+d': append,
    '<ctrl>+c':copy}) as h:
 h.join()

