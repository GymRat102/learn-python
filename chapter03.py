print("--------------------chapter03--------------------")
# 列表简介
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') # 末尾追加元素
print(motorcycles)
motorcycles.insert(0, 'ducati') # 指定索引位置插入元素
print(motorcycles)
del motorcycles[0] # 使用del和索引来删除元素
print(motorcycles)
popped_motorcycle = motorcycles.pop() # 使用pop弹出末尾元素就可以使用被弹出的值
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title()) # pop方法也可以和索引一起使用
motorcycles.remove('yamaha') # remove根据值来删除，删除第一个出现的元素

# list.sort()对列表的排序修改是永久性的，可以按字母顺序反向排序
cars = ['bmw', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# sorted(list)以特定的顺序呈现列表
print(sorted(cars))
print(sorted(cars, reverse=True))
print("------")

# list.reverse()永久性地倒转列表
cars = ['bmw', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))

# 列表为空时，通过-1访问列表会报错
a_list = []
print(a_list[-1])