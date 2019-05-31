def minmax(x,y):
    if (x<y):
        return x,y
    else:
        return y,x

x=10
y=5
minXY,maxXY=minmax(x,y)
print(minXY)
print(maxXY)
minXY,maxXY=minmax(y,x)
print(minXY)
print(maxXY)
