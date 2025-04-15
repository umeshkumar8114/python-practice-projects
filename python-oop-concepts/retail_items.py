# Umesh Kumar U95237454 (Navigator)
# Ebin Abraham U52630521 (Driver)
# ASSIGNMENT 7
# Participation % = 50/50
# Exercise (Retail items)

class Retail_Items:
    def __init__(self, type, amount, price):
        self.__type = type
        self.__amount = amount
        self.__price = price

    def __str__(self):
        strings = '{:<20}{:<10}${:<10}'.format(self.__type, self.__amount, self.__price)
        return strings


def main():
    item1_type = input("Name of item 1: ")  # asking user about  the data
    item1_amount = input("Amount of item 1: ")
    item1_price = input("Price of item 1: ")
    item1 = Retail_Items(item1_type, item1_amount, item1_price)  # creating a object item 1

    item2_type = input("Name of item 2: ")  # asking user about  the data
    item2_amount = input("Amount of item 2: ")
    item2_price = input("Price of item 2: ")
    item2 = Retail_Items(item2_type, item2_amount, item2_price)  # creating a object item 2

    print('Here\'s the summary of the items you added:')
    formatString = '{name:20}{amount:10}{price:10}'  # defining width for name,amount and price
    print(formatString.format(name='Name', amount='Amount', price="Price"))
    print('-' * 35)  # this will print the dash 35 times
    print(item1)
    print(item2)


main()
