array_1 = ["zero", "unu", "doua", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua", "zece", "unsprezece", "doisprezece", "treisprezece", "paisprezece", "cincisprezece", "saisprezece", "saptesprezece", "optsprezece", "nouasprezece"]
array_2 = ["douazeci", "treizeci", "patruzeci", "cincizeci"]
timpul =input("Ora = ")
ora, minute = timpul.split(':')
o = int(ora)
m = int(minute)
if o < 20:
    print(array_1[o], end='')
else:
    if int(ora[1]) > 0:
        print(array_2[int(ora[0])-2] + " si " +array_1[int(ora[1])], end='')
    else:
        print(array_2[int(ora[0])-2], end='')

if m < 20:
    print(array_1[m] +" minute", end='')
else:
    if int(minute[1]) > 0:
        print(array_2[int(minute[0])-2] + " si " +array_1[int(minute[1])] +" minute", end='')
    else:
        print(array_2[int(minute[0])-2] +" minute", end='')

