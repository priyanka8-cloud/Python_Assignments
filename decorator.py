def decorator_text(text):
    def decorator(func):
        def wrapping(*args, **kwargs):
            print(f"{text} Before the function call")
            func(*args, **kwargs)
            print(f"{text} After the function call")
        return wrapping
    return decorator

@decorator_text("Decorator-1")
@decorator_text("Decorator-2")
@decorator_text("Decorator-3")
def add(a, b):
    print(f"Result = {a * b}")

add(8,6)


#Order of Execution

#Wrapping order:
#1️. Decorator-3 → innermost
#2️. Decorator-2 → middle
#3️. Decorator-1 → outermost
