def sum_decorator(function):
    def wrapper(*args, **kwargs):
        total = sum(function(*args, **kwargs))
        print(f"Total number of the list: {total}")
    return wrapper

@sum_decorator
def range_list(num):
    my_list = [x for x in range(1, num)]
    return my_list

@sum_decorator
def power_list(num):
    my_list = [x*x for x in range (1, num)]
    return my_list

@sum_decorator
def even_list(num):
    my_list = [x for x in range(1, num) if x%2==0]
    return my_list

power_list(100)