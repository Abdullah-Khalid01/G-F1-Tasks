import pyperclip
import keyboard

# Craete List as a buffer to store copied texts
txt_lst = []

# Open file and write message to idicate the start
with open('/home/abdullah/Documents/notes1.txt','a') as file:
    file.write("start: ")

#Call back function stores the text in the file
def append():

    #Define the txt_lst as global to retieve it's data
    global txt_lst
    print(txt_lst)

    #Write the txt_lst data into the file
    with open('/home/abdullah/Documents/notes1.txt','a') as file:  
        for txt in txt_lst:
            file.write(txt+'\n')

    #Clear the buffer for the upcoming operation        
    txt_lst=[]
    

#Define The hotkey, related to the required operation
keyboard.add_hotkey('ctrl + shift + d', append)

#Keep reading the Clipboard for new data
while 1:

    #Once new data is appended retrieve it    
    clip = pyperclip.waitForNewPaste()
    
    #Append this data to the buffer (txt_lst)
    txt_lst.append(clip)


