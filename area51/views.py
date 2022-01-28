from django.shortcuts import render

def bad_request_view(request, exception):
    return render(request, 'error/400.html', status=400)

def access_denied_view(request, exception):
    return render(request, 'error/403.html', status=403)
    
def page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)

def not_allowed_view(request, exception):
    return render(request, 'error/405.html', status=405)

def timeout_view(request, exception):
    return render(request, 'error/408.html', status=408)

def server_error_view(request):
    return render(request, 'error/500.html', status=500)