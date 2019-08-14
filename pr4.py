b1,c2=map(str,input().split())
yas=0
if len(b1)>len(c2):
  b1,c2=c2,b1
p=0
while p<len(b1):
  yas+=(ord(c2[p])-ord(b1[p]))
  p+=1
for p in range(p,len(c2)):
  yas+=ord(c2[p])-ord('a')+1
print(yas)
