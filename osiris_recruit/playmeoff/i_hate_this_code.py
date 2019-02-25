import json

filename = 'ref.txt'
no_thanks = '00:00:00:00:00:00:00:00'
out = []
with open(filename, 'r') as f:
    for line in f:
        line = line.strip("\n")
        if line and line != no_thanks:
            out.append(line[6:8])




filename = 'reference'
with open(filename, 'r') as f:
    ref1 = f.readline()
    ref2 = f.readline()



lower_case = ref1[:-1]
upper_case = ref2[:-1]

print(lower_case)
print(upper_case)




vals = []
for i in range(len(out)):
    blabla1 = '00:' + out[i]
    blabla2 = '02:' + out[i]
    vals.append((blabla1, lower_case[i]))
    vals.append((blabla2, upper_case[i]))

print(vals)



with open('finally2.txt', 'w') as f:
    json.dump(vals, f)

