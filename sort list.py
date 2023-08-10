def sort_list(list1, sort_type):
    if sort_type == "asc":
        list1.sort()
        return list1
    elif sort_type == "desc":
        list1.sort(reverse=True)
        return list1
    else:
        return list1


numbers_list = list(input("""Enter a list of numbers
"""))
sort_input = str(input("""Enter a type of sort. 'asc' for ascending, 'desc' for descending and leave empty for no sort.
"""))
list_sorted = sort_list(numbers_list, sort_input)
print(list_sorted)
