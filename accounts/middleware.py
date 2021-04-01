from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout


class PrintHello(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            print("***hello from middleware class")
