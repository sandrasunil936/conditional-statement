# string 
# sequence of series can be any characters etc
# represented as ',"","'"

name = "mohan"
print (name)
print (type (name ))

date = "mohan's resume"
qt = '''gandhi once said that "say no to violence" '''
print (qt) 

# escape sequence 
# \'--'
# \n - newline 
# \t - tab space 
# \b - backspace 
# \\ - consider as a string

date = "mohan's resume"
qt = "gandhi\b on\tce said \nthat\"say no to violence\" " 
print (qt)

date = "mohan's resume"
qt = "gandhi\b on\tce said \\n that\"say no to violence\" " 
print (qt)

# raw string - to avoid escape sequence 

date = "mohan's resume"
qt = r"gandhi\b on\tce said \nthat\"say no to violence\"" 
print (qt)

# input function - python ask input to the user at the runtime
# input function always returns a string that is even if,
# the user write a numbr python treat it as a text 
a = "44"
b = "55"
print (a+b)

a = int (input('enter a number'))
b = int (input('entrt an another number'))
print (a + b)

a = float(input('enter a number'))
b = float (input('enter an another number'))
print (a + b)

print (type(a))
print (type(b))

a = "mohan"
b = "das"
print (a+' '+b)

# string formating 

name = "sandra"
age = 25
marriedstatus = "false"
rating = 4.9
result = f"my name is {name},my age is {age},my marriedstatus is {marriedstatus},my rating is {rating}"
print (result)