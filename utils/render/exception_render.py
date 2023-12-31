from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Handle validation errors
        response.data = {
            "message": exc.default_code,
            "errors": response.data,
        }

    return response
