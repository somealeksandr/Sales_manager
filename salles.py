if __name__ == "__main__":
    start()

def start(items):
    
    db_items = items
    exit = False
    while not exit:
        print("====================Sales Manager==================")
        choice = int(input("1. Show items\n2. Add items\n3. Delete item\n4. Sort by Price\n5. Sell item\n6. Selling statistic\n0. Exit\n"))
        print("User choice => ", choice)
        if choice == 1:
            show_items(db_items)
        elif choice == 2:
            add(db_items)
        elif choice == 3:
            delete(db_items)
        elif choice == 4:
            sort_by_price(db_items)
        elif choice == 5:
            sell(db_items)
        elif choice == 6:
            sell_statistics(db_items)               
        elif choice == 0:
            exit = True
        else:
            print("Read the manual")        


def show_items(items):
    for item in items:
        print(item["id"], item['name'].join('||'),
              item['model'].join('||'), str(item["price"]).join('[]'))



def add(items):
    name = input("Enter name: ")
    model = input("Enter model: ")
    price = input("Enter price: ")
    items.append({"id": len(items)+1, "name": name, "model": model, "price": price})

def delete(items):
    delete_phone = input("Enter the phone you want to delete:  ")
    items.pop(int(delete_phone))

def sort_by_price(items):
    sort = int(input("Enter sort by:\nID : 1\nPrice : 2\nName : 3\n=>: "))
    if sort == 1:
        sort = "id"
    elif sort == 2:
        sort = "price"
    else:
        sort = "name"
        
    sorted_items = sorted(items, key=lambda item: item[sort])
    print(sorted_items)
    input()
    return sorted_items

def sell(items):
    print(items)
    sell_item = input("Enter a number of item you wan't to buy: ")
    for item in items:
        return item["id"].pop(int(sell_item))


def sell_statistics(soled):
    print("[", soled, "]-- Items was sold")
    input("Enter to continue")    


        



    
    