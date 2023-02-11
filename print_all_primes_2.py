print(2)
index = 3
while True:
    previous = 1
    current = 3
    for i in range(2,index):
        previous, current = current, (previous+current)%index
    print(f"{index}\n"*(current==1),end="")
    index+=2

