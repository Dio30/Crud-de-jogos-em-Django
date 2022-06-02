from django.contrib import admin
from. models import Jogos

# Register your models here.
class JogosAdmin(admin.ModelAdmin):
    list_display = ['nome_do_jogo', 'tipo_de_jogo', 'valor_do_jogo', 'descrição_do_jogo', 'usuario']

admin.site.register(Jogos, JogosAdmin)