from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

#funcao de emergencia para resetar dados do admin no sistema
class Command(BaseCommand):
    help = 'resetar dados do admin no sistema'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        try:
            admin_user = User.objects.get(id=1)
            admin_user.nome = 'Administrador'
            admin_user.password = make_password('123456')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Dados do admin resetados com sucesso'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Você precisa rodar o comando inicializa_sistema primeiro'))