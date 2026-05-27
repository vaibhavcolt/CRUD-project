from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, NotFound

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # If the response is None, it means it's an unhandled exception, 
    # but we will wrap handled exceptions into our custom format.
    if response is not None:
        custom_response_data = {
            "success": False,
        }
        
        # Handle validation errors (e.g., Duplicate email, invalid fields)
        if isinstance(exc, ValidationError):
            # Extract first error message or format it
            errors = response.data
            if isinstance(errors, dict):
                first_key = list(errors.keys())[0]
                error_msg = errors[first_key]
                if isinstance(error_msg, list):
                    error_msg = error_msg[0]
                
                # Check for specific duplicate email case from unique validator
                if 'user with this email already exists' in str(error_msg).lower():
                    custom_response_data['error'] = 'Duplicate email'
                else:
                    custom_response_data['error'] = f"{first_key}: {error_msg}"
            elif isinstance(errors, list):
                custom_response_data['error'] = errors[0]
            else:
                custom_response_data['error'] = str(errors)

        # Handle Not Found (e.g., User not found)
        elif isinstance(exc, NotFound):
            custom_response_data['error'] = "User not found"
        else:
            # Default fallback for other handled exceptions
            custom_response_data['error'] = str(exc.detail) if hasattr(exc, 'detail') else str(exc)

        response.data = custom_response_data

    return response
