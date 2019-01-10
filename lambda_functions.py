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


