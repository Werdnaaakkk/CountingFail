IP = list(map(int, input().split())) # input
count = 0
for i in IP:
    if i < 60:
        count += 1
print(count)
