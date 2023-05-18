# 파이썬 코드를 임시로 실행하는 곳입니다.
a=int(input())
b=[]
for j in range(2,a):
    if j==2:
        b.append(j)
        continue
    is_prime = True
    for i in range(2,j):
        if j%i==0:
            is_prime = False
            break
    if is_prime== True:
        b.append(j)
print(sum(b))
