import random


class Data_structure:
    def __init__(self):
        self.list = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            print(f"{val} already present in Data Structure")
            return
        self.list.append(val)
        self.index_map[val] = len(self.list) - 1

    def delete(self, val):
        if val not in self.index_map:
            print(f"{val} Not found in Data Structure")
            return
        index = self.index_map[val]
        last_element = self.list[-1]
        self.list[index] = last_element
        self.index_map[last_element] = index
        self.list.pop()
        del self.index_map[val]
        print(f"Successfully delete {val} from data structure")

    def getrandom(self):
        index = random.randint(0, len(self.list) - 1)
        print(f"random element : {self.list[index]}")

    def print_state(self):
        print(self.list)


random_list = Data_structure()

random_list.insert(20)
random_list.insert("jhghj")
random_list.insert(20)
random_list.delete(20)
random_list.getrandom()
random_list.print_state()
