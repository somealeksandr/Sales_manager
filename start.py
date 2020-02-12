# a = [1, 22, 45, 34, 23, "Bill"]
# b = ["monday", True, "Test"]

# c = a + b
# print(type(c), c)
# c = tuple(c)
# print(type(c), c)

# print(c[-1])

# c = "Bill", 34, "Admin"
# print(type(c))
# name, age, role = c
# print(name)
# print(age)
# print(role)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
 
 
# user = get_user()
# print(user[0])              # Tom
# print(user[1])              # 22
# print(user[2])              # False




                # TASK

# Написати модуль (sales_manager) який реалізеє діалог з користувачем (Меню) наступний функціонал:

# 1. Показати всі товари
# 2. Додати товар
# 3. Видалити товар
# 4. Сортувати за ціною
# 5. Продати товар (проданий товар записується в інший список)
# 6. Показати продані товари
# 0. Вийти

from salles import start


phones = [
    {
    "id" : 1,    
    "name" : "samsung",
    "model" : "s10",
    "price": "23000"
    },
    {
    "id" : 2,      
    "name" : "xiaomi",
    "model" : "4x",
    "price" : "4000"
    },
    {
    "id" : 3,      
    "name" : "iPhone",
    "model" : "XR",
    "price" : "25000"
    },
    {
    "id" : 4,      
    "name" : "asus",
    "model" : "464",
    "price" : "4500"
    },
    {
    "id" : 5,      
    "name" : "CAT",
    "model" : "cv89",
    "price" : "45000"
    }
]


# for item in phones:
#     print(item, " \n ")
try:
    start(phones)
except:
    print("is not tuple")