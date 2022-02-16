import json  
def main():
    data = json.load(open("./data.json"))

    print("Select a category to edit:")
    for i, d in enumerate(data):
        print("", i,": ", d['name'])
    
    ch = input(
            "Choose a category. "+
            "Enter index to edit category, "+
            "'a' to add a category, "+
            "'c' to change order, "+
            "x to delete\n>")

    if ch == 'a':
        new = {}
        new['name'] = input("The new category's name\n>")
        new['products'] = []
        data.append(new)
    elif ch == 'c':
        print("Select a category to move:")

        for i, d in enumerate(data):
            print("", i,": ", d['name'])
        ans1 = int(input("index of item to be moved"))
        ans2 = int(input("new index of item (others will be offset)"))
        
        item = data.pop(ans1)
        # print(data)
        if ans1 < ans2:
            ans2 -= 1
        data.insert(ans2, item)
        # print(data)
    elif ch == 'x':
        print("Select a category to delete:")

        for i, d in enumerate(data):
            print("", i,": ", d['name'])
        ans1 = int(input("index of item to be moved"))
        
        item = data.pop(ans1)

    else:
        try:
            i = int(ch)
            enterCategory(i, data)
        except Exception as e:
            print(type(e))
            print(e)
            print("You didnt do it right >:(")
            exit()
    for i, d in enumerate(data):
        print("", i,": ", d['name'])
    if input("Save changes?") == "y":
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)

def editProduct(cat):
    print("Select a product to edit:")
    for i, c in enumerate(cat['products']):
        print("", i,": ", c['name'])
    ch = int(input("Choose a product\n>"))
    product = cat['products'][ch] 

    attr_list = list(product.keys())
    for i, p in enumerate(attr_list):
        print("", i,": ", p, product[p])
    inp = int(input("choose an attribute"))

    attr= attr_list[inp]
    t = type(product[attr])
    if t == type(True):
        print("its a bool")
        v = input("toggle?(y/n)") == "y"
        # a lil xor
        a = product[attr]
        product[attr] = not a if v else a
    elif t == type(0.1):
        num = float(input("What should the value be changed to?"))
        product[attr] = num
    elif t == type(1):
        num = int(input("What should the value be changed to?"))
        product[attr] = num
    elif t == type(""):
        num = input("What should the value be changed to?")
        product[attr] = num
    else:
        print(product[attr].__class__(), "has not been coverd")

def enterCategory(categoryIndex, data):
    cat = data[categoryIndex]
    print("you chose the category:", cat['name'])
    print("What do you want to do?")
    inp = input("a - add, e - edit, c - change order, m - move to other category x - delete\n>")

    if inp == "a":
        cat['products'].append( addProduct(data))
    elif inp == "e":
        editProduct(cat)
    elif inp == "c":
        print("Select a product to move:")
        for i, d in enumerate(cat['products']):
            print("", i,": ", d['name'])
        ans1 = int(input("index of item to be moved"))
        ans2 = int(input("new index of item (others will be offset)"))
        l = cat['products']
        item = l[ans1]
        l.remove(item)
        if ans1 < ans2:
            ans2 -= 1
        l.insert(ans2, item)
    elif inp == "m":
        print("Select a product to move:")
        for i, d in enumerate(cat['products']):
            print("", i,": ", d['name'])
        ans1 = int(input("index of item to be moved"))
        print("Select a category to move to:")
        for i, d in enumerate(data):
            print("", i,": ", d['name'])
        ans2 = int(input("index of category to move to"))
        l= cat["products"]
        item = l[ans1]
        l.remove(item)
        data[ans2]["products"].insert(ans2, item);

    elif inp == "x":
        print("Select a product to delete:")
        for i, d in enumerate(cat['products']):
            print("", i,": ", d['name'])
        ans1 = int(input("index of item to delete"))
        l = cat['products']
        item = l[ans1]
        l.remove(item)
                


def addProduct(cat):
    prod = None
    prod_type = input("What type of product is it? ('' for regular, 'b' for box, 'f' for bottle, 's' for snacks)")
    if prod_type == "" or prod_type == "regular" or prod_type == "r":
        prod = addRegular()
    elif prod_type == "b" or prod_type == "box" or prod_type == "boks":
        prod = addWineBox()
    elif prod_type == "f" or prod_type == "flaske" or prod_type == "bottle":
        prod = addWineBottle()
    elif prod_type == "s" or prod_type == "snack" or prod_type == "snacks":
        prod = addSnacks()
    return prod

def addRegular():
    new = {}
    new['name'] = input('Name:\n>')
    new['volume'] = float(input('Volume:\n>'))
    new['price'] = int(input('price:\n>'))
    try:
        n = int(input("price internal('' for ", new['price']-5,":\n>"))
    except:
        n = new['price'] -5 
    new['priceIntern'] = n
    new['active'] = input("activate? (y/n)") == "y" 
    new['glutenfree'] = input("glutenfree? (y/n)") == "y" 
    new['type'] = "regular"
    return new

def addSnacks():
    new = {}
    new['name'] = input('Name:\n>')
    new['volume'] = float(input('Volume:\n>'))
    new['price'] = int(input('price:\n>'))
    try:
        n = int(input("price internal('' for ",new['price']-5,":\n>"))
    except:
        n = new['price'] -5 
    new['priceIntern'] = n
    new['active'] = input("activate? (y/n)") == "y" 
    new['glutenfree'] = input("glutenfree? (y/n)") == "y" 
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
    new['info'] = input("Any additional info?")
    return new
def addWineBox():
    new = {}
    new['name'] = input('Name:\n>')
    new['volume'] = float(input('Volume:\n>'))
    new['price'] = int(input('price:\n>'))
    try:
        n = int(input(
            "price internal('' for ",new['price']-5,":\n>"))
    except:
        n = new['price'] -5 
    new['priceIntern'] = n
    new['active'] = input("activate? (y/n)") == "y" 
    new['glutenfree'] = input("glutenfree? (y/n)") == "y" 
    new['type'] = "boks"
    new['info'] = input("Any additional info?")
    return new
# for d in data:
#     for p in d['products']:
#         try:
#             a = p['priceIntern']
#         except KeyError:
#             try:
#                 p['priceIntern'] = p['price'] - 5
#             except KeyError:
#                 p['price1Intern'] = p['price1'] - 5
#                 p['price2Intern'] = p['price2'] - 5


if __name__ == "__main__":
    main()
