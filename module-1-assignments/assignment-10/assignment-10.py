def palinedrome(string):
    if string[0:int(len(string)/2)] == string[int(len(string)/2)+1:][::-1]:
        return True
    else:
        return False

x = input("Enter string : ")
if palinedrome(x):
    print ("Yes, it is a palindrome.")
else:
    print("not palindrome")