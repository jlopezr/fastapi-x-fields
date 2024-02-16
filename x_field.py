from typing import Callable
from fastapi.openapi.utils import get_openapi

def x_field(**kwargs) -> Callable:
    def decorator(func: Callable) -> Callable:
        if not hasattr(func, 'x_fields'):
            func.x_fields = {}
        func.x_fields.update(kwargs)
        return func
    return decorator

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )

    for route in app.routes:
        if hasattr(route, "endpoint") and hasattr(route.endpoint, "x_fields"):
            x_fields = getattr(route.endpoint, "x_fields")
            # Identify the route's operations in the OpenAPI schema
            for method in route.methods:
                # Normalize HTTP method to lowercase
                method_lower = method.lower()
                # Access the route in OpenAPI schema if it exists
                if route.path in openapi_schema["paths"] and method_lower in openapi_schema["paths"][route.path]:
                    operation = openapi_schema["paths"][route.path][method_lower]
                    # Apply x_fields to the operation
                    operation.update(x_fields)

    app.openapi_schema = openapi_schema
    return app.openapi_schema

def create_openapi(app):
    return lambda: custom_openapi(app)