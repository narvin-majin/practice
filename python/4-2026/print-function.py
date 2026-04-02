n = int(input())
    
for i in range(1,n+1):
    print(i,end='')

#print(*objects, sep=' ', end='\n') print syntax
#print(1, 2, 3, sep="-", end=" END")


print(*range(1, n+1), sep="")

#here * mean unpack value

#range(stop) ,range(start, stop), range(start, stop, step) same as indexing

#2026-04-01 | print funcion hr | solved | 15min | edge case solved | narvin