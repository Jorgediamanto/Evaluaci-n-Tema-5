f = open('contador.txt', 'r')

for line in f.readlines():
    print(line)

f.close()

while True:
    x = input("inc -para incrementar , dec - para disminuir: ")

    if x == "inc":
        f = open('contador.txt', 'r')

        for line in f.readlines():
            xx = line
            
        
        open('contador.txt', 'w').close()
        with open('contador.txt', 'w') as file:
            file.write(str(int(xx)+1))

        f = open('contador.txt', 'r')
        for line in f.readlines():
            print(line)
        f.close()

    elif x == "dec":
        f = open('contador.txt', 'r')

        for line in f.readlines():
            xx = line

        open('contador.txt', 'w').close()
        with open('contador.txt', 'w') as file:
            file.write(str(int(xx)-1))

        f = open('contador.txt', 'r')
        for line in f.readlines():
            print(line)
        f.close()

    else:
        break