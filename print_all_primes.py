previous = 1
index = 2
current = 3

while True :
    if (current-1)%index==0:
        print(index)
    current, previous = current + previous, current
    index+=1
