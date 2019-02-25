import json

with open('finally2.txt', 'r') as f:
    vals = json.load(f)


something = []
with open('hello.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and line != '\n':
            something.append(line)

whatever = []
for i in range(len(something)):
    if something[i][:2] != '02':
        for j in range(0, len(vals), 2):
            if ((vals[j][0][3:] == something[i][6:8]) and something[i][9:11] == '00'):
                whatever.append(vals[j][1])
            if ((vals[j][0][3:] == something[i][9:11]) and something[i][6:8] == '00'):
                whatever.append(vals[j][1])
    else:
        for j in range(1, len(vals), 2):
            if ((vals[j][0][3:] == something[i][6:8]) and something[i][9:11] == '00'):
                whatever.append(vals[j][1])
            if ((vals[j][0][3:] == something[i][9:11]) and something[i][6:8] == '00'):
                whatever.append(vals[j][1])

print("".join(whatever))

