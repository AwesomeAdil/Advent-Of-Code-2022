from aocd import get_data
cur = 0
all = []
input_data = get_data(day=1, year=2022).split('\n')
for x in input_data:
    if x == "":
        all.append(cur)
        cur = 0
    else:
        cur += int(x)
all.append(cur)
all.sort()
print(sum(all[-3:]))

