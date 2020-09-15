
import inspect
import os
import re

import pytest

import session8


README_CONTENT_CHECK_FOR = ["check_doc_string_len","gen_next_fibonacci_num","add","mul","div","counter","user_counter"]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_docstring():
    functions = inspect.getmembers(session8, inspect.isfunction)

    for func in functions:
        assert not func.__doc__ is None, f"docstring not included in {func}"

def test_closure():
    assert bool(session8.check_doc_str.__closure__) == True, "check_doc_string_len is not a closure"

def test_freevar():
    assert session8.check_doc_str.__code__.co_freevars[0] == 'doc_str_threshold', "doc_str_threshold is not free variable"

def test_fibonacci():
    lst = [0,1,1,2,3,5,8]
    gen_lst = [session8.fibonacci() for _ in range(7)]
    assert lst == gen_lst,"gen_next_fibonacci_num is not working properly"

def test_counter_add():
    cnt_add = session8.counter(session8.add)
    for i in range(10):
        cnt_add(4,5)
    assert session8.cnt['add'] == 10, "Counter function is not working"

def test_counter_mul():
    cnt_mul = session8.counter(session8.mul)
    for i in range(10):
        cnt_mul(4,5)
    assert session8.cnt['mul'] == 10, "Counter function is not working"

def test_counter_div():
    cnt_div = session8.counter(session8.div)
    for i in range(10):
        cnt_div(4,5)
    assert session8.cnt['div'] == 10, "Counter function is not working"

def test_user_counter_add():
    u1, u2 = {}, {}
    cnt_add1 = session8.user_counter(session8.add, u1)
    for i in range(10):
        cnt_add1(4,5)
    assert u1['add'] == 10, "Check counter function"

    cnt_add2 = session8.user_counter(session8.add, u2)
    for i in range(8):
        cnt_add2(4,6)
    assert u2['add'] == 8, "Check counter function"

def test_user_counter_mul():
    u1, u2 = {}, {}
    cnt_mul1 = session8.user_counter(session8.mul, u1)
    for i in range(10):
        cnt_mul1(4,5)
    assert u1['mul'] == 10, "Check counter function"

    cnt_mul2 = session8.user_counter(session8.mul, u2)
    for i in range(8):
        cnt_mul2(4,6)
    assert u2['mul'] == 8, "Check counter function"

def test_user_counter_div():
    u1, u2 = {}, {}
    cnt_div1 = session8.user_counter(session8.div, u1)
    for i in range(10):
        cnt_div1(4,5)
    assert u1['div'] == 10, "Check counter function"

    cnt_div2 = session8.user_counter(session8.div, u2)
    for i in range(8):
        cnt_div2(4,6)
    assert u2['div'] == 8, "Check counter function"



