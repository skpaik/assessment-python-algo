def my_get(n):
    for i in range(n):
        yield i ** 2


gen = my_get(4)

result = [i for i in gen if i % 2 == 0]

print(result)

dict1 = {'first': 'apple', 'second': 'mango'}

dict2 = {1: 3, 2: 4}

dict1.update(dict2)

print(dict1[2])


class CarList:
    def __init__(self, name):
        self.name=name

    @staticmethod
    def get_cars(name):
        cars=["HONDA", "BMW"]
        return cars

    def start(self):
        print(self.get_cars(self.name))


i = CarList("MyCars")
i.start()



original_dict= {"A": [1,2,3], "B": {"X": 4, "Y": 5}}

new_dict= dict(original_dict)

new_dict["A"].append(4)
new_dict["B"]["Z"]=6


print(original_dict)
print(new_dict)


dict_1={"a": 1, "b": 2, "C": 3}
dict_2=dict.fromkeys(['a', 'b', 'c'], 0)
dict_3={}

# for i in range(len(dict_1)):
#     dict_3[dict_1.keys()[i]] = dict_1.values()[i]+dict_2[dict_1.keys()[i]]



fruits =["Apple", "Mango", "Guava"]
colors=["Red", "Yellow", "Green"]

print(list(zip(fruits, colors)))