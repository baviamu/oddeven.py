o1,o2=map(int,input().split())
cnt=0
arr=list(map(int,input().split()))[:o1]
for d in arr:
  if d==o2:
    cnt+=1
print(cnt)
