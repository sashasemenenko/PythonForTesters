def example_function():
    lacal_var = "I'm a local var"
    print(f"Inside example_function: {lacal_var}")


example_function()

global_var = "I'm a global var"
def example_function_2():
    global global_var
    global_var = "I'm modified global var"
    print(f"Inside example_function: {global_var}")

example_function_2()
print(f"Outside example_function: {global_var}")