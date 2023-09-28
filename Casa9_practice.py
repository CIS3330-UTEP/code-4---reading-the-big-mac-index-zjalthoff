unordered_list1 = [60,11,64,85,121,43,30,90]

def search(unordered_list,term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            return i
    return None

print(search(unordered_list1,121)) #remember that it's offset (4 = 3)
