
def get_common_elements(list1, list2):
    """This function uses list comprehension to find common elements in two lists."""
    return [elem for elem in list1 if elem in list2]

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(get_common_elements(list1, list2))
