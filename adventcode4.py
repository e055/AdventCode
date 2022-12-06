bb = []

with open('dane4.txt', mode='r') as f:
    content = []
    index = 1
    for line in f:
        b = line.strip().split(',')
        bb.append(b)
print(bb)
bb_ok = []
for pair in bb:
    c = [pair[0].split('-'), pair[1].split('-')]
    bb_ok.append(c)
print(bb_ok)

counter = 0
for x in bb_ok:
    if int(x[0][0]) <= int(x[1][0]):
        if int(x[0][1]) >= int(x[1][1]):
            counter += 1
        elif int(x[0][0]) >= int(x[1][0]):
            if int(x[0][1]) <= int(x[1][1]):
                counter += 1
    elif int(x[0][0]) >= int(x[1][0]):
        if int(x[0][1]) <= int(x[1][1]):
            counter += 1
print(counter)
