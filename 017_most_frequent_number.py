# To improve your defining function skills and reinforce your knowledge of max() and .count.

# Given a list, return the most frequent (repeating) element.


# Note : If there are the same number of repeating elements, it returns the first element that repeats most from left to right in the list.


def most_freq(given_list):   
    counts = [ given_list.count(i) for i in given_list]
    index = -1
    for i in counts:
        index += 1
        if i == max(counts):
            return given_list[index]
    
        
print(most_freq([3,1,2,2,2,2,1,1,3]))