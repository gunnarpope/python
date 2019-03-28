# lambda_functions.py
# by: gunnar pope

# here are some basic examples of using lambda functions in python
# to run, enter this in the terminal:
# $ python lambda_functions.py


# example 1: 
# filter a list of integers having a greater value than threshold


if __name__ == '__main__':
    
    x = list(range(10))

    # filter a list of values having a greater value than threshold
    threshold = 7
    filtered = list(filter(lambda x: x>threshold,x))
    print('Example 1:')
    print('Input: ', x)
    print('Output: ', filtered)

    # Program to double each item in a list using map()

    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    
    new_list = list(map(lambda x: x * 2 , my_list))
    
    # Output: [2, 10, 8, 12, 16, 22, 6, 24]
    print(new_list)
    
