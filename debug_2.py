def outer_function(x):
    print(f"outer_function received {x}")

    def inner_function(y):
        print(f"inner_function received {y}")
        return y * y

    result = inner_function(x)
    print(f"Result from inner_function: {result}")

# вызов внешней функции
outer_function(5)