n,b=input().split()
char=abs(len(b)-len(n))
for g in range(len(n)):
  if(len(b)==1 and b[g] in n):
    break
  if(a[g]!=b[g]):
    char=char+1
print(char)
