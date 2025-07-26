N, G = input().split()
xi = set()

for i in range(int(N)):
    xi.add(input())
    
if G == 'Y':
    print(len(xi))
elif G == 'F':
    print(len(xi)//2)
else :
    print(len(xi)//3)