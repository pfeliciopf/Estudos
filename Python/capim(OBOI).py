n = int(input())
s= input()

soma =0 
count = {0 : 1}
resposta=0

for c in s:
    soma += 1 if c == '1' else -1
    if soma in count:
        resposta+= count[soma]
        count[soma] +=1
    else:
        count[soma] =1

print(resposta)

