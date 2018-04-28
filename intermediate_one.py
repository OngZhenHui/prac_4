def main():
    number_list = []
    for i in range(5):
        number = int(input("Enter number {}: ".format(i + 1)))
        number_list.append(number)
    print("The first number is", number_list[0])
    print("The last number is", number_list[-1])
    print("The smallest number is", min(number_list))
    print("The largest number is", max(number_list))
    print("The average of the numbers is", sum(number_list) / len(number_list))


main()