#Reverse an integer:
n = 12345
rev=0   
while(n>0):
    dig=n%10 #gets last digit
    rev=rev*10 + n%10 #adds a power of ten and sets equal to last digit
    n=n//10
print(n, " reversed ", rev)

#Reverse a string:
print("hello world reversed ", 'hello world'[::-1])
