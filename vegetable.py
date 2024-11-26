vegetable = ['potato', 'onion', 'brinjal', 'tomato', 'mirchi', 'ladyfinger', 'peas', 'bitter gourd', 'garlic',
             'mushroom', 'tinda', 'turnip', 'parmal', 'taro', 'beetroot', 'long beans', 'lemon', 'ginger', 'bottle gourd',
             'radish', 'spinach', 'ridge gourd', 'cucumber', 'yam', 'fenugreek', 'lima beans', 'lettuce', 'sweet potato']
quantity = [20, 30, 15, 25, 10, 20, 10, 5, 2, 22, 5, 6, 8, 4, 10, 13, 5, 2, 3, 5.5, 3.5, 5, 10, 0.5, 2.5, 10, 1, 10.5]
price = [30, 25, 45, 20, 70, 40, 50, 35, 80, 85, 15, 19, 28, 19, 20, 44, 57, 150, 22, 33, 12, 40, 35, 5, 20, 34, 38, 40]
print('*' * 10, 'WELCOME TO SUPER MARKET', '*' * 10)
while True:
    print('1.shopkeeper')
    print('2.customer')
    print('3. quantity')
    select = int(input('enter a number(1 or 2 or 3): '))
    if select == 1:
        while True:
            print('a.adding vegetables')
            print('b.removing vegetables')
            chA = input('enter a alphabetic from the above(a/b): ').lower()
            if chA == 'a':
                chVeg = input('which vegetable want to add: ')
                if chVeg not in vegetable:
                    vegetable.append(chVeg)
                    idx = vegetable.index(chVeg)
                    chQty = float(input('how much quantity added '))
                    quantity.insert(idx, chQty)
                    chPrz = float(input('add price: '))
                    price.insert(idx, chPrz)
                    print(vegetable)
                    print(quantity)
                    print(price)
                elif chVeg in vegetable:
                    zzz = float(input('how much quantity want to add '))
                    id = vegetable.index(chVeg)
                    quantity.insert(id, zzz)
                    quantity.pop(id+1)
                    print(vegetable)
                    print(quantity)
                    print(price)
                else:
                    print('already in the list')
                z = input('if you want to add another vegetable(yes/no): ')
                if z == 'no':
                    break
            if chA == 'b':
                chdVeg = input('which vegetable want to remove: ')
                if chdVeg in vegetable:
                    idx = vegetable.index(chdVeg)
                    vegetable.remove(chdVeg)
                    quantity.pop(idx)
                    price.pop(idx)
                    print(vegetable)
                    print(quantity)
                    print(price)
                zz = input('you want to remove another one(yes/no) : ')
                if zz == 'no':
                    break
    li = []
    qua = []
    amount = 0
    if select == 2:
        print('*'*10, 'WELCOME SUPER MARKET', '*'*10)
        print(vegetable)
        while True:
            ch = input('which vegetable you want:  ')
            if ch in vegetable:
                li.append(ch)
                idx = vegetable.index(ch)
                q = float(input('enter quantity of'))
                if q <= quantity[idx]:
                    quantity[idx] = quantity[idx] - q
                    amount = q * price[idx] + amount
                else:
                    print('quantity unavailable')
            else:
                print('out of stock')
            sss = input('do you want buy again (yes/no): ')
            if sss == 'no':
                name = input('enter your name: ')
                mobile_no = int(input('enter your mobile number: '))
                print('*'*5, 'YOUR BILL', '*'*5)
                print(name)
                print(mobile_no)
                print(li)
                print('please pay amount of: ', amount)
                print('*'*20)
                print('closing')
                '''
                print('*'*2, 'remaining quantity after shopping', '*'*2)
                for i, j in zip(vegetable, quantity):
                    print(i, '---', j, 'kg-s')
                print('*'*10)'''
                break
    if select == 3:
        print('*' * 2, 'remaining quantity after shopping', '*' * 2)
        for i, j in zip(vegetable, quantity):
            print(i, '---', j, 'kg-s')
        print('*' * 10)
        aaa = input('you want to close the shop(yes/no): ')
        if aaa == 'yes':
            break