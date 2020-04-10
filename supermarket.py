class Tovar:
    def __init__(self, price, category, name, counter):
        self.price=price
        self.category=category
        self.name=name
        self.counter=counter
    def is_eatable(self):
        if self.category!='household chemicals':
            return True
        else: return False
    def price_total(self, amount):
        return self.price*amount

class Basket:
    def __init__(self, my_list):
        self.my_list=my_list
    def total(self):
        sum=0
        for key,value in self.my_list:
            sum+=key.price_total(value)
        return sum
    def totally_eatable(self):
        flag=True
        for key, value in self.my_list:
            if key.is_eatable()==False:
                flag=False
        return flag
bread=Tovar(10, 'food', 'bread', 'one')
milk=Tovar(17, 'drink', 'milk', 'one')
apple=Tovar(13, 'food', 'apple', 'kg')
soap=Tovar(7, 'household chemicals', 'soap', 'one')
need=Basket([[bread, 2], [milk, 1], [apple, 4], [soap, 3]])
print(bread.price_total(13))
print(soap.is_eatable())
print(need.total())
print(need.totally_eatable())
