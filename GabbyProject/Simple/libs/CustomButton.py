import bs4
import tkinter as tk
window = tk.Tk()
 
import json

def addLog(title, message, image):
    with open('Simple/libs/data.json', 'r') as openfile:
        data = json.load(openfile)
        data[title] = [message, image]
    with open("Simple/libs/data.json", "w") as outfile:
        json.dump(data, outfile)
    updateLog(title)
def removeLog(title):
    with open('Simple/libs/data.json', 'r') as openfile:
        data = json.load(openfile)
    variable2.set("None")
    data.pop(title)
    menu2['menu'].delete(title)

   
    
        
    print(data)
    with open("Simple/libs/data.json", "w") as outfile:
        json.dump(data, outfile)
 
def pullLog():
    with open("Simple/libs/data.json", 'r') as openfile:
        return json.load(openfile)
def updateLog(title):
    menu2['menu'].add_command(label=title, command=tk._setit(variable2, title))


    


paths = {'Activities Board': "Simple/Activity.html",
         'Drink Menu': "Simple/Drink.html",
         'Food Menu': "Simple/Eat.html",

         'Food and Drink Board': "Simple/Food.html",
         'Home': "Simple/Home.html"}
k = list(paths.keys())
variable = tk.StringVar(window)
variable.set(k[0]) # default value

output = tk.Label(text = "")


titleLabel = tk.Label(text = "Title")
messageLabel = tk.Label(text = "Message")
imgLabel = tk.Label(text = "Image Name")

entryTitle=tk.Entry()
entryMessage=tk.Entry()
entryImg=tk.Entry()
menu = tk.OptionMenu(window,variable, *k)

data = pullLog()
k2 = list(data.keys())
variable2 = tk.StringVar(window)
variable2.set("None") # default value
print('|•/||••|/|||||•|•|•|')
menu2 = tk.OptionMenu(window,variable2, *k2)


def changeFileAdd(title, message, image, pathway):
    with open(pathway) as inf:
        txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")

    str1 = soup.contents
    print(str1)
    str2 = str1[0].__str__().split("</body>", 1)
   
    data = str2[0] + "<button onclick=\"send('"+message+"')\" class=\"button1\"><img src=\"imgs/Custom/"+image+"\" style=\"height: 80%; width: 80%;\"/><br>"+title+"</button>" +"\n</body>"+ str2[1]
    print(data)
    soup2 = bs4.BeautifulSoup(data, features="html.parser")

    with open(pathway, "w") as outf:
        outf.write(str(soup2))

def handle_clickAdd(event):
    message = entryMessage.get()
    title = entryTitle.get()
    image = entryImg.get()
    pathway = paths[variable.get()]
    print(title, message, image, pathway)
    changeFileAdd(title, message, image, pathway)
    output.config(text = "Button Successfully Added!")
    addLog(title, message, image)


def changeFileRemove(title, message, image, pathway):
    with open(pathway) as inf:
        txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    string = "<button class=\"button1\" onclick=\"send('"+message+"')\"><img src=\"imgs/Custom/"+image+"\" style=\"height: 80%; width: 80%;\"/><br/>"+title+"</button>"
    print(string)
    str1 = soup.contents
    str2 = str1[0].__str__().split(string, 1)

    data = str2[0] + str2[1]
    print(data)
    soup2 = bs4.BeautifulSoup(data, features="html.parser")

    with open(pathway, "w") as outf:
        outf.write(str(soup2))

def handle_clickRemove(event):
    title = variable2.get()
    message = pullLog()[title][0]
    image = pullLog()[title][1]
    pathway = paths[variable.get()]
    print(title, message, image, pathway)
    changeFileRemove(title, message, image, pathway)
    output.config(text = "Button Successfully Removed!")
    removeLog(title)

button = tk.Button(text="Add")

button.bind("<Button-1>", handle_clickAdd)
button2 = tk.Button(text="Remove")
print('2.19.7D5')
button2.bind("<Button-1>", handle_clickRemove)
output.pack()
menu.pack()
titleLabel.pack()
entryTitle.pack()
messageLabel.pack()
entryMessage.pack()
imgLabel.pack()
entryImg.pack()
button.pack()
menu2.pack()
button2.pack()




window.mainloop()