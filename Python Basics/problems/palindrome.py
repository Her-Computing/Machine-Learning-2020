def palindrome(number):
  string_num = ""

  for i in str(number):
    string_num = i + string_num 
  
  if string_num == str(number):
    return True
  else:
    return False

palindrome_num = palindrome(3334)
print(palindrome_num)

#extra solutions
'''
def isPalindrome(s): 
  string = str(s)
  
  #returns reverse of string
  if string == string[::-1]:
    return True
  else:
    return False

s = "12121121212121"
ans = isPalindrome(s) 
print(ans)

x = "malayalam"
w = "" 
for i in x: 
  print(i)
  w = i + w 
  #print(w)
  if (x==w): 
      print("YES") 
'''