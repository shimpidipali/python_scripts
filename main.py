import random


class Data_structure:
    def __init__(self):
        """
        Initializes the Data_structure with an empty list and an empty index map.
        """
        self.list = []
        self.index_map = {}

    def insert(self, val: int):
        """
        Inserts a value into the data structure.

        If the value is already present, it will not be added again. Updates the list
        and index_map to reflect the new value.

        Parameters:
        val (int): The value to be inserted.

        Prints a message if the value is already present in the data structure.
        """
        if val in self.index_map:
            print(f"{val} already present in Data Structure")
            return
        self.list.append(val)
        self.index_map[val] = len(self.list) - 1

    def delete(self, val: int):
        """
        Deletes a value from the data structure.

        If the value is not present, no action is taken. Replaces the value to be deleted
        with the last element in the list, updates the index_map, and then removes the last element.

        Parameters:
        val (int): The value to be deleted.

        Prints a message if the value is not found in the data structure.
        """
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
        """
        Prints a random element from the data structure.

        If the list is not empty, a random element is selected from the list and printed.
        """
        if self.list:
            print(f"random element by choice : {random.choice(self.list)}")

    def test_getrandom(self, range_num):
        """
        Tests the randomness of the `getrandom` method by selecting random elements from the list
        multiple times and recording the frequency of each element.

        Parameters:
        range_num (int): The number of times to randomly select an element from the list.

        Prints the frequency distribution of each element after `range_num` random selections.
        This helps in verifying that each element has an equal probability of being chosen.
        """
        if self.list:
            probability_dic = {}
            for i in range(range_num):
                random_num = random.choice(self.list)
                probability_dic[random_num] = probability_dic.get(random_num, 0) + 1
            print(f"Probability of each element for {range_num} trials: {probability_dic}")


random_list = Data_structure()

random_list.insert(20)  # Inserts 20, list: [20], index_map: {20: 0}
# Explanation: 20 is added to the list. The index_map is updated to reflect that 20 is at index 0.


random_list.insert(50)  # Inserts 50, list: [20, 50], index_map: {20: 0, 50: 1}
# Explanation: 50 is added to the end of the list. The index_map is updated to show that 50 is at index 1.


random_list.insert(80)  # Inserts 80, list: [20, 50, 80], index_map: {20: 0, 50: 1, 80: 2}
# Explanation: 80 is appended to the list. The index_map is updated to indicate that 80 is at index 2.


random_list.insert(90)  # Inserts 90, list: [20, 50, 80, 90], index_map: {20: 0, 50: 1, 80: 2, 90: 3}
# Explanation: 90 is added to the list. The index_map is updated to show that 90 is at index 3.

random_list.delete(80)  # Deletes 80, list: [20, 50, 90], index_map: {20: 0, 50: 1, 90: 2}
# Explanation: 80 is removed from the list. The last element (90) replaces 80's position. The index_map is updated to reflect the new index of 90.


random_list.getrandom()  # Prints a random element from the list: could be 20, 50, or 90
# Explanation: A random element is selected from the current list. The element is chosen randomly with equal probability.

random_list.test_getrandom(1000000)
