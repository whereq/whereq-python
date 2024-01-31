msg = "Hello Mars!"
int_array = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(msg)
    print(int_array)
    foo('apple')
    x = Foo()
    print(x)