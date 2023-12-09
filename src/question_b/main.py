import question_b

filename = "stocklist.txt"
stock_dict = question_b.get_stock_list(filename)

bold = '\033[1m'
underline = '\033[4m'
normal = "\033[0;0m"

while True:
    print("Menu:")
    print("1 - Display stock purchase history")
    print("2 - Exit")
    option = str(input("Select option 1 or 2: "))

    while option not in ('1', '2'):
        option = input("Invalid option, Please select option 1 or 2: ")

    if option == '1':
        print("\nStock Purchase History")
        print("Symbol\tCompany Name")
        print(bold+"\nStock Purchase History")
        print(underline+"Stock\t"+normal+"      "+underline+bold+"Report"+normal)
        for symbol, stocks in stock_dict.items():
            print(f"{str(stocks.get_symbol()).ljust(8)}{stocks.get_company_name()}")
            print(f"{str(stocks.get_company_name()).ljust(14)}{stocks.get_symbol()}")
        print("")
    elif option == '2':
        print("Exiting Program")
        break

