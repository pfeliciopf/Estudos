fat = [1]*21
for i in range(1, 21):
    fat[i] = fat[i-1] * i 

T = int(input())

for _ in range(T):
    N, K= map(int, input().split())
    K-=1

    disponiveis = list(range(1, N+1))
    permutacao = []

    for i in range(N, 0, -1):
        f = fat[i-1]
        pos= K//f
        K%=f

        permutacao.append(disponiveis.pop(pos))

    print(*permutacao)
