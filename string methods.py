# string are immutable
a="Abhishek kumar"
b="Abhishek kumar!!!!!!!!"
c="Abhishek kumar!!!!!!!!!abhi"
d="Abhishek kumar !!!! Abhi"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(b.rstrip("!"))
print(c.replace("abhishekkumar","abhi"))
print(d.split(" "))

blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "Welcome to the Console  !!!"
print(len(str1))
print(len(str1.center(50)))

e="Abhishek !!!!! Abhishek !!!! Abhishek"
print(e.count("Abhi"))

#endswith
str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))

str2 = "she's name is kallo. She is an honest woman"
print(str2.find("is"))
print(str2.endswith("is"))
print(str2.startswith("she"))
print(str2.startswith("is")) 

# "index"= error produce
print(str2.find("ishh"))
# print(str2.index("ishh"))     #this line given error

#ISALNUM() = The Isalnum() method returns true only if the entire
# only consists of A-Z , a-z , 0-9.If any other charaters or punctuations
# are present, then it returns false

str3 = "WelcomeToTheConsole"
print(str3.isalnum())
str3 = "welcome99"    #FALSE
print(str3.isalpha())

str4 = "hello world"
print(str4.islower())



str5 = "We wish youn a Meery Christmas\n"
print(str5)
print(str5.isprintable())



str6 = "      "      #using spacebar
print(str6.isspace())
str7 = "  "        #using tab
print(str7.isspace())





str8 = "World Health Organization"
print(str8.istitle())



str9 = "To Kill a Mocking Bird"
print(str9.istitle())


str10 ="python is a Interpreted language"
print(str10.startswith("python"))
print(str10.endswith("python"))


str11 ="python is a Interpreted language"
print(str11.swapcase())


str12 = " He's name is a Deepanshu. Deepanshu is an honest men"
print(str12.title())




#OUTPUT print line by line

# Abhishek kumar
# 14
# ABHISHEK KUMAR
# abhishek kumar
# Abhishek kumar
# Abhishek kumar!!!!!!!!!abhi
# ['Abhishek', 'kumar', '!!!!', 'Abhi']
# Introduction to js
# 27
# 50
# 3
# True
# 11
# False
# True
# False
# -1
# True
# False
# True
# We wish youn a Meery Christmas

# False
# True
# True
# True
# False
# True
# False
# PYTHON IS A iNTERPRETED LANGUAGE
#  He'S Name Is A Deepanshu. Deepanshu Is An Honest Men