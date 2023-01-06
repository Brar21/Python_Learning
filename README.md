# Python_Learning


## Installation of Python in your System

1. go to website- ```www.python.org``` 
2. click on dowloads select you OS accordingly.
3. Download the latest version.
4. Open download file and follow the steps

# Install VSCode
 
1. go to website- ```www.code.visualstudio.com``` 
2. click on dowloads select you OS accordingly.
3. Download the latest version.
4. Open download file and follow the steps

***Open window.powershell***
   - ```python``` in powershell. then you will enter in python world.
   - ```exit()```  write in powershell you will come out from python.
   - for just check version of Python you installed just type ```python --version``` in powershell.
   - ```pip``` for just create python environment like- install,uninstall Packages. etc.
   - ```pip --version``` for check version and where our "pip" is installed.

# What is pyhton?
  ***Python is programing language which help us to communicate with computer or laptop even with any type of opreating system.
  It is very simple and easy to understand  like reading a simple "English". Python pseudo code nature make python easy to learn for non-codder to just start learning coding and machine learning***

# What is PIP?
  ***Pip is the package maneger for pyhton like Node or npm in package manager for javascript/Node.js.you can use pip to install packages or a module on your system.***

# what are Modules?
  ***Module is a file with code written by somebody else which you can import byt installing that module in you program using pip***

# Types of Modules?
   *** Built-in => which you during installation of python in your system.***
   *** External => which you have to install using "pip" in your system.***

***Simple example of Python working that is you can use pyhton as "Calculater"*** 
      ***REPl - Read Evaluate Print loop***

# Comments?
 *Basiclly developer use this for give instruction in code base. Comments will never show on Browser when we run file on web-browser.*
 *Comment can be single line or Multiple line*

# Key-Features of Python 
  - Easy to understand = Fast Development
  - Free and open source
  - Work with every Opreating system.
  - Enjoy workin with it.

# World best code we gonna written
  for Javascript we use console.log("Hello World")   ==> print("Hello World") for Python Language
  - for "run" pyhton we need just click on Run button.
  - External command for terminal ```python {file.name}``` you can use shortcut just write "pyhton" space you file names first letter -> "python h" then press tab it will auto-complete name and after getting name hit "Enter" button.

# Install Python Extension
  1. Open visual studion code.
  2. Click on "Extension" tab.
  3. Search "Python" in search-bar.
  4. Click on Install button.
  5. Congratulation! You done it.
  6. Final and last step select pyhton Interprater.

# Variables and Datatypes in Python
  *Variable is name given to value for storing in your program or with Declare a varible name with value you can use that anywher in that particuler file*
  *TO declare a variable name you have to follow set of Rules:*
  1. variable name can contain alphabet,numbers,underscore.
  2. variable name can never be start with number.
  3. variable name can only start with Alphabet.
  4. you can't give space inside variable name.

  ***Datatype in python- mostly used datatype are as following:-***
  *Integerns*
  *Floating point numbers*
  *Strings*
  *Boolean*
  *None*

  # Operators in Pyhton
    1. Arithmetic operators => "+,-,/,*" common examples.
    2. Assignment operators => "=,+=,-=" you will use in further steps.
    3. Comperison operators => "==,>,>=,<,<=,!=" for compare value and type also.
    4. Logical operators => "and,or,not" check logic in functions.

# type() functions and typecasting
  - if you have number in string and you want to add number in that string, Just put variable name as parameter in ```int(varibele.name)``` then string number will be convert in number or integer. But it is valid on number or integers.

# String
  *String is just a Datatype in Python*
  *You can write with three ways*
   1. Single quoted string -> course="Pyhton"
   2. Double quoted string -> language="Hindi"
   3. Triple quoted string -> easy='''Yes'''

# String Slicing
  - slice means chop into peaces "Simple words to make every single words as string you can use "Slicing" in pyhton.   

  *what you need to know for use slicing?*
  1. Index -> this is given by pyhton internaly to string characters.
  2. Length -> total words or characters in string is Length of that string.
  3. Example string="Varinder" print(name[0]) will print only first letter "V" of string.
  4. print(name[0:4]) will print "Vari" ii will print index-number=[0,1,2,3] not print 4 number because index=length-1.

***Can you use Negtive index number in Python?***
   - Answer is YES!. Mostly case where you can use this is when you have to print last Index of string but you don't know the length of string.
   1. Example= "print last index of this string"  --> you don't know the length then how print last[index]?
   2. Simple -> print(Example[-1])

***Can you skip the index number in Python?***
   - Answer is Yes. How! you are thinking about it...let understand with following example:
   1. Example= "Varinder"  --> skip "ar" and "nd"
   2. simple print(Example[0:7:3])  --> you will get "Vie".

