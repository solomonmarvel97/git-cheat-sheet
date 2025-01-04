# import the function from marv.py
from marv import get_marvs_info 


def print_hello(name:str) -> str:
    return f"Hello, {name}!"

print(print_hello("Marv"))

def add(a:int,b:int) -> int:
    return a + b

print(add(1,2))


print(get_marvs_info())