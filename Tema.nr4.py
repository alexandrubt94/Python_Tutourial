a = input()
vector = []
i = 0


while int(a) != -1:
    vector.append(int(a))
    a = input()
print(min(vector))
print(max(vector))