def main():
    list1 = []
    list2 = []
    distance = 0
    with open("./2024/1/inputs/input.txt") as f:
        for line in f:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
    
    while(len(list1) != 0):
        min1 = min(list1)
        min2 = min(list2)
        distance += abs(min1 - min2)

        list1.remove(min1)
        list2.remove(min2)

    print(distance)

main()