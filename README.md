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
   
     
   

   
        
      
