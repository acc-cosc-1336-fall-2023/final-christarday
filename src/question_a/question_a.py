#write functions here, don't add input('') statements here!

def create_multiplication(x, y):
    table = []

    for i in range(1, x + 1):
        row = []

        for j in range(1, y + 1):
            product = i * j
            row.append(product)
        table.append(row)

    return table

def display_table(table):
    for i in range(len(table)):
        print('')
        for j in range(len(table[i])):
            print(str(table[i][j]).ljust(4), end=' ')
        print('')

def display_menu():
    print("1 - Create Multiplication Table")
    print("2 - Exit")

def run_menu():
    display_menu()
    option = str(input("Select option 1 or 2: "))
    while option not in ('1', '2'):
        option = input("Invalid option, Select 1 or 2: ")

    run_option(option)

def run_option(option):
    if option == '1':
        option_1()
    elif option == '2':
        option_2()

def option_1():
    while True:
        try:
            row = int(input("Select number of rows for your table: "))
            break
        except ValueError:
            print("Invalid input, Please enter a whole number")
    while True:
        try:
            column = int(input("Select number of columns for your table: "))
            break
        except ValueError:
            print("Invalid input, Please enter a whole number!")
    table = create_multiplication(row, column)
    display_table(table)
    option = str(input("If you would like to create another table, press Y. Otherwise, enter any other key to exit: ")).lower()
    if option in ('y', 'yes'):
        option_1()
    else:
        option_2()

def option_2():
    print("Exiting Program")

if __name__ == "__main__":
    run_menu()


        