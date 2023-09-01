array = [0, 0, 0, 0, 0]
print("Input 5 numbers in random order")
for x in range(0, 5): #user enters numbers
	num = int(input("Enter integer: "))
	array[x] = num

sort = False #flag
passes = 0
print(array)
while sort == False:
    sort = True
    for i in range(0, len(array) - 1):
        temp = array[i + 1] #store next value in temp variable
        if array[i] > array[i + 1]: #compare
            array[i + 1] = array[i] #swap if next value is smaller
            array[i] = temp
            sort = False #set flag to false
        print(array)
    if sort == False:
        passes = passes + 1
        print("pass", passes)
    else:
        print("list sorted: ")
        print(array)
    

    
