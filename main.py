import random


class DataStructure:
    def __init__(self):
        """
        Initializes the Data_structure with an empty list and an empty index map.
        """
        self.values = []
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
        self.values.append(val)
        self.index_map[val] = len(self.values) - 1

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
        last_element = self.values[-1]
        self.values[index] = last_element
        self.index_map[last_element] = index
        self.values.pop()
        del self.index_map[val]
        print(f"Successfully delete {val} from data structure")

    def get_random(self):
        """
        Prints a random element from the data structure.

        If the list is not empty, a random element is selected from the list and printed.
        """
        if self.values:
            print(f"random element by choice : {random.choice(self.values)}")
        else:
            print("Data Structure is empty")

    def test_get_random(self, range_num):
        """
        Tests the randomness of the `getrandom` method by selecting random elements from the list
        multiple times and recording the frequency of each element.

        Parameters:
        range_num (int): The number of times to randomly select an element from the list.

        Prints the frequency distribution of each element after `range_num` random selections.
        This helps in verifying that each element has an equal probability of being chosen.
        """
        if self.values:
            probability_dic = {}
            for i in range(range_num):
                random_num = random.choice(self.values)
                probability_dic[random_num] = probability_dic.get(random_num, 0) + 1
            print(
                f"Probability of each element for {range_num} trials: {probability_dic}"
            )
        else:
            print("Data Structure is empty")

ds_object = DataStructure()

ds_object.insert(20)  # Inserts 20, list: [20], index_map: {20: 0}
# Explanation: 20 is added to the list. The index_map is updated to reflect that 20 is at index 0.


ds_object.insert(50)  # Inserts 50, list: [20, 50], index_map: {20: 0, 50: 1}
# Explanation: 50 is added to the end of the list. The index_map is updated to show that 50 is at index 1.


ds_object.insert(
    80
)  # Inserts 80, list: [20, 50, 80], index_map: {20: 0, 50: 1, 80: 2}
# Explanation: 80 is appended to the list. The index_map is updated to indicate that 80 is at index 2.


ds_object.insert(
    90
)  # Inserts 90, list: [20, 50, 80, 90], index_map: {20: 0, 50: 1, 80: 2, 90: 3}
# Explanation: 90 is added to the list. The index_map is updated to show that 90 is at index 3.

ds_object.delete(
    80
)  # Deletes 80, list: [20, 50, 90], index_map: {20: 0, 50: 1, 90: 2}
# Explanation: 80 is removed from the list. The last element (90) replaces 80's position. The index_map is updated to reflect the new index of 90.


ds_object.get_random()  # Prints a random element from the list: could be 20, 50, or 90
# Explanation: A random element is selected from the current list. The element is chosen randomly with equal probability.

ds_object.test_get_random(1000000)
