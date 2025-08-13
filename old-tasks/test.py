

text = "   welcom to python programing    "

text = text.strip()

print(text)

text = text.lower()

print(text)



text = input("enter the name").replace( "python" , "java" , count=1 )
print(text)

print(len(text))

# /////////////////////////////////////////////////////////////


name = input("enter your name: ")

name = name.title()
if name.startswith("eng"):
    print("hello engineer"+ name[3:])


