from .models import Usuario, Aluno

class AttachUsuarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                # Vincular o modelo Usuario ao request
                request.usuario = Usuario.objects.get(user=request.user)
                
                # Verificar se o tipo_de_usuario é 'Aluno'
                if request.usuario.tipo_de_usuario == 'Aluno':
                    try:
                        # Vincular o modelo Aluno ao request
                        request.aluno = Aluno.objects.get(usuario=request.usuario)
                    except Aluno.DoesNotExist:
                        request.aluno = None
                else:
                    request.aluno = None
            except Usuario.DoesNotExist:
                request.usuario = None
                request.aluno = None
        else:
            request.usuario = None
            request.aluno = None

        response = self.get_response(request)
        return response
