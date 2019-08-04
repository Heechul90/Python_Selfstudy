### All_the_Same#############################
from typing import List, Any


def all_the_same(elements: List[Any]):
    return len(set(elements)) <= 1

list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
a = set(list)
a


all_the_same([1, 'a', 1])
all_the_same(list)