#leet speak function
def l337encodes(s):
    #capitalizes every letter
    s = s.upper()
    #replaces following letters
    s = s.replace("A","4")
    s = s.replace("B","8")
    s = s.replace("E","3")
    s = s.replace("L","1")
    s = s.replace("O","0")
    s = s.replace("S","5")
    s = s.replace("T","7")
    #prints final string
    print(s)

s = "bob is an elite haxor"
l337encodes(s)    