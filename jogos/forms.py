from django import forms
from .models import Jogos

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ['nome_do_jogo', 'tipo_de_jogo', 'valor_do_jogo', 'descrição_do_jogo']