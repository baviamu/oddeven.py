bav=int(input())
u=0
e=0
while(bav>0):
    e=bav%10
    u=u+e
    bav=bav//10
print(u)
