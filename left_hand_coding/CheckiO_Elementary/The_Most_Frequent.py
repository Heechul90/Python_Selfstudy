### The_Most_Frequent



def the_most_frequent(data):
    return max(data, key = data.count)


the_most_frequent(['a', 'a', 'a', 'a', 'b', 'b', 'b'])
the_most_frequent(['a', 'a', 'a', 'b', 'b', 'c', 'c'])
