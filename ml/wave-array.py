 #2d List in Pyhton
l=[ [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
  ]
print(l)

#Number of rows
print(len(l)) 
#Number of columns 
print(len(l[0]))
row=len(l)
col=len(l[0])

#wave form print
for(j in range(col):
    if(j%2==0):
        for(i in range(row):
            print(l[i][j],end=" ")
    else:
        for(i in range(row-1,-1,-1)):
            print(l[i][j],end=" ")
            
