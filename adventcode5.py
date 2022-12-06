import re

contanair_holder = {
    1: 'LNWTD',
    2: 'CPH',
    3: 'WPHNDGMJ',
    4: 'CWSNTQL',
    5: 'PHCN',
    6: 'THNDMWQB',
    7: 'MBRJGSL',
    8: 'ZNWGVBRT',
    9: 'WGDNPL',
}
# print(contanair_holder)
bb = []
with open('dane5.txt', mode='r') as f:
    content = []
    index = 1
    for line in f:
        b = line.strip()  # .split(',')
        bb.append(b)
bb_ok = []
for pair in bb:
    c = re.sub(r'[movefromto ]', '', pair)
    bb_ok.append(c)
print(bb_ok)
print(int(bb_ok[0][0]))


def container_mover(b, a, c):
    container = contanair_holder[a]
    print(container)
    move = (container[-b:])
    # move = move[::-1]
    print(move)
    deleter = len(contanair_holder[a]) - b
    contanair_holder[c] = contanair_holder[c] + move
    contanair_holder[a] = contanair_holder[a][:deleter]
    print(contanair_holder[a])
    print(contanair_holder)

for i in bb_ok:
    l = len(i)
    if l == 3:
        a = int(i[0])
        b = int(i[1])
        c = int(i[2])
        container_mover(a, b, c)
    else:
        a = i[0:2]
        a_ok = int(a)
        b = int(i[2])
        c = int(i[3])
        container_mover(a_ok, b, c)
print(contanair_holder)
