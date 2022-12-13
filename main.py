def biggestNumber(txt):
    with open(txt, "r") as f:
        a = [int(x) for x in f.readlines()]
    return max(a)

add = biggestNumber('file.txt')
with open('file.txt', 'a') as f:
    f.write(str(add))