from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    arr=[0]*size
    arr[index]=value
    return arr



# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
