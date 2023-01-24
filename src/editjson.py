import json
def main():
    data = json.load(open("./data.json"))
    running = True
    while running:
        print("\nSelect a category to edit:")
        print_info(data)

        ch = input(
                "Enter index - edit category \n"+
                "a - add a category \n"+
                "c - change order \n"+
                "x - delete \n"+
                "q - exit \n>")

        if ch == 'a':
            new = {}
            new['name'] = input("The new category's name:\n>")
            new['products'] = []
            data.append(new)

        elif ch == 'c':
            print("Select a category to move:\n")
            print_info(data)

            ans1 = int(input("Index of item to be moved:\n"))
            ans2 = int(input("New index of item (others will be offset):\n"))

            item = data.pop(ans1)
            # print(data)
            if ans1 < ans2:
                ans2 -= 1
            data.insert(ans2, item)
            # print(data)

        elif ch == 'x':
            print("Select a category to delete:\n")
            print_info(data)

            ans1 = int(input("Index of item to be deleted:\n"))
            item = data.pop(ans1)

        elif ch == "q":
            running = False

        else:
            try:
                i = int(ch)
                enterCategory(i, data)
            except Exception as e:
                print()
                print(e)
                print("Please enter a number between 0-" + str(len(data)-1))
                print()

    print_info(data)
    if input("Save changes? (y/n)") == "y":
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)

def editProduct(cat):
    print("Select a product to edit:")
    print_info(cat['products'])

    ch = int(input("Choose a product:\n>"))
    product = cat['products'][ch]

    attr_list = list(product.keys())

    for i, p in enumerate(attr_list):
        print(str(i) + ": " + p + " - " + str(product[p]))
    inp = int(input("Choose an attribute:\n"))

    attr= attr_list[inp]
    t = type(product[attr])
    if t == type(True):
        v = input("Toggle bool? (y/n)\n") == "y"
        # a lil xor
        a = product[attr]
        product[attr] = not a if v else a
    elif t == type(0.1):
        num = float(input("What should the value be changed to?\n"))
        product[attr] = num
    elif t == type(1):
        num = int(input("What should the value be changed to?\n"))
        product[attr] = num
    elif t == type(""):
        num = input("What should the value be changed to?\n")
        product[attr] = num
    else:
        print(product[attr].__class__(), "has not been coverd")

def enterCategory(categoryIndex, data):
    cat = data[categoryIndex]
    running = True
    while running:
        print("You chose the category: ", cat['name'])
        print_info(cat['products'])

        print("What do you want to do?")
        inp = input(
                "a - add a product \n"+
                "e - edit\n"+
                "c - change order \n"+
                "m - move to other category\n"+
                "x - delete\n"+
                "q - back\n>")

        if inp == "a":
            cat['products'].append(addProduct(data))

        elif inp == "e":
            editProduct(cat)

        elif inp == "c":
            print("Select a product to move:")
            print_info(cat['products'])

            ans1 = int(input("Index of item to be moved:\n"))
            ans2 = int(input("New index of item (others will be offset):\n"))
            l = cat['products']
            item = l[ans1]
            l.remove(item)
            if ans1 < ans2:
                ans2 -= 1
            l.insert(ans2, item)

        elif inp == "m":
            print("Select a product to move:")
            print_info(cat['products'])
            ans1 = int(input("Index of item to be moved:\n"))
            print_info(data)
            ans2 = int(input("Select a category to move to:\n"))
            l= cat["products"]
            item = l[ans1]
            l.remove(item)
            data[ans2]["products"].insert(ans2, item);

        elif inp == "x":
            print("Select products to delete:")
            print_info(cat['products'])
            ans1 = input("Index of items to delete (seperate with spaces): ").split()

            l = cat['products']
            new_products = []
            for i in range(len(l)):
                if not str(i) in ans1:
                    new_products.append(l[i])
            cat['products'] = new_products

        elif inp == "q":
            running = False

def addProduct(cat):
    prod = None
    prod_type = input("What type of product is it? \n('' - regular, 'b' - box, 'f' - bottle, 's' - snacks):\n")
    if prod_type == "" or prod_type == "regular" or prod_type == "r":
        prod = addRegular()
    elif prod_type == "b" or prod_type == "box" or prod_type == "boks":
        prod = addWineBox()
    elif prod_type == "f" or prod_type == "flaske" or prod_type == "bottle":
        prod = addWineBottle()
    elif prod_type == "s" or prod_type == "snack" or prod_type == "snacks":
        prod = addSnacks()
    return prod

def defaultProduct():
    new = {}
    new['name'] = input('Name:\n>')
    new['volume'] = float(input('Volume:\n>'))
    new['price'] = int(input('Price:\n>'))
    try:
        n = int(input("Price internal:\n"))
    except:
        n = new['price'] - 5
    new['priceIntern'] = n
    new['active'] = input("Activate? (y/n)") == "y"
    new['glutenfree'] = input("Glutenfree? (y/n)") == "y"
    return new

def addRegular():
    new = defaultProduct()
    new['type'] = "regular"
    return new

def addSnacks():
    new = defaultProduct()
    new['type'] = "snacks"
    return new

def addWineBottle():
    new = {}
    new['name'] = input('Name:\n>')
    new['price1'] = int(input('price glass:\n>'))
    try:
        n = int(input("price glass internal('' for ",new['price1']-5,":\n>"))
    except:
        n = new['price1'] -5
    new['price1Intern'] = n
    new['price2'] = int(input('price bottle:\n>'))
    try:
        n = int(input("price bottle internal('' for ",new['price2']-5,":\n>"))
    except:
        n = new['price2'] -5
    new['price2Intern'] = n
    new['active'] = input("activate? (y/n)") == "y"
    new['glutenfree'] = input("glutenfree? (y/n)") == "y"
    new['type'] = "flaske"
    new['info'] = input("Any additional info:\n")
    return new

def addWineBox():
    new = defaultProduct()
    new['type'] = "boks"
    new['info'] = input("Any additional info:\n")
    return new

def print_info(info):
    print()
    for i, d in enumerate(info):
        print(str(i) + ": " + d['name'])
    print()

if __name__ == "__main__":
    main()
