input()
temps = map(int, input().strip().split(" "))
out = sum([temp < 0 for temp in temps])
print(out)