f = open('contador.txt', 'r')
squares, cubes, fourths = [], [], []
for line in f.readlines():
    print(line)
f.close()