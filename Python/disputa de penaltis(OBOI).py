#obzYDGV

N, v1, v2, d1, d2=map(int, open(0).read().split())

time1pv= (N - d1)> v2
time2pv= (N - d2)> v1

print("S" if time1pv else "N")
print("S" if time2pv else "N")
