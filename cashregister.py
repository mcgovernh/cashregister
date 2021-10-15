class switcher(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switcher.value for arg in args))

def menu():
    print("**** Cash Register Program ****")
    print("To get options type \"0\"")
    print("To quit type \"exit\"")
    print("To cash out type \"total\"")
    print("To cancel out type \"cancel\"")

total = 0
price = 0
tendered = 0

while True:
    menu()
    while True:
        print("Sub total is ", round(total,2))

        price = float(input("Enter the price for next item:"))

        total = total + price

        if(price == 0):
            break
    choice = input("Enter option:")

    while switcher(choice):
        if case("cancel"):
            total = 0
            print("You have cancelled your transaction!")
            break
        if case("exit"):
            print("Goodbye")
            break
        if case("total"):
            print("Your total is ", round(total,2))
            tendered = float(input("How much tendered?"))
            if (total - tendered) > 0:
                print("I need another ",round((total-tendered),2))
            elif (total - tendered) < 0:
                print("Your change is ", round(-(total-tendered),2))
            break
        break
    choice = input("Another Go Y/N:")
    if choice.upper() == "Y":
        total = 0
        continue
    else:
        break
    break
