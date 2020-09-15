def check_doc_string_len():
    """ Closure function to generate function to check doc string length > 50
    Returns:
        inner: function
    """
    doc_str_threshold = 50
    def doc_length_check(fn):
        fn_len = len(fn.__doc__.replace("\n",""))
        print('Docstring: {0}\nCharacter Count = {1}'.format(fn.__doc__,fn_len))
        return fn_len > doc_str_threshold
    return doc_length_check

check_doc_str = check_doc_string_len()


def gen_next_fibonacci_num():
    """ Closure function to generate next fibonacci number
    Returns:
        fibonacci: function
    """
    num1 = 0
    num2 = 0
    def fibonacci():
        nonlocal num1, num2
        if num1 ==0 and num2 ==0:
            num2 = 1
        else:
            num2, num1 = num1+ num2, num2
        return num1
    return fibonacci

# Creating a function to generate the next fibonacci number
fibonacci = gen_next_fibonacci_num()

def add(a, b):
    """ Addition function

    """
    return a+b

def mul(a, b):
    """ Multiplication function

    """
    return a*b

def div(a, b):
    """ Division function

    """
    return a/b


cnt={}
def counter(fn):
    """ Closure function to create a counter function 
    Counter will be saved as dictionary with key as function name
    Args:
        fn: function call to be counted
        cnt: is global counter
    Return:
        inner: function
    """
    key = ""
    def inner(*args, **kwargs):
        global cnt
        nonlocal key
        key = fn.__name__
        if key not in cnt:            
            cnt[key] = 0
        cnt[key] += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt[key]))
        return fn(*args, **kwargs)
    return inner


def user_counter(fn,cnt):
    """ Closure function to create a counter function 
    Counter will be saved as dictionary with key as function name
    Args:
        fn: function call to be counted
        cnt: user defined counter for each user different
    Return:
        inner: function
    """
    key = ""
    def inner(*args, **kwargs):
        nonlocal key
        key = fn.__name__
        if key not in cnt:            
            cnt[key] = 0
        cnt[key] += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt[key]))
        return fn(*args, **kwargs)
    return inner