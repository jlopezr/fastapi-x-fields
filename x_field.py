from typing import Callable

def x_field(**kwargs) -> Callable:
    def decorator(func: Callable) -> Callable:
        if not hasattr(func, 'x_fields'):
            func.x_fields = {}
        func.x_fields.update(kwargs)
        return func
    return decorator