from rest_framework.response import Response

def success_response(message, data=None, status_code=200):
    response_data = {
        "success": True,
        "message": message,
    }
    if data is not None:
        response_data["data"] = data
        
    return Response(response_data, status=status_code)

def error_response(error_message, status_code=400):
    return Response({
        "success": False,
        "error": error_message
    }, status=status_code)
