def mult_table(n):
    for i in range(1, 11):
        print(f"{i} * {n} = {i * n}")

if __name__ == '__main__':
    number = float(input("Enter number to generate multiplication table: "))
    mult_table(number)