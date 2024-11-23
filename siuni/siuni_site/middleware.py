from .models import Usuario

class AttachUsuarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.usuario = Usuario.objects.get(user=request.user)
            except Usuario.DoesNotExist:
                request.usuario = None
        else:
            request.usuario = None

        response = self.get_response(request)
        return response