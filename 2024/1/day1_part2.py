def main():
    list1 = []
    list2 = []
    distance = 0
    with open("./2024/1/inputs/input.txt") as f:
        for line in f:
            num1, num2 = line.split()
            list1.append(int(num1))
            list2.append(int(num2))
    
    for num in list1:
        distance += num * list2.count(num)

    print(distance)

main()