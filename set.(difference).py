x = int(input())
math = set(map(int,input().split())) 
y = int(input())
science = set(map(int,input().split()))
print(len(math - science))