# String functions in Python?
  - Find length of string using len(). "len" is nothing just short form of length.
  *syntax to write len function*
     print(len(name_of_string))   
  - To check string endwiths given entry or not (it will return true || false).   
  *syntax to use endswith function*
     print(string..endwith(given_value))
  - To count how words are present in string equal to given letter(value).   
  *syntax to write count function*
     print(variable_name.count(value_for_count))
  - To make first letter capital in string starting use Capital() function
  *syntax to write Capital() function*
     print(variable_name.capitalize()))
   - To Find word is present in string equal to given letter(value).   
  *syntax to write find() function*
     print(variable_name.find(value_for_count))   
     *it will provide first word index if more then 1 same words are present in string*
   - To Replace word is present in string equal to given letter(value).   
  *syntax to write replace() function*
     print(variable_name.replace(value_want_replace,value_want_after_replace))   
     *it will replace all words if more then 1 same words are present in string with new value*  

# Escape sequences characters
  1. Characters after "\" will come know as Escape sequence character
  *Example- \n,\t,\',\\ etc*

## Lists and tuples in Python
   -- List are basically set of values of any type. Any type menas it can be Strings, Boolean, Integers, Floating points etc.   
      ***Booleans list - [true,false,true]***
      ***Integers list - [1,2,3,45,6,8]***
      ***Strings list - ["Phython","Java","C#","Javascript"]***
      ***Floating points list - [0.35,1.52,35.89,1.105]***
  
  **List Indexing**
     -- Index is always same in every case:
      - it will start from number "0".
      - It will stop at length-1 index number.

   **Can change value of list**
     -- Answer is Yes!
     - a=[1,2,4,3]   --> for change value you index of that place where you want to change
     - a[2]=3        --> now  "4" will change with "3" 
     - a[3]=4        --> now  "3" will change with "4" 
    
   **Can string Functions can implemen in Lists?**
     -- Answer is Yes! but not all of them
        - Len() to find length of list.
        - Slicing also can be implement in list like "[0:4]"

# List  Methods
  *For more understand through examples check file "ListMethods.py"*
   -- .Sort(): for sorting of list in assending order.
   -- .reverse(): for sorting of list in desending order.
   -- .append(): for add someting in the end of list.
   -- .insert(): for add something on selected index value.
   -- .pop(): to delete value from list by index number or if not give any index number then last item will be deleted.
   -- .remove() to remove item by Value providing it.
```for more methods```

 <button><a href="https://docs.python.org/3/tutorial/datastructures.html"> Link for Method List</a></button>

# Tuples   
   *Immutable in nature->menas you can't make changes in it*
  -- Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.
      - Tuple types:
   1. t=() --> Empty tuple.
   2. t=(1,)  --> Tuple with Single element
   *Comma is must to declare tuple with single item*  

  ## Can you chnage values in tuple like you don in "List"
     -- No,you got an error because you read values from tuple but cannot chnage that value.
   *for more see practical check file "Tuples.py" code*
# Tuple Method
  -- To count how many time same word in tuple comes.
    *syntax for this function count()*
    - print(tuple.name(value_for_check))
  -- To first occurence of value in tuple.
    *syntax for this function count()*
    - print(tuple.index(value_for_check))

 <button><a href="https://data-flair.training/blogs/python-tuple/"> Link for Tupple More Information</a></button>


# Dictoinery and Sets in python

*Dictionary mean not Oxford dictionary*

  -- In simple mean you work with Javascript than you Know about "Objects". Object have "Key-value" pairs. Same in Python this known as "Dictionary".
   
   - More simplfy it than you can say "Key" is like when you search on google you write somthing in "input tag" that is key and anwser you get from in revert that is called "Value".

 **syntax**
   - Examples:
   1. dictionary={
    "name":"Varinder",
    "age":27,
    "developer":True,
    "project":[1,2,3,4,5]
   }    #name=key
        #Varinder=value
  *Data-Types you can put in Dictionary*
  1. Interger("int")
  2. Boolen ("bol")
  3.  String-Literal("str")
  4. List("lst")
  5. Dictionary("dic")   

# Properties of Python Dictionaries:
  - Unordered in manner
  - Mutable(you can change then according your need)
  - Indexed
  - Duplicasy is not allowed
  
