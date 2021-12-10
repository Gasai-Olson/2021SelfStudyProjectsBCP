
def write(arg):
    f = open('/Users/timyc1/Desktop/houseofrep/Output.txt','w') 
    f.write(arg)

def take_note(arg):
    f= open('/Users/timyc1/Desktop/houseofrep/Output.txt','r')
    s = f.readlines()
    s.append(arg)
    write(str(arg)+' : Written to file')