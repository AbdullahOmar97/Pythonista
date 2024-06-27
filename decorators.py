import time

def runtime_decorator(func):
    """
    Decorator that measures and prints the runtime of the decorated function.

    Args:
    - func: The function to be decorated.

    Returns:
    - wrapper function that measures runtime and calls the original function.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that measures runtime and calls the original function.

        Args:
        - *args: Positional arguments for the decorated function.
        - **kwargs: Keyword arguments for the decorated function.

        Returns:
        - The result of the decorated function call.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("I am a really good pythonista developer at ASAC")
        print(f"Runtime: {end_time - start_time} seconds")
        return result
    return wrapper

def bold_decorator(func):
    """
    Decorator that wraps the output of the decorated function with <b> tags.

    Args:
    - func: The function to be decorated.

    Returns:
    - wrapper function that wraps the function's output with <b> tags.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that wraps the function's output with <b> tags.

        Args:
        - *args: Positional arguments for the decorated function.
        - **kwargs: Keyword arguments for the decorated function.

        Returns:
        - String with <b> tags around the original function's output.
        """
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic_decorator(func):
    """
    Decorator that wraps the output of the decorated function with <i> tags.

    Args:
    - func: The function to be decorated.

    Returns:
    - wrapper function that wraps the function's output with <i> tags.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that wraps the function's output with <i> tags.

        Args:
        - *args: Positional arguments for the decorated function.
        - **kwargs: Keyword arguments for the decorated function.

        Returns:
        - String with <i> tags around the original function's output.
        """
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

def underline_decorator(func):
    """
    Decorator that wraps the output of the decorated function with <u> tags.

    Args:
    - func: The function to be decorated.

    Returns:
    - wrapper function that wraps the function's output with <u> tags.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that wraps the function's output with <u> tags.

        Args:
        - *args: Positional arguments for the decorated function.
        - **kwargs: Keyword arguments for the decorated function.

        Returns:
        - String with <u> tags around the original function's output.
        """
        return "<u>" + func(*args, **kwargs) + "</u>"
    return wrapper
