1. Read a string statement from the command line in python:

    step 1: Enter your name locally and enter key on your keyboard it will print the entered name    
       
       str=input("Enter your name")
       print(str)

2. Findout total number of characters present in the statement:

    Step 1: By passing the len() function, it will return the number characters in integer.
         
         str="abc"
         print(len(str))

3. Findout toal number of duplicate Characters in the statement:

    Step 1: create a string

         str="madam"

     Step 2: create a empty list to store a values

         dup=[]

     Step 3: Loop over each letters in a string

         for i in str:

     Step 4: Check if letters appears more than once and if not already in the duplicate list

         if str.count(i)>1 and i not in dup:

     Step 5: Append the letters to the duplicate list and print the duplicate list

         dup.append(i)
         print(dup)
   
4. Findout total number of words present in the statement:

     Step 1: Enter a string and store it ina variable

           str ="god is great"

     Step 2: character count variable is initialized to zero and word count variable is initialized to 1.

           char=0
           word=1

     Step 3: for loop is used to traverse through character in a string

           for i in str:

     Step 4: The character count is increamented each time and the word count is increamented when the space is encountered.

            char=char+1
            if(i==' '):
               word=word+1
       
     Step 5: Print the total no of char and words present in the string.

             print(char)
             print(word)

5. Findout toal number of duplicate wordsin the statement:

     Step 1: Enter the string and store it in one variable. Split the stored variable and store it into another variable.
             create an empty list to store the string and assign duplicate count value as 0.

             str = "i am not a robot to do all i am human"
             str1 = str.split()
             dup = []
             dup_count = 0

     Step 2: For loop is used to traverse the spiltted string. And check if the word already not present in duplicate list append the
             i value into the list.

             for i in str1:
                 if i not in dup:
                     dup.append(i)

     Step 3: Otherwise increase the count of duplicate value.
 
                 else:
                     dup_count = dup_count+1

6. Reverse the characters present in the statement:
   
     Step 1: Enter a string and store into one variable. create one empty string.

              str = "hello"
              empty_str = " "

    Step 2: Used for loop to traverse the string into character. 

              for i in str:
                 empty_str = i+empty_str
              print(empty_str)

7. Reverse the word present in the statement:

    Step 1: Enter a string and store into variable.create one empty string to store the reversed word

              str = "hi welcome"
              str1 = str.split()
              empt_str = ""
              for i in str1:
                   empt_str = i + "" +empt_str
              print(empt_str)

8. Form a new statement from the reversed words:

           reversed_words  = "ognam tae"
           new_statement = reversed_words
           print("New statement from reversed words:", new_statement)

9. Remove the duplicate characters from the latest statement:

           reversed_words  = "ognam tae"
           emp = ""
           for i in reversed_words:
               if i not in emp:
                  emp+=i
           print(emp)  


#######################################################################################################################################################################

                                                           Task 2: 
Write a Python program to validate the entered email address if the email is valid then write into a file. Continue this operation until uses says No/exit. 
If user says Yes continue Validating emails and writing into file
If user says No then display all the email IDs from the file.
Note: Regex should be for validation.

import re


while True:

    user = input("Enter the user choice yes or no").lower()


#If the user says it will show previous stored email id's

    if user =='no':
        file = open('email_txt.txt','r')
        print(file.read())

#Or else if the user says yes yu have to enter the valid email pattern and we should search that email id into entered email id


    elif user =='yes':
        user = input("Enter the valid email id").lower()
        pattern = r"^[A-Za-z][A-Za-z0-9]+@[A-Za-z]+\.[a-zA-Z]+$"
        out = re.search(pattern,user)

#If that pattern searched means we should write and group the email id and read that email.


        if out:
            fw = open('email_txt.txt','a')
            fw.write(out.group()+'\n')
            fw.close()
            file = open('email_txt.txt','r')
            print(file.read())



     
   

   
        
      
