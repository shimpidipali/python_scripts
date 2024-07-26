## Data Structures and Algorithms

### Data Structures Used

1. **List (`self.list`)**:
   - **Purpose**: Stores the actual elements in the data structure.
   - **Implementation**: A dynamic array (list) that supports efficient indexing and appending.

2. **Dictionary (`self.index_map`)**:
   - **Purpose**: Maps each element to its index in `self.list`. This enables fast lookups and updates.
   - **Implementation**: A hash table (dictionary), providing average \( O(1) \) time complexity for insertions, deletions, and lookups.

### Methods and Time Complexity

#### 1. Insertion (`insert(val: int)`)

- **Algorithm**:
  1. **Check Existence**:
     - **Operation**: Check if `val` is already present in `self.index_map`.
     - **Time Complexity**: \( O(1) \) on average. 
     - **Reason**: Dictionary in Python is implemented as a hash table, and the “in” operator uses hash table lookups to find the key, which takes constant time on average.
  2. **Add to List**:
     - **Operation**: Append `val` to `self.list`.
     - **Time Complexity**: \( O(1) \) on average.
     - **Reason**: Lists are spontaneously accessed, the very last item can be reached in O(1) time, which is why adding any new item at the end of the list takes O(1) time.
  3. **Create Dictionary**:
     - **Operation**: Update `self.index_map` with the new index of `val`.
     - **Time Complexity**: \( O(1) \) on average.

- **Overall Complexity**: The insertion operation is \( O(1) \) because each step (checking existence, appending, and updating) is performed in constant time.

#### 2. Deletion (`delete(val: int)`)

- **Algorithm**:
  1. **Check Existence**:
     - **Operation**: Check if `val` exists in `self.index_map`.
     - **Time Complexity**: \( O(1) \) on average.
     - **Reason**: Dictionary in Python is implemented as a hash table, and the “in” operator uses hash table lookups to find the key, which takes constant time on average.
  2. **Locate and Replace**:
     - **Operation**: 
       - Retrieve the index of `val` from `self.index_map`.
       - Swap `val` with the last element in `self.list`.
       - Update the index of the swapped element in `self.index_map`.
     - **Time Complexity**: \( O(1) \) for each operation.
  3. **Remove**:
     - **Operation**: Remove the last element from `self.list` and delete `val` from `self.index_map`.
     - **Time Complexity**: \( O(1) \).
     - **Reason(list.pop())**: In this operation, the top element is removed and the pointer that was pointing to the topmost element now points to the one just below it. The operations performed in this case are all performed in constant time.
     - **Reason(del function)**: O(1) on average, O(n) worst case if there are many collisions

- **Overall Complexity**: The deletion operation is \( O(1) \) because all steps (checking existence, locating, swapping, and removal) are performed in constant time.

#### 3. Random Access (`getrandom()`)

- **Algorithm**:
  - **Operation**: Use `random.choice(self.list)` to select a random element from `self.list`.
  - **Time Complexity**: \( O(1) \) on average.
  - **Note**: `random.choice(self.list)` selects a random element from the list in constant time.

- **Overall Complexity**: The random access operation is \( O(1) \) because selecting a random element from the list is a constant-time operation.
<br>
<br>

## Space Complexity of the `insert`, `delete`, `random` Operations

### Immediate Space Usage for Each Operation
 \( O(1) \) for individual operations like checking, appending, updating, or selecting a random element.

### Overall Space complexity
 \( O(n) \) where n is the number of elements in the data structure. This is because both the list and index map grow linearly with the number of elements.

## Example Usage

Here's how the `Data_structure` class is used:

```python
random_list = Data_structure()

random_list.insert(20)  # Inserts 20 into the data structure
random_list.insert(50)  # Inserts 50 into the data structure
random_list.insert(80)  # Inserts 80 into the data structure
random_list.insert(90)  # Inserts 90 into the data structure
random_list.delete(80)  # Delete 80 from the data structure
random_list.getrandom() # Gets a random element from the data structure