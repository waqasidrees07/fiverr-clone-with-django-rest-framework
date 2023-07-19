from django.shortcuts import redirect


class PreventLoginAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == '/accounts/login/':
            # User is already logged in, redirect to another page
            return redirect('home')  # Replace 'home' with the appropriate URL or name of the desired page

        response = self.get_response(request)
        return response
