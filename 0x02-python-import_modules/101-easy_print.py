#!/usr/bin/python3

__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))
102-magic_calculation.py:
    #!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return (c)

        else:
            return (sub(a, b))

