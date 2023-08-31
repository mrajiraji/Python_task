import re
while True:
    user = input("Enter the user choice yes or no").lower()
    if user =='no':
        file = open('email_txt.txt','r')
        print(file.read())
    elif user =='yes':
        user = input("Enter the valid email id").lower()
        pattern = r"^[A-Za-z][A-Za-z0-9]+@[A-Za-z]+\.[a-zA-Z]+$"
        out = re.search(pattern,user)
        if out:
            fw = open('email_txt.txt','a')
            fw.write(out.group()+'\n')
            fw.close()
            file = open('email_txt.txt','r')
            print(file.read())