# Distionary Methods:
  - For print all key in list manner:
    *print(Dictionary.name.keys())*
    this will all key of your "Dictionary" 
      1. can check type of keys?
        - Yes! very simple to check write code as show here "print(type(Dictionary.name.keys()))  
        - type= "dict_keys"
      2. can you print keys in list manner?
                - Yes! very simple to check write code as show here "print(list(Dictionary.name.keys()))  
   - For print all Values in list manner:
    *print(Dictionary.name.value())*
    this will all Value of your "Dictionary"  
       1. can check type of keys?
       - Yes! very simple to check write code as show here "print(type(Dictionary.name.values()))  
       - type= "dict_values"        
       2. can you print values in list manner?
                - Yes! very simple to check write code as show here "print(list(Dictionary.name.values()))   
    - For get in return list of (key,value) tuples
    *print(Disctionary.name.items())*

    - For update new key-value pair in dictionary
    newItem={
        "Mac-Book":"New_wish"
    }            
    *Dictionary.name(newitem)*
    *print(Dictionary.name(name_of_item))*

    - For get value of key you can use ".get()" 
    *print(Dicationary.name.get("key_name"))*
     but you may confuse here that you can value by simply write
     *print(Dictionary.name["key_name"])* then what is nee of ".get()" ?
     simple reason behind this if you don't have that "value" then ".get()" will show "NONE" where simple "["key_name"] will through error because in simple ["key_value"] you have take care that key-name should be there which you written there.


     <a href="https://docs.python.org/3/tutorial/datastructures.html#dictionaries">More Dictionary Methods</a>


# Set in Python
  ***Set is a Collection of non-repetitve elements*** 
   - for example check first example in "Set.py" file.
 *For more simply this You can say that "Sets" are data-types which contain only unique elements means value should be diffrent from each other*  

 
# Properties of Python Sets:
  - Unordered in manner
  - Immutable(you can't change then according your need)
  - Sets are unindexed(you can get them by index number)
  - Duplicasy is not allowed means you can't write same value more than one time.

# Sets Methods
  - ".Add()" to add element or value in sets
  *Set.name.add(value_or_elements) is syntax to use method*   
     -- You can't same element two or more time --
     -- You can't add list or dictionary in Sets --
     -- You can only add Immutable data-type like: "tuples" --
  - "Len()" to print length of Sets
  *print(len(Set.name)) is syntax to use methods*   
  - ".Remove()" from remove element from Sets
  *Set.name.remove(value_to_remove) os syntax to use method*
  - ".pop()" remove element from set and return that element
  *print(Set.name.pop()) is systax to use mehtod*
  - ".clear()" from clean that set or remove everything from Set
  *Set.name.clear() is syntax to use method*
  - ".Union() to get all elements present in both sets
  *is Syntax to use  method*
  - ".Intersection() to get "Same" elements present in both sets
  *is Syntax to use  method*

## Conditoional Experssion in Python

  -- Conditional experssions means when have some situation or condition to full fill "If" or "else" best example of this is you can read below:
   *when are in school in 10th standard you for "Iphone" to your "Dad" and he say if you "marks" is greater then 90% than you will get it or if you score are above 80% than you will get "Samsung". If your marks above 70% than "realme" or if you get below than 60% than "Chappal"*
   *this is called Conditional Expression*

  ***Syntax***
   - if(condition):
   print("yes")
   - else :
   print("no") 
   *one more syntax you that elif which means (else if). this is used when conditions are more then two* 
   - elif(condition):
        print("Maybe")

 # Relational operators
   - we already dicussed this here is some examples of relational operators:
   "==",">=","<=" etc.  

 # Logical operators   
   - logical operators operate on conditional statement example:
   "and", "or","not"
   1. "and"  if both conditions are true than it go inside if statement.
   2. "or" if from both condition one will be true than it will go inside the statement
   3. "not" is use to make true into false and false into true.

 ## IS or IN uses
   - you mostly gonna use if,elif or else but you should know about this things also
     what "Is" work for?
     what "In"  work for?

# Loops in Python
  - if you want print "Hello world" 1000 times than you will shock and start thinking like i have write code "print("hello world")" 
    1000 times. You answer is like "bhai mujhe nai sikhni yeh "coding-voding" main chla ghr bye!" 

  ***what is your reaction when i tell you that it can be done in two lines of code!!!***

  -- Yes Loops gonna help us in this work --

## Types of loops in Python
   1. while loop
   2. for loop

  # While loop -
    - Syntax of while loop is show  below:  

    While condition :  #loop will until it == true#
            #here we right body code of loop 

  # For loop -
    - Syntax of while loop is show  below:

    for ("name of initial value") in varibale or etc.
         for "total" in "table" :
                    print(total)          

## Range Function in Python
   - if you wanna print sequences of numbers than this will help you how? you wanna se than come to file name "Loops.py line no.46"                    