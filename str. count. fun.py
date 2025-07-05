# string m count function ka mtlb hota h ki string me koi bi value kitni bar aai h uski value print hoti h 

str = "i am a student of b.tech and i am a full stack developer "

print(str.count("of")) #yha pr of ki value count hoke print hogi mtlb ki of kiti baar aaya h 

print(str.capitalize()) #yha pr string ki value ko captial kr dega 


print(str.endswith("developer")) # yha pr ending ki value ko end me developer h ya nhi ki check krega or print krega true of false

print(str.startswith("i am ")) # yha pr starting ki value ko start me i am h ya nhi check krega or print krega true of false 

print(str.isalnum()) # yha pr check krega ki starting me koi alphanumeric value h ya nhi mtlb ki string me koi number or letter dono h ya nhi or print krega true or false


print(str.isalpha()) # yha pr check krega ki string me koi alphabetic value h ya nhi mtlb ki string me sirf letter h or koi number nhi h or print krega true or false

print(str.isdigit()) #yha pr check krega ki string me koi digit value h ya nhi mtlb ki string me sirf number h or koi letter nhi h or print krega true or false

print(str.islower()) #yha pr check krega ki string me koi lower case value to h ya nhi mtlb ki string me sirf small letter h or koi capital letter nhi h or print krega true ya false 

print(str.isupper()) #yha pr check krega ki string me koi upper case valueto h ya nhi mtlb ki string me sirf captial letter h or koi small letter nhi h or print krega true or false

print(str.title()) #yha pr string ki value ko title case me convert krenga mtlb ki first letter ko captial kr dega or baki sab small letter me hoga

print(str.swapcase()) #yha pr string ki value ko swap case me convert krenga mtlb ki small letter ko captial or captial letter ko small letter me convert kr dega

print(str.replace("i am"," you are")) # yha pr string me i am ki jagah you are replace kr dega or print krega

print(str.split()) # yha pr string ko split kr dega mtlb ki space ke hisab se string ko alag alag list me convert kr dega or print krega 

print(str.find("student")) #yha pr string me student ki value ko find krega or uski index value ko print krega 

print(str.index("b.tech")) #yha pr string me b.tech ki value ko index krega or uski index value ko print krega 

print(str.join(["hello","world"])) #yha pr string me hello or world ko join kr dega mtlb ki dono ko space ke hisab se join kr dega or print krega 

