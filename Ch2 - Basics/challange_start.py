
text=""

def polidromtest(text):
    y=""
   
    for x in text:
        if x.isalnum():
            y=y+x
    test=True
    rev=y[::-1]
    for i,b in enumerate(y):
       
        if rev[i]!=b:
            print("Is palindrom:",False)
            test=False
            break
            
    if test:
        print("Polindrom!")

        
    

while text != "exit":
    
    text =input ("Enter palindrome or 'exit':")
    text=text.lower()
    if text=="exit":
        break
    else: 
        polidromtest(text)
