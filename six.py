# control statements
#basically looping - 2 types while ,for
#while condition :
  #code to be executed
# while loop execute till the condition become false 

i = 1
while i<=100:
    print (i)
    i = i + 1
print ("mohan")  

# sum of first 10 numbers

i = 1
sum = 0
while i<=10:
    sum = sum + i
    print (sum)
    i = i + 1

i = 1
esum = 0
osum = 0

while i<=100:
    if i % 2 ==0:
        esum = esum + i
    else:
        osum = osum + i
    
    i = i + 1
    print (esum)
    print (osum)


