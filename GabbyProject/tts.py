import playsound
import pyttsx3;
engine = pyttsx3.init();
import json

def scan():
    f = open('data.json',)
    
    data = json.load(f)
    
    # Iterating through the json
    # list
    b_dict = list()
    b_adv_dict = list()
    for i in data['b_dict']:
        for e in i:
            b_dict.append(e)
            b_dict.append(i[e])


    for i in data['b_adv_dict']:
        for e in i:
            b_adv_dict.append(e)
            b_adv_dict.append(i[e])
    return b_dict,b_adv_dict
def write_json(name,message, section,filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        bum = file_data[section][0]
        bum[name] = message
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def call(inp):
    b_dict, b_adv_dict = scan()
    if "NewButton" in inp:
        trashvar, inp = inp.split('[')
        inp.replace(']','')
        name,message = inp.split(',',1)
        message,trash = message.split(',')
        write_json(name,message,'b_dict')
    elif "NewScreen" in inp:
        temp = inp
        trashvar, temp = temp.split("[")
        name,location = temp.split(',')
        button_obj = '''<button class="button1" onclick='send("''' +name +'''")',style="height: 80%; width: 80%;"/>'''+name+'''</button>'''
        print(button_obj)
        templist = list()
        outfile = list()
        with open(location) as file:
            for line in file:
                templist.append(line.rstrip())
        for i in range(len(templist)):
            outfile.append(templist[i])
            if templist[i] =='<div>':
                outfile.append(button_obj)
        with open(location, 'w') as fi:
            for line in outfile:
                fi.write(line +'\n')
            
    elif inp != '':
        for i in range(len(b_dict)):
            if inp == b_dict[i]:
                
                if "Songs" in b_dict[i+1]:
                    playsound.playsound(b_dict[i+1])
                else:
                    engine.say(b_dict[i+1])
                    engine.runAndWait()
            else:
                print(inp)
                print(b_dict[i])
        for i in range(len(b_adv_dict)):
            if inp in b_adv_dict[i]:
                    engine.say(inp)
                    engine.runAndWait()

        
'''
voices = engine.getProperty('voices')
#1,7,10,
engine.setProperty('voice', voices[].id) #change index to change voices
engine.say('I\'m a little teapot...')

engine.runAndWait()
'''