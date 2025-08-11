num=int(input("Enter the number of heights:"))
heights=[int(input(f"Enter the {i+1} height:"))for i in range(num)]
print(heights)
ans=0
lmax=[0]*num
rmax=[0]*num
lmax[0]=heights[0]
rmax[num-1]=heights[num-1]
for i in range(1,num):
    lmax[i]=max(lmax[i-1],heights[i])
for i in range(num-2,-1,-1):
    rmax[i]=max(rmax[i+1],heights[i])
for i in range(0,num):
    ans+=(min(lmax[i],rmax[i]))-heights[i]
print(ans)