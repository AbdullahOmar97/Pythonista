import time

def runtime_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("I am a really good pythonista developer at ASAC")
        print(f"Runtime: {end_time - start_time} seconds")
        return result
    return wrapper

def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

def underline_decorator(func):
    def wrapper(*args, **kwargs):
        return "<u>" + func(*args, **kwargs) + "</u>"
    return wrapper
