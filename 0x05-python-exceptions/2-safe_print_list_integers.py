def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    index = 0  # Index for accessing elements in my_list
    while count < x:  # Print x integers at most
        try:
            element = my_list[index]
            if type(element) == int:
                print("{:d}".format(element), end=" ")
                count += 1  # Increment counter
        except IndexError:  # x is greater than the length of my_list
            break
        except (ValueError, TypeError):  # Skip non-integer elements
            pass
        index += 1  # Increment index
    print()  # Print new line after printing integers
    return count
