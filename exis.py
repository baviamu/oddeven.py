u1,u2=map(int,input().split())
sorc=list(map(int,input().split()))
for v in sorc:
	if(v==u2):
		print("yes")
		break
else:
	print("no")
