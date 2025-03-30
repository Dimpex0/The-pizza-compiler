from django.conf import  settings

EXCLUDE_FROM_MIDDLEWARE = []

class AuthorizationMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = view_func.__name__

        if hasattr(view_func, 'view_class'):
            view_name = view_func.view_class.__name__

        if view_name in EXCLUDE_FROM_MIDDLEWARE:
            return None

    def __call__(self, request):
        token = request.COOKIES.get(settings.SIMPLE_JWT['ACCESS_TOKEN'])
        if token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
        return self.get_response(request)