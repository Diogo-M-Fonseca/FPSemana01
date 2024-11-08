ch1 = str(input("Character one name: "))
hp1=int(input("Health points: "))
lvl1=int(input("Level: "))
ch2 = str(input("Character two name: "))
hp2=int(input("Health points: "))
lvl2=int(input("Level: "))
ch3 = str(input("Character three name: "))
hp3=int(input("Health points: "))
lvl3=int(input("Level: "))


print(ch1)
print(hp1)
print(lvl1)
print(ch2)
print(hp2)
print(lvl2)
print(ch3)
print(hp3)
print(lvl3)

conjunto =[
    [ch1,(hp1,lvl1)],
    [ch2,(hp2,lvl2)],
    [ch3,(hp3,lvl3)]
]

print(conjunto)

def arrumação_characterlvl(conjunto):
    for i in range(len(conjunto)):
        for j in range(0,len(conjunto)-i-1):
            if conjunto[j][1][1]<conjunto[j+1][1][1]:
                conjunto[j],conjunto[j+1] = conjunto[j+1], conjunto[j]
arrumação_characterlvl(conjunto)

for i in conjunto:
    print(i[0])