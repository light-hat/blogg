#from django.core.exceptions import PermissionDenied
#from security.models import Visitors
'''
class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_ips = Visitors.objects.get(blocked=True)
        blocked = []

        for addr in blocked_ips:
            blocked.append(blocked_ips.ip)
        
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        
        else:
            ip = request.META.get('REMOTE_ADDR')

        if ip in blocked:
            raise PermissionDenied
        
        response = self.get_response(request)
        
        return response
    '''
