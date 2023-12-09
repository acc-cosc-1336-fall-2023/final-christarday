bold = '\033[1m'
underline = '\033[4m'
normal = "\033[0;0m" 

class Stock():
     __symbol = None
     __company_name = None
     def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

     def get_symbol(self):
        return self.__symbol

     def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stock1 = Stock('APL', 'Apple Inc')
    stock2 = Stock('CAT', 'Caterpillar')
    stock3 = Stock('EK', 'Eastman Kodak')
    stock4 = Stock('GOOG', 'Google')
    stock5 = Stock('MSFT', 'Microsoft')

    stock_dictionary = {
        stock1.get_symbol(): stock1.get_company_name(),
        stock2.get_symbol(): stock2.get_company_name(),
        stock3.get_symbol(): stock3.get_company_name(),
        stock4.get_symbol(): stock4.get_company_name(),
        stock5.get_symbol(): stock5.get_company_name()
    }

    print("\nStock Purchase History")
    print("Symbol\tCompany Name")
    print(bold+"\nStock Purchase History")
    print(underline+"Symbol\tCompany Name"+normal)
    for symbol, company in stock_dictionary.items():
        print(symbol.ljust(7), company)
    print("")

# Call the function to test
stock_purchase_history() 