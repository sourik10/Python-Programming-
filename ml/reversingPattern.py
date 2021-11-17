n=int(input())
ans=1
for i in range(1,n+1):
    if(i%2==1):     #oddRow(1,3,5)
        for j in range(1,i+1):
            print(ans,end=" ")
            ans+=1
        ans=ans+i
    else:            #evenRow(2,4,6)
        for j in range(1,i+1):
            print(ans,end=" ")
            ans-=1
        ans=ans+i+1
    print()
