import os
if (not os.path.exists('seektellfunctions')):
    os.mkdir('seektellfunctions')

with open('seektell.txt','w') as w:
    text = w.write("Scarnon Mate, What are you up to")

with open('seektell.txt','r') as r:
    readingText = r.read()
    print(readingText)

print("Current Working Directory:", os.getcwd())


#seek and tell functions 

with open('seektell.txt','r') as f:
    f.seek(10) #starts fron 10th index
    text=f.read(5) #read 5 characters
 
    print(text)

#truncate function

with open('truncate.txt','w') as t:
    t.write('Hello world')
    t.truncate(5) #makes the text file of 5 characters

with open('truncate.txt','r') as t:
    text=t.read()
    print(text)