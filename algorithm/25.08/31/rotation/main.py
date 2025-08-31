aaa = [[1,2,3],[4,5,6],[7,8,9]]

print (*aaa)

a = list(map(list, zip(*aaa)))
print (*a)
b = list(zip(*aaa[::-1]))
print (*b)
c = list(zip(*aaa))[::-1]
print (*c)