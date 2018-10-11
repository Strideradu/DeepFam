with open("C:/Research/20181011_GPCR/trans.txt") as f:
    to_label = {}
    to_subfamily = {}
    to_family = {}
    for line in f.readlines():
        line = line.strip()
        sp = line.split()
        to_label[sp[1]] = int(sp[0])
        to_family[sp[1]] = sp[2]
        to_subfamily[sp[1]] = sp[3]

    print(to_label)
    print(to_family)
    print(to_subfamily)