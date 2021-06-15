with open("24-j9.txt") as F:
  s = F.readline() # считали строку

def isPalindrome( startPos, L ):
  endPos = startPos + L - 1
  while startPos < endPos:
    if s[startPos] != s[endPos]:
      return False
    startPos += 1
    endPos -= 1
  return True

L = 5
cnt = 0
for i in range(len(s)-L):
  if isPalindrome(i, L):
    cnt += 1

print( cnt )




