num_1 = float(input("Enter a number"))
num_2 = float(input("Enter another number"))
choice = input("Enter the operation = + - * / :")
if choice == "+":
    sum = num_1 + num_2
    print("The sum is", sum)
elif choice == "-":
    diff = num_1 - num_2
    print("The diff is", diff)
elif choice == "*":
    mul = num_1 * num_2
    print("The mul is", mul)
elif choice == "/":
    div = num_1 / num_2
    print("The div is", div)
else:
    print("Invalid")