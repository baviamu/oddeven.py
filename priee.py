hei=int(input())
for r in range(2,hei):
    if hei%r==0:
        print("no")
        break
else:
    print("yes")
